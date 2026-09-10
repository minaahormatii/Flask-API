from flask import jsonify, request

from db import product_records


def create_product():
    post_data = request.form if request.form else request.json

    product = {}

    product['product_id'] = int(post_data['product_id'])
    product['name'] = post_data['name']
    product['description'] = post_data['description']
    product['price'] = float(post_data['price'])
    product['active'] = post_data['active']

    product_records.append(product)

    return jsonify({"message": "Product created successfully", "result": product}), 201


def read_product_by_id(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            return jsonify({"message": "product found", "result": product}), 200

    return jsonify({"message": "product not found"}), 404


def read_active_products():
    active_products = [
        product for product in product_records
        if product.get("active") is True
    ]

    if active_products:
        return jsonify({
            "message": "active products found",
            "results": active_products
        }), 200

    return jsonify({
        "message": "no active products found"
    }), 404


def get_all_products():
    return jsonify({"message": "products found", "results": product_records}), 200


def update_product_by_id(product_id):
    post_data = request.form if request.form else request.json

    product = {}

    product['product_id'] = int(product_id)

    if not product["product_id"]:
        return jsonify({"message": "product_id is required"}), 400

    for record in product_records:
        if record['product_id'] == product['product_id']:
            product = record
            product_records.remove(record)

    product['name'] = post_data.get('name', product['name'])
    product['description'] = post_data.get('description', product['description'])
    product['price'] = post_data.get('price', product['price'])

    product_records.append(product)

    return jsonify({"message": "product updated successfully", "result": product}), 200

def deactivate_product_by_id(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            product['active'] = False
            return jsonify({"message": "product deactivated successfully", "result": product}), 200

    return jsonify({"message": "product not found"}), 404

def delete_product_by_id(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            product_records.remove(product)
            return jsonify({"message": "product deleted successfully", "result": product}), 200
    return jsonify({"message": "product not found"}), 404

        
            


