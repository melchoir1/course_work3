from flask import Flask, render_template, request
from utils import load_posts, load_posts_user_id, search_for_posts, search_for_name, load_comments
from api.api import api_bp

app = Flask(__name__)

app.register_blueprint(api_bp)

"""выводим все посты"""
@app.route("/")
def main_screen():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route("/post/<int:pk>/")
def view_posts(pk):
    """отбражение конкретного поста"""
    post = load_posts_user_id(pk)
    comments = load_comments(pk)
    return render_template('post.html', post=post, comments=comments)

@app.route("/search/", methods=["POST"])
def search_post():
    """поиск по словам"""
    posts = search_for_posts(request.form.get("word"))
    return render_template('search.html', posts=posts)

@app.route("/user/<user_name>/")
def view_posts_user(user_name):
    """отбражение конкретного имени и какие посты он написал"""
    posts = search_for_name(user_name)
    return render_template('user-feed.html', posts=posts)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

