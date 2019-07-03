from flask import Flask
app = Flask(__name__,
 static_folder = './public',
 template_folder="./static")
from templates.src.views import blueprint

# register blueprints (blueprints help make app modular)
app.register_blueprint(blueprint)