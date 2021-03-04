from base64 import b64encode
import feedparser
import io
import math
import re
import requests
import sys

from manager import user
from word import word
from generator import wordcloud

class Bookmark:
    # 公開しているブックマークの数を求める
    def __init__(self):
        self.osusumedic = {}
        self.entries = {}

    def count_bookmark_page(self, hatena_id: str, option: str = '') -> int:
        data = requests.get(
            'https://b.hatena.ne.jp/{}/bookmark.rss?{}'.format(hatena_id, option))
        d = feedparser.parse(data.text)
        content = d['feed'].get('subtitle')  # 'Userのはてなブックマーク (num)'
        if content is None:
            raise Exception('Error: User does not exists')
        match = re.search(r"(はてなブックマーク \()(.*?)\)", content)
        num = match.group(2).replace(',', '')  # 公開しているブックマーク数
        if not num.isdecimal():
            raise Exception('Error: bookmark num is string')
        return math.ceil(int(num)/20)

    # optionには追加のクエリパラメータを記述
    def get_title(self, hatena_id: str, option: str = '') -> list[str]:
        # 1ページに20件のデータがある。ページ数を求める
        if hatena_id == "":
            return []
        try:
            max_page = self.count_bookmark_page(hatena_id, option)
        except Exception as err:
            print(err, file=sys.stderr)
            max_page = 0

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

    def update_wordcloud(self, hatena_id: str) -> bytes:
        titles = self.get_title(hatena_id)
        output = io.BytesIO()
        wordcloud.create_wordcloud(word.get_noun(' '.join(titles))
                            ).save(output, format='PNG')
        wordcloud_image = b64encode(output.getvalue())
        user.update_wordcloud(hatena_id, wordcloud_image)
        return wordcloud_image
