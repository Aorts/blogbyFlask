from flask import (Blueprint , render_template)


# set module = sites
module = Blueprint("sites", __name__)


@module.route("/")
def index():
    return render_template(
        "sites/index.html")
