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
    response = requests.get(url='https://api.npoint.io/13462902ff4869770bda')
    all_posts = response.json()
    current = datetime.date.today()
    return render_template('blog.html', posts=all_posts, year=current.year)

@app.route('/post/<id>')
def post(id):
    response = requests.get(url='https://api.npoint.io/13462902ff4869770bda')
    all_posts = response.json()
    for p in all_posts:
        if p["id"] == id:
            post_x = p
    current = datetime.date.today()
    return render_template('post.html', post=post_x, year=current.year)


if __name__ == "__main__":
    app.run(debug=True)

