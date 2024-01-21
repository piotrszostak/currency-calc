from flask import Flask, request, render_template
from curr import fetch_rates

app = Flask(__name__)

@app.route('/')
def calc():
    rates = fetch_rates()
    return render_template("index.html", rates=rates)

@app.route('/result', methods=['POST'])
def result():
    result = request.form # -> MultiDict ([(currency, "USD"), (amount: 123)])
    rates = fetch_rates()

    currency = [currency_dict for currency_dict in rates if currency_dict['code'] == result["currency"]][0]
    ask = currency['ask']
    amount = int(result['amount'])
    value = round(ask * amount, ndigits=2)
    return render_template("result.html", value=value, ask=ask, amount=amount, currency=currency)
