from email.policy import default
from math import trunc
import re
import mongoengine as me
import datetime
from .. import models




class Post(me.Document):
    meta = {"collection": "Post"}
    title = me.StringField(required=True, min_length=1, max_length=200)
    subtitle = me.StringField(max_length=50)
    author = me.StringField(max_length=30)
    picture = me.ImageField(thumbnail_size=(820, 460))
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now())
    content = me.StringField()