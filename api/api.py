from flask import Blueprint, jsonify

from logger import get_logger
from utils import load_posts, load_posts_user_id

api_bp = Blueprint("api", __name__, url_prefix='/api/')

logger = get_logger(__name__)

@api_bp.route("posts/")
def api_posts():
    posts = load_posts()
    logger.info('api_posts')
    return jsonify(posts)


@api_bp.route("post/<int:pk>/")
def api_post(pk):
    post = load_posts_user_id(pk)
    logger.info('api_post')
    return jsonify(post)

