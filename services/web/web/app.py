from flask import Flask, render_template, request, redirect, url_for

from learner import learner
from manager import manager

app = Flask(__name__, template_folder='/work/templates')

hatena_id = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    image = None
    entries = []
    if request.method == 'GET':
        if hatena_id:
            u = manager.create_user(hatena_id)
            if u.wordcloud:
                image = u.wordcloud.decode("utf-8")
            entries = sorted(learner.get_suggestion(hatena_id),
                        key=lambda x: x.score, reverse=True)
    return render_template("index.html", hatena_id=hatena_id, entries=entries, image=image)

@app.route('/id', methods=['POST'])
def id():
    if request.method == 'POST':
        global hatena_id
        hatena_id = request.form["user_id"]
        u = manager.create_user(hatena_id)
    return redirect(url_for('index'))

@app.route('/wordcloud', methods=['POST'])
def wordcloud():
    if request.method == 'POST':
        if hatena_id:
            wordcloud = learner.create_wordcloud(hatena_id)
    return redirect(url_for('index'))

@app.route('/learn', methods=['POST'])
def learn():
    if request.method == 'POST':
        learner.learn(hatena_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
