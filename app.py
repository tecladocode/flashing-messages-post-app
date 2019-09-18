"""
This app is only partially complete. At the moment there is no message flashing.

Want to find out how we'd complete it?

Check out our blog post: <>
"""
import functools
from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = "jose"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")
