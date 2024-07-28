from flask import Blueprint, render_template

skeleton_bp = Blueprint('skeleton', __name__, template_folder=f"./templates")


@skeleton_bp.route("/", methods=["GET"])
def test_page():
    return render_template("skeleton/index.html")
