from flask import Flask, request, render_template
from curr import fetch_rates

app = Flask(__name__)

@app.route('/')
def calc():
    rates = fetch_rates()
    return render_template("index.html", rates=rates)
