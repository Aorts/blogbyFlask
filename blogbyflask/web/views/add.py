from flask import (Blueprint , render_template)
from datetime import datetime
from blogbyflask import models


module = Blueprint("add", __name__)


@module.route("/add", methods=["GET", "POST"])
def add():
    return render_template(
        "post/addPost.html")

