from flask import Flask, render_template, request, redirect, session, url_for
import os

from learner import learner
from manager import manager

app = Flask(__name__, template_folder='/work/templates')

app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        hatena_id = ""
        entries = []
        image = None
        if 'hatena_id' in session:
            hatena_id = session['hatena_id']
            u = manager.create_user(session['hatena_id'])
            if u.wordcloud:
                image = u.wordcloud.decode('utf-8')
            entries = sorted(learner.get_suggestion(hatena_id),
                        key=lambda x: x.score, reverse=True)
        return render_template("index.html", hatena_id=hatena_id, entries=entries, image=image)

@app.route('/id', methods=['POST'])
def id():
    if request.method == 'POST':
        id = request.form["user_id"]
        if learner.exists_hatena_id(id):
            session['hatena_id'] = id
            u = manager.create_user(id)
    return redirect(url_for('index'))

@app.route('/wordcloud', methods=['POST'])
def wordcloud():
    if request.method == 'POST':
        if 'hatena_id' in session:
            wordcloud = learner.create_wordcloud(session['hatena_id'])
    return redirect(url_for('index'))

@app.route('/learn', methods=['POST'])
def learn():
    if request.method == 'POST':
        learner.learn(session['hatena_id'])
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
