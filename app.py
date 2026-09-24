from flask import Flask, jsonify, request, render_template
from data import products as products_data


app = Flask(__name__)


@app.route('/')
def hello_worl():
    return 'Hello !'


@app.route('/products')
def show_products():
    ids = []

    for product in products_data:
        ids.append(product['id'])

    id = request.args.get('id')

    if id is None:
        return render_template('products.html', products=products_data)

    id = int(id)

    if id in ids and id > 0:
        products = []

        for product in products_data:
            if product['id'] == id:
                products.append(product)

        return render_template('products.html', products=products)

    return render_template('products.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True)