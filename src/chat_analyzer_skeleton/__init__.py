from flask import Blueprint, Flask

from app_context.appmenu import ApplicationMenu
from .skeleton import skeleton_bp


def inject_blueprint(app: Flask) -> Blueprint:
    app.register_blueprint(skeleton_bp, url_prefix="/skeleton")

    return skeleton_bp


def inject_menu(menu: ApplicationMenu):
    menu.add_section("skeleton", "Test page", target_url="/skeleton/")
