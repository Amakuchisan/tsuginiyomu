from flask import Flask, render_template, request, redirect, url_for

from util.bookmark import Bookmark
from util import wc, word

from learner import learner
from manager import manager

app = Flask(__name__, template_folder='/work/templates')

image = None
bookmark = Bookmark()
hatena_id = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global image
    if request.method == 'GET':
        entries = sorted(bookmark.get_hotentry(hatena_id, "it"),
                         key=lambda x: x['recommendation_score'], reverse=True)
        return render_template("index.html", hatena_id=hatena_id, entries=entries, image=image)

    elif request.method == 'POST':
        wordcloud = learner.create_wordcloud(hatena_id)
        image = wordcloud.decode("utf-8")

        return redirect(url_for('index'))


@app.route('/id', methods=['POST'])
def id():
    if request.method == 'POST':
        global hatena_id
        global image
        hatena_id = request.form["user_id"]
        u = manager.create_user(hatena_id)
        img = u.wordcloud
        if not img:
            image = None
        else:
            image = img.decode("utf-8")
    return redirect(url_for('index'))


@app.route('/learn', methods=['POST'])
def learn():
    if request.method == 'POST':
        learner.learn(hatena_id)
    return redirect(url_for('index'))


# @app.route('/recommended', methods=['POST'])
# def recommended():
#     if request.method == 'POST':
#         bookmark.count_osusume(hatena_id)
#     return redirect(url_for('index'))


# @app.route('/atodeyomu', methods=['GET'])
# def atodeyomu():
#     if request.method == 'GET':
#         entries = bookmark.get_suggestion(hatena_id, "tag=あとで読む&")
#         if not entries[0]['score'] == "データがありません":
#             entries = sorted(entries,
#                             key=lambda x: x['score'], reverse=True)
#         return render_template("atodeyomu.html", hatena_id=hatena_id, atodeyomu_entries=entries)


if __name__ == "__main__":
    app.run(debug=True)
