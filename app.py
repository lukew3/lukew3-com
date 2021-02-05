from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, jsonify, Response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aslkfjhcaniewjnaefs'


@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template("home.html" )


if __name__ == "__main__":
    app.run()
