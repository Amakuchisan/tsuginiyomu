import MeCab
import os
from wordcloud import WordCloud

#ワードクラウドの作成
def create_wordcloud(text: str):
    if len(text) == 0:
        text = "あなたの ワードクラウドを 作成しよう"
        word_chain = text
    else:
        word_chain = ' '.join(text)

    fontpath = '/work/.fonts/' + os.environ['FONTFILE']

    wordcloud = WordCloud(background_color=None,
                          mode="RGBA",
                          font_path=fontpath,
                          width=900,
                          height=500,
                          relative_scaling=0.5 # フォントサイズの相対的な単語頻度の重要性
                         ).generate(word_chain)

    #ファイルの作成
    img = wordcloud.to_image()
    # img.save("/work/images/image-" + os.environ['HATENAID'] + ".png", optimize=True)
    return img
