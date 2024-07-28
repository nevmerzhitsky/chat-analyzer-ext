from flask import Blueprint, render_template

extension_bp = Blueprint('foo-extension', __name__, template_folder=f"./templates")


@extension_bp.route("/", methods=["GET"])
def example_page():
    return render_template("extension/index.html")
