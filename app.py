from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, jsonify, Response
import requests, uuid
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aslkfjhcaniewjnaefs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/luke/journal.db'


@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template("home.html" )

@app.route('/contact', methods=['GET'])
def contact():
   return render_template("contact.html" )

@app.route('/projectList', methods=['GET', 'POST'])
def project_list():
   return render_template("project_list.html")

@app.route('/recolorbot/photos/<filename>', methods=['GET'])
def recolorDisplayImage(filename):
    return send_from_directory('./recolorbot/photos', filename)

@app.route('/recolorbot', methods=['GET'])
def recolorBotReroute():
    return redirect("https://www.reddit.com/user/recolorbot")

db = SQLAlchemy(app)
class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    # Time should always be in 24 hour format eastern time
    time = db.Column(db.Integer)

    def __repr__(self):
        return f'Entry {self.month}/{self.day}/{self.year} {self.time} - {self.text}'

@app.route('/jrnl', methods=['GET', 'POST'])
def add_journal_entry():
    if request.method == 'POST':
        text = request.form.get('entry')
        if text == "":
            return render_template("journal.html")
        now = datetime.now(pytz.timezone('America/New_York'))
        new_entry = JournalEntry(text=text,
                year=now.strftime("%Y"),
                month=now.strftime("%m"),
                day=now.strftime("%d"),
                time=now.strftime("%H:%M:%S"))
        db.session.add(new_entry)
        db.session.commit()
    return render_template("journal.html")

@app.route('/mathgenerator', methods=['GET'])
def mathgenerator():
    return render_template("mathgenerator.html")

if __name__ == "__main__":
    app.run()
