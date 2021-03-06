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

# return server_error, html
def get_body_from_URL(url: str) -> tuple[bool, str]:
    client_err_code = [400, 403, 404]
    server_err_code = [500, 502, 503]
    headers = {
        'User-Agent': 'tsuginiyomu (github.com/Amakuchisan)'
    }
    if not allow_robots_txt(url):
        print(url, "not allowed to access")
        return False, ''
    try:
        res = requests.get(url, headers=headers, verify=False)
        if res.status_code in client_err_code:
            return False, ''
        if res.status_code in server_err_code:
            return True, ''
    except Exception as e:
        print(url, e)
        return True, ''
    soup = BeautifulSoup(res.content, 'html.parser')
    if soup.find('article') is None:
        html = soup.get_text()
    else:
        html = '\n'.join([c.get_text() for c in soup.find_all('article')])
    return False, strip_symbol(strip_tags(strip_url(neologdn.normalize(html))))

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
