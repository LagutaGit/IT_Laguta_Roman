from flask import Flask, render_template, url_for
#from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/modules')
def modules():
    return render_template("modules.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/polezno')
def polezno():
    return render_template("polezno.html")


@app.route('/users/<string:name>/<int:id>')
def user(name, id):
    return "users: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)