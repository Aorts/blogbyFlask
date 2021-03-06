from flask_mongoengine import MongoEngine
from .users import User
from .Post import Post
__all__ = [
    "User",
    "Post"
    ]

db = MongoEngine()


def init_db(app):
    db.init_app(app)
