from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, jsonify, Response
import requests, uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aslkfjhcaniewjnaefs'


@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template("home.html" )

@app.route('/recolorbot/photos/<filename>', methods=['GET'])
def recolorDisplayImage(filename):
    return send_from_directory('./recolorbot/photos', filename)    

@app.route('/recolorbot', methods=['GET'])
def recolorBotReroute():
    return redirect("https://www.reddit.com/user/recolorbot")

if __name__ == "__main__":
    app.run()
