from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, jsonify, Response
import requests, uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aslkfjhcaniewjnaefs'


@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template("home.html" )

@app.route('/recolorbot/upload', methods=['POST'])
def recolorBotUpload():
    url = request.args['url']
    r = requests.get(url)
    
    filename = str(uuid.uuid4()) + ".jpg"
    with open(f'recolorbot/photos/{filename}', 'wb') as f:
        f.write(r.content)

    return jsonify(url=f"https://lukew3.com/recolorbot/photos/{filename}")

@app.route('/recolorbot/photos/<filename>', methods=['GET'])
def recolorDisplayImage(filename):
    return send_from_directory('./recolorbot/photos', filename)    

if __name__ == "__main__":
    app.run()
