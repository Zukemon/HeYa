from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    abort,
    session,
    jsonify,
    Blueprint,
)
from HeYa import *
# import os
from werkzeug.utils import secure_filename
from moviepy.editor import *
# import animation
# import time


# configure app
app = Flask(__name__)

# Ensure temps are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
@app.route('/')
def home():
    return render_template("home.html", hi= "Hey there! Wanna make your own HeYa video greeting card that you can send to friends and family? It's easy. Come say..")


@app.route('/heya', methods=["GET", "POST"])
def heya_x():

    if request.method == 'POST':
        # queue()
       
        return main()

    else:

        return render_template("heya.html", snape="Create your own 'HeYa!' message now!")


@app.route('/loader', methods=["GET", "POST"])
def loader():
    if request.method == 'POST':
        main()
        flash("Well done!")
        return redirect(url_for("heya.home"))
    else:
        return render_template("loader.html", scan= "rendering out message")
    
        
        



        
        