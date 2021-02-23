from base64 import b64encode
import feedparser
import io
import math
import os
import re
import requests
import sys

from domain import user
from manager import word, article
import pb.learner.learner_pb2 as learner_pb2
from util import word as wd
from util import wc

class Bookmark:
    # 公開しているブックマークの数を求める
    def __init__(self):
        self.allnoun = []
        self.dic = {}
        self.bodies = []
        self.bodynoun = []
        self.bodydic = {}
        self.osusumedic = {}
        self.entries = {}

    def learn(self, hatena_id: str) -> bool:
        articles = []
        url_list = article.create(hatena_id, self.get_url(hatena_id)) # DBに新規に登録したURLを取得
        for url in url_list:
            html = wd.get_body_from_URL(url)
            if not html :
                continue # htmlが空だったら、次のurlへ

            noun = wd.get_noun(html)
            # 登場回数が多い順に3件取得
            dic = wd.get_n_dict(wd.create_dict_from_list(noun), 3)
            articles.append(article.createArticleModel(url, dic))
        return word.create(articles)

    def count_bookmark_page(self, hatena_id: str, option: str = '') -> int:
        data = requests.get(
            'https://b.hatena.ne.jp/{}/bookmark.rss?{}'.format(hatena_id, option))
        d = feedparser.parse(data.text)
        content = d['feed']['subtitle']  # 'Userのはてなブックマーク (num)'
        match = re.search(r"(はてなブックマーク \()(.*?)\)", content)
        num = match.group(2).replace(',', '')  # 公開しているブックマーク数
        if not num.isdecimal():
            print('Error: num is string', file=sys.stderr)
            return 0
        return math.ceil(int(num)/20)

    # optionには追加のクエリパラメータを記述
    def get_title(self, hatena_id: str, option: str = '') -> list[str]:
        # 1ページに20件のデータがある。ページ数を求める
        if hatena_id == "":
            return []
        max_page = self.count_bookmark_page(hatena_id, option)

        if max_page > 10:
            # 最大200件まで取得するようにする
            max_page = 10

        titles = []

        for i in range(max_page):
            data = requests.get(
                'https://b.hatena.ne.jp/{}/bookmark.rss?{}page={}'.format(hatena_id, option, i+1))
            d = feedparser.parse(data.text)
            entries = d['entries']
            for entry in entries:
                titles.append(entry['title'])
        return titles

    # optionには追加のクエリパラメータを記述
    def get_url(self, hatena_id: str, option: str = '') -> list[str]:
        # 1ページに20件のデータがある。ページ数を求める
        if hatena_id == "":
            return []
        max_page = self.count_bookmark_page(hatena_id, option)

        if max_page > 10:
            # 最大200件まで取得するようにする
            max_page = 10

        links = []

        for i in range(max_page):
            data = requests.get(
                'https://b.hatena.ne.jp/{}/bookmark.rss?{}page={}'.format(hatena_id, option, i+1))
            d = feedparser.parse(data.text)
            entries = d['entries']
            for entry in entries:
                links.append(entry['link'])
        return links

    def count_osusume(self, hatena_id: str):
        self.osusumedic = {}
        w = word.find_word(hatena_id)
        if len(w) == 0:
            # 検索結果が0だったら何もしない
            return
        for entry in self.entries:
            if hatena_id == "":
                return ""
            noun = wd.get_noun(entry['title'])
            self.osusumedic.setdefault(entry['link'], 0)
            for n in noun:
                if n in w:
                    self.osusumedic[entry['link']] += w[n]

    def update_hotentry(self, category: str):
        d = feedparser.parse(
            'https://b.hatena.ne.jp/hotentry/{}.rss'.format(category))
        self.entries = d['entries']

    def get_hotentry(self, hatena_id: str, category: str) -> list[dict[str, str]]:
        entries = []
        osusume = "未計算"
        self.update_hotentry(category)
        for entry in self.entries:
            if entry['link'] in self.osusumedic:
                osusume = self.osusumedic[entry['link']]
            entries.append(
                dict(link=entry['link'], title=entry['title'], recommendation_score=osusume))
        return entries

    def get_user_entries(self, hatena_id: str, option: str = '') -> list[feedparser.util.FeedParserDict]:
        # 1ページに20件のデータがある。ページ数を求める
        if hatena_id == "":
            return []
        max_page = self.count_bookmark_page(hatena_id, option)

        if max_page > 10:
            # 最大200件まで取得するようにする
            max_page = 10
        entries = []
        for i in range(max_page):
            data = requests.get(
                'https://b.hatena.ne.jp/{}/bookmark.rss?{}page={}'.format(hatena_id, option, i+1))
            d = feedparser.parse(data.text)
            entries += d['entries']
        return entries

    def get_suggestions(self, hatena_id: str, option: str) -> list[dict[str, str]]:
        if hatena_id == "":
            return ""
        dic = {}
        data = []

        entries = self.get_user_entries(hatena_id, option)

        w = word.find_word(hatena_id)
        if len(w) == 0:
            # 検索結果が0だったら何もしない
            return [self.create_suggestion_model(link="", title="学習を行ってください", score=0)]
        for entry in entries:
            noun = wd.get_noun(entry['title'])
            dic.setdefault(entry['link'], 0)
            for n in noun:
                if n in w:
                    dic[entry['link']] += w[n]

            data.append(self.create_suggestion_model(link=entry['link'], title=entry['title'], score=dic[entry['link']]))
        return data

    def update_wordcloud(self, hatena_id: str) -> bytes:
        titles = self.get_title(hatena_id)
        output = io.BytesIO()
        wc.create_wordcloud(wd.get_noun(' '.join(titles))
                            ).save(output, format='PNG')
        wordcloud = b64encode(output.getvalue())
        user.update_wordcloud(hatena_id, wordcloud)
        return wordcloud

    def create_suggestion_model(self, link: str, title: str, score: str) -> learner_pb2.Suggestion():
        suggestion = learner_pb2.Suggestion()
        suggestion.link = link
        suggestion.title = title
        suggestion.score = score
        return suggestion
