FROM python:3.9-slim

WORKDIR /work

# mecabとmecab-ipadic-NEologdの導入
RUN apt-get update \
    && apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file sudo gcc g++

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && bin/install-mecab-ipadic-neologd -n -y \
    && ln -s /etc/mecabrc /usr/local/etc/mecabrc

COPY userdic userdic

# ユーザ辞書の追加
RUN /usr/lib/mecab/mecab-dict-index \
    -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd \
    -u /work/userdic/myDic.dic \
    -f utf-8 -t utf-8 /work/userdic/myDic.csv \
    && echo userdic = /work/userdic/myDic.dic >> /usr/local/etc/mecabrc

COPY requirements.txt .

RUN pip install -U pip \
    && pip install -r requirements.txt

COPY . .

RUN sed -i -e 's/CipherString = DEFAULT@SECLEVEL=2/# CipherString = DEFAULT@SECLEVEL=2/g' /etc/ssl/openssl.cnf

CMD ["python3", "/work/main.py"]
