from base64 import b64encode
from flask import Flask, render_template, request, redirect, url_for
import io
from PIL import Image

from util.bookmark import Bookmark
from util import wc, word

from domain import user

app = Flask(__name__, template_folder='/work/templates')

output = io.BytesIO()
wc.create_wordcloud('').save(output, format='PNG')
sample_image = b64encode(output.getvalue()).decode("utf-8")
image = sample_image

bookmark = Bookmark()
hatena_id = ""


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        entries = sorted(bookmark.get_hotentry(hatena_id, "it"),
                         key=lambda x: x['recommendation_score'], reverse=True)
        return render_template("index.html", hatena_id=hatena_id, entries=entries, image=image)

    elif request.method == 'POST':
        update_wordcloud()
        return redirect(url_for('index'))


@app.route('/id', methods=['POST'])
def id():
    if request.method == 'POST':
        global hatena_id
        global image
        hatena_id = request.form["user_id"]
        u = user.create(hatena_id)
        img = u.wordCloud
        if not img:
            image = sample_image
        else:
            image = img.decode("utf-8")
        bookmark.count_osusume(hatena_id)
    return redirect(url_for('index'))


@app.route('/learn', methods=['POST'])
def learn():
    if request.method == 'POST':
        bookmark.init(hatena_id)
    return redirect(url_for('index'))


@app.route('/recommended', methods=['POST'])
def recommended():
    if request.method == 'POST':
        bookmark.count_osusume(hatena_id)
    return redirect(url_for('index'))


@app.route('/atodeyomu', methods=['GET'])
def atodeyomu():
    if request.method == 'GET':
        entries = bookmark.get_suggestion(hatena_id, "tag=あとで読む&")
        if not entries[0]['score'] == "データがありません":
            entries = sorted(entries,
                            key=lambda x: x['score'], reverse=True)
        return render_template("atodeyomu.html", hatena_id=hatena_id, atodeyomu_entries=entries)


def update_wordcloud():
    global image
    global output
    titles = bookmark.get_title(hatena_id)
    output = io.BytesIO()
    wc.create_wordcloud(word.get_noun(' '.join(titles))
                        ).save(output, format='PNG')
    image = b64encode(output.getvalue()).decode("utf-8")
    user.update_wordcloud(hatena_id, b64encode(output.getvalue()))


if __name__ == "__main__":
    app.run(debug=True)
