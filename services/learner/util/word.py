from bs4 import BeautifulSoup
import emoji
import MeCab
import neologdn
import regex
import requests
from time import sleep

from my_urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
from stop_words import stop_words as stop

# 名詞を取得
def get_noun(text: str) -> list[str]:
    stop_words = stop.get()
    # 形態素解析
    tagger = MeCab.Tagger(
        '-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'
    )
    tagger.parse('')
    node = tagger.parseToNode(text)
    word_list = []
    while node:
        word_type = node.feature.split(',')[0]
        word_surf = node.surface.split(',')[0]
        if word_type == '名詞' and word_surf not in stop_words:
            if len(set(["副詞可能", "数", "非自立", "代名詞", "接尾"]) & set(node.feature.split(",")[1:4])) == 0:
                word_list.append(node.surface)
        node = node.next
    words = remove_emoji(word_list)
    return list(map(lambda s: s.lower(), words))

def strip_tags(html: str) -> str:
    html = html.replace("&lt;", '<').replace("&gt;", '>')
    p = r"(?<rec><(?:[^<>]+|(?&rec))*>)"
    return regex.sub(p, '', html)

def remove_emoji(word_list: list[str]) -> list[str]:
    return list(filter(lambda x: x not in emoji.UNICODE_EMOJI['en'], word_list))

def strip_url(html: str) -> str:
    p = r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)"
    return regex.sub(p, '', html)


def strip_symbol(html: str) -> str:
    p = r"[!-/:-@[-`{-~ʹ·]"
    return regex.sub(p, ' ', html)


def get_body_from_URL(url: str) -> str:
    err_code = [500, 502, 503]
    if not allow_robots_txt(url):
        print(url, "not allowed to access")
        return ""
    try:
        res = get_retry(url, 3, err_code)
        if res.status_code in err_code:
            return ''
    except Exception as e:
        print(url, e)
        return ''
    soup = BeautifulSoup(res.content, 'html.parser')
    if soup.find('article') is None:
        html = soup.get_text()
    else:
        html = '\n'.join([c.get_text() for c in soup.find_all('article')])
    return strip_symbol(strip_tags(strip_url(neologdn.normalize(html))))


def allow_robots_txt(url: str) -> bool:
    rp = RobotFileParser()
    try:
        rp.set_url("{0.scheme}://{0.netloc}/robots.txt".format(urlparse(url)))
        rp.read()
        if rp.can_fetch("*", url):
            return True
    except Exception as e:
        print(url, e)
    return False


def get_retry(url, retry_times, errs):
    headers = {
        'User-Agent': 'tsuginiyomu (github.com/Amakuchisan)'
    }
    for t in range(retry_times + 1):
        r = requests.get(url, headers=headers, verify=False)
        if t < retry_times:
            if r.status_code in errs:
                sleep(2)
                continue
        return r

def get_title_by_url(url: str) -> str:
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")
    except Exception as e:
        print(url, e)
        return ""
    #タイトル取得
    return soup.title.string
