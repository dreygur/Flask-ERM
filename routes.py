from flask import Blueprint
from flask import jsonify, request
from flask import render_template
from flask_login import current_user
from flask_login import login_required

routes = Blueprint("routes", __name__)

@login_required
def root():
    return render_template("index.html")

@login_required
def form():
    return render_template("pages/forms/form-elements.html")

def api():
    if request.method == "POST":
        data = request.form
        print(data)
        return jsonify({"name": "Totul"})
    return "Hi"

@routes.context_processor
def context_processor():
    photo = "../static/images/profile/male/image_1.png"
    if current_user.name:
        photo = f"../static/images/profile/male/{current_user.email}.png"
    return dict(photo=photo)
