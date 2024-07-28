from flask import Blueprint, Flask

from app_context.appmenu import ApplicationMenu
from .extension import extension_bp


def inject_blueprint(app: Flask) -> Blueprint:
    app.register_blueprint(extension_bp, url_prefix="/extension")

    return extension_bp


def inject_menu(menu: ApplicationMenu):
    menu.add_section("extension", "Extension test page", target_url="/extension/")
