from flask import Flask
from flask import render_template,url_for
import os

app = Flask(__name__)

directories = [d for d in os.listdir('static') if os.path.isdir(os.path.join('static', d))]
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
    """
    iframe_links = {
        'pages': url_for('static', filename='pages/pages.html'),
        '2048': url_for('static', filename='2048/pages.html'),
        'soccer': url_for('static', filename='soccer/soccer.html'),
        'agario': url_for('static', filename='agario/agario.html'),
        '2048cupcakes': url_for('static', filename='2048/2048cupcakes.html'),
        'amigopancho3': url_for('static', filename='amigopancho3/amigopancho3.html'),
        'appleworm': url_for('static', filename='appleworm/appleworm.html'),
        'appleshooter': url_for('static', filename='appleshooter/appleshooter.html'),
        'adanceoffireandice': url_for('static', filename='adanceoffireandice/adanceoffireandice.html'),
        'ageofwar2': url_for('static', filename='ageofwar2/ageofwar2.html'),
        '99balls': url_for('static', filename='99balls/99balls.html'),
        'backrooms': url_for('static', filename='backrooms/backrooms.html'),
        'baldisbasics': url_for('static', filename='baldisbasics/baldisbasics.html'),
        'freerider': url_for('static', filename='freerider/freerider.html'),
    }
    """
    iframe_links = {}

    for directory_name in directories:
        iframe_links[directory_name] = url_for('static', filename=directory_name + '/' + directory_name + '.html')


    iframe_url = iframe_links.get(game_name)
    return render_template('gameweb.html', iframe_url=iframe_url,directories=directories)

