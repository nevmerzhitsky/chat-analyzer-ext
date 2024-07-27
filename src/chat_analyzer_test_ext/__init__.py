from flask import Flask

from test import test_bp


def inject_blueprint(app: Flask):
    print(f"{app=}")
    app.register_blueprint(test_bp, template="./templates")


def inject_menu():
    print(f"{inject_menu=}")
    pass
