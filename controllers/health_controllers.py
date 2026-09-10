from flask import jsonify

def get_health():
    return jsonify({"message": "flask is running", "status": "ok"}), 200