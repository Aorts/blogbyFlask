from flask import (Blueprint , render_template, request, Response, send_file, redirect, url_for)
from datetime import datetime
from blogbyflask import models
from blogbyflask.web import forms


module = Blueprint("accounts", __name__, url_prefix="/accounts")

@module.route("/")
def index():
    post = models.Post.objects()
    return render_template(
        "sites/index.html",
        post=post
        )
        
@module.route("/add", methods=["GET","POST"])
def add():
    form = forms.PostForm()
    if not form.validate_on_submit():
        return render_template(
            "post/addPost.html",
                            form=form,
        )
    
    post = models.Post()
    if form.upload_picture.data:
        data = form.upload_picture.data
        post.picture.put(data, filename=data.filename, content_type=data.content_type)
    post.title = form.title.data 
    post.subtitle = form.subtitle.data 
    post.author = form.author.data 
    post.content = form.content.data 
    post.created_date = datetime.now()
    post.save()

    return redirect(
        url_for(
            "sites.index",
        )
    )



@module.route("/<post_id>/edit", methods=["GET","POST"])
def edit(post_id):
    post = models.Post.objects.get(id=post_id)
    form = forms.PostForm(obj=post)


    if not form.validate_on_submit():
        return render_template(
            "post/addPost.html",
            post=post,
                            form=form,
        )
    if form.upload_picture:
        data = form.upload_picture.data
        form.upload_picture.replace(
            data, filename=data.filename, content_type=data.content_type
        )
    else:
        post.upload_picture.put(
            data, filename=data.filename, content_type=data.content_type
        )
    form.populate_obj(post)
    post.save()
    return redirect(
        url_for(
            "sites.index",
        )
    )

@module.route("/get_image/<post_id>/<filename>/<get_type>", methods=["GET", "POST"])
def get_image(post_id, filename, get_type):
    post = models.Post.objects.get(id=post_id)
    img = None
    if post.picture.filename == filename:
        if get_type == "thumbnail":
            img = post.picture.thumbnail
        else:
            img = post.picture
    response = Response()
    if img:
        mimetype = "image/jpg"
        if hasattr(img, "content_type") and img.content_type:
            mimetype = img.content_type
        elif hasattr(img, "filename") and img.filename:
            mimetype = "image/{}".format(img.filename[: img.filename.rfind(".")])
        mimetype = mimetype.lower()
        response = send_file(img, mimetype=mimetype)
    else:
        response.status_code = 404
    return response


@module.route("/<post_id>/delete", methods=["GET", "POST"])
def delete(post_id):
    post = models.Post.objects.get(id=post_id)
    post.delete()

    return redirect(
        url_for(
            "sites.index",
        )
    )

@module.route("/<post_id>/read", methods=["GET", "POST"])
def read(post_id):
    post = models.Post.objects.get(id=post_id)
    return render_template(
        "sites/readnow.html",
        post=post
        )

