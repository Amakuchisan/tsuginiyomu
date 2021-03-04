from base64 import b64encode
import io
import os
from wordcloud import WordCloud
from manager import user, word

# ワードクラウドの更新
def update_wordcloud(hatena_id: str) -> bytes:
    frequencies = {}
    if hatena_id != "":
        frequencies = word.find_word(hatena_id)

    output = io.BytesIO()
    create_wordcloud(frequencies).save(output, format='PNG')
    wordcloud_image = b64encode(output.getvalue())
    user.update_wordcloud(hatena_id, wordcloud_image)

    return wordcloud_image

# ワードクラウドの作成
def create_wordcloud(frequencies: dict[str, int]) : #  -> PIL.Image.Image
    if len(frequencies) == 0:
        frequencies = {"データが": 1, "学習されている": 2, "ありません": 1}

    fontpath = '/work/.fonts/' + os.environ['FONTFILE']

    wordcloud = WordCloud(background_color=None,
                          mode="RGBA",
                          font_path=fontpath,
                          width=900,
                          height=500,
                          relative_scaling=0.5 # フォントサイズの相対的な単語頻度の重要性
                         ).fit_words(frequencies)

    #ファイルの作成
    img = wordcloud.to_image()
    return img
