import json
from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current = datetime.date.today()
    return render_template('index.html', year=current.year)

@app.route('/blog')
def blog():
    with open(file='static/package.json', mode="r") as file:
        all_posts = json.load(file)
        current = datetime.date.today()
        return render_template('blog.html', posts=all_posts, year=current.year)

@app.route('/post/<id>')
def post(id):
    with open(file='static/package.json', mode="r") as file:
        all_posts = json.load(file)
        for p in all_posts:
            if p["id"] == id:
                post_x = p
        current = datetime.date.today()
        return render_template('post.html', post=post_x, year=current.year)


if __name__ == "__main__":
    app.run(debug=True)

