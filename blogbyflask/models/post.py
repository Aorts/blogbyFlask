from pkg_resources import require
import mongoengine as me
import datetime


class Post(me.Document):
    title = me.StringField(required=True , default="" , min_length=1, max_length=200)
    subtitle = me.StringField(default="", max_length=50)
    author = me.StringField(default="", max_length=30)
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now())
    picture = me.ImageField(thumbnail_size=(820, 460))
    content = me.StringField(max_length=300)