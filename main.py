from flask import Flask
from flask import render_template,url_for
import os

app = Flask(__name__)

directories = [d for d in os.listdir('static') if os.path.isdir(os.path.join('static', d))]
iframe_links = {}


@app.route("/")
def main():
    return render_template('mainweb.html', directories=directories)
@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/game/<game_name>')
def gameweb(game_name):


    for directory_name in directories:
        iframe_links[directory_name] = url_for('static', filename=directory_name + '/' + directory_name + '.html')

    iframe_url = iframe_links.get(game_name)

    return render_template('gameweb.html', iframe_url=iframe_url,directories=directories)

@app.route("/game/<game_name>/fullscreen")
def fullscreen(game_name):
    iframe_url=iframe_links.get(game_name)
    return render_template("fullscreen.html",iframe_url=iframe_url)