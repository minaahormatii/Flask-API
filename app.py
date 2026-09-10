import os
from flask import Flask, jsonify

import routes

flask_host = os.environ.get('FLASK_HOST')
flask_port = os.environ.get('FLASK_PORT')

app = Flask(__name__)
app.register_blueprint(routes.health)
app.register_blueprint(routes.products)
app.register_blueprint(routes.demo)


if __name__ == '__main__':
    app.run(host=flask_host, port=flask_port)