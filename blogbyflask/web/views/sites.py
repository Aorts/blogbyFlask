from flask import (Blueprint , render_template)
from blogbyflask import models
from blogbyflask.web import forms


# set module = sites
module = Blueprint("sites", __name__)



@module.route("/")
def index():
    post = models.Post.objects().order_by("-id")

    return render_template(
        "sites/index.html",
        post=post
        )
