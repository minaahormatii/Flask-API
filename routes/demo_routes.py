from flask import Blueprint

import controllers

demo = Blueprint('demo', __name__)

@demo.route('/string', methods=['GET'])
def respond_string():
    return controllers.respond_string()

@demo.route('/html', methods=['GET'])
def respond_html():
    return controllers.respond_html()

@demo.route('/json', methods=['GET'])
def respond_json():
    return controllers.respond_json()

@demo.route("/addition/<num1>/<num2>", methods=['GET'])
def respond_addition(num1, num2):
    return controllers.respond_addition(num1, num2)