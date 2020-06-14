from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = "kj3h46kjh3k6h54354hk43"

    from . import urlshort

    app.register_blueprint(urlshort.bp)

    return app
