from flask import jsonify


def respond_string():
    return "Here is a response with a python string!"

def respond_html():
    return "<h1 align='center' style='color: orange;'>Here is a response with HTML!</h1>"

def respond_json():
    return jsonify({"message": "Here is a response with JSON!"})

def respond_addition(num1, num2):
    def addition(num1, num2):
        count = int(num1) + int(num2)
        return count
    sum = addition(num1, num2)
    return jsonify({"message": f"Here is a response with addition {sum}"})

