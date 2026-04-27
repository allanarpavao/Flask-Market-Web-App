from run import app
from flask import render_template

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Tanzanite', 'barcode': 893212299897, 'price':500},
        {'id': 2, 'name': 'Ametist', 'barcode': 123985473165, 'price': 900},
        {'id': 3, 'name': 'Periodot', 'barcode': 231985128446, 'price': 150}
    ]
    return render_template('market.html', items=items)