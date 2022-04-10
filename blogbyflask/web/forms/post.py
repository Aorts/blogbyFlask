from wtforms import fields, widgets
from flask_wtf import FlaskForm
from flask_mongoengine.wtf import model_form
from blogbyflask import models



class PostForm(FlaskForm):
    title = fields.StringField("ชื่อหัวข้อ")
    subtitle = fields.StringField("เรื่องย่อ")
    author = fields.StringField("ชื่อผู้เขียน")
    content = fields.StringField("content")
    upload_picture = fields.FileField("รูปภาพประกอบ")
    

