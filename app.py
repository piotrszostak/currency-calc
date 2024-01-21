from flask import Flask, request, render_template
from helpers import fetch_rates, fetch_rate_by_currency

app = Flask(__name__)

@app.route('/')
def calculate():
    rates = fetch_rates()
    return render_template("index.html", rates=rates)

@app.route('/result', methods=['POST'])
def show_result():
    request_form = request.form # -> MultiDict ([(currency, "USD"), (amount: 123)])
    currency = request_form['currency']
    ask = fetch_rate_by_currency(currency)
    amount = int(request_form['amount'])
    value = round(ask * amount, ndigits=2)
    return render_template("result.html", value=value, ask=ask, amount=amount, currency=currency)
