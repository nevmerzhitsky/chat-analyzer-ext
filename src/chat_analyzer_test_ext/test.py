from flask import Blueprint, render_template

test_bp = Blueprint('test', __name__, template_folder=f"./templates")


@test_bp.route("/", methods=["GET"])
def test_page():
    return render_template("test/index.html")
