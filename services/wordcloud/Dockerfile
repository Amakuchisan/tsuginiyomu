FROM python:3.9-slim

WORKDIR /work

# 環境変数にフォントのファイル名をセット
ENV FONTFILE NotoSansCJKjp-Regular.otf

COPY .fonts .fonts

COPY requirements.txt .

RUN pip install -U pip \
    && pip install -r requirements.txt

COPY . .

CMD ["python3", "/work/main.py"]
