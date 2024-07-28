from flask import Blueprint, Flask

from app_context.appmenu import ApplicationMenu
from .test import test_bp


def inject_blueprint(app: Flask) -> Blueprint:
    app.register_blueprint(test_bp, url_prefix="/test")

    return test_bp


def inject_menu(menu: ApplicationMenu):
    menu.add_section("test", "Test page", target_url="/test/")
