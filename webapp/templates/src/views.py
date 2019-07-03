from flask import render_template, Blueprint
blueprint = Blueprint('src',__name__)
@blueprint.route('/')
def index():
 return render_template("index.html")
