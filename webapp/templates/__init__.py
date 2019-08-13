from flask import Flask,session
app = Flask(__name__,
 static_folder = './public',
 template_folder="./static")
from templates.src.views import blueprint

# register blueprints (blueprints help make app modular)
#for some reason the route wont register
@app.route('/reset')
def reset():
     session["currQuery"] = ""
     return {"status":200}
app.register_blueprint(blueprint)