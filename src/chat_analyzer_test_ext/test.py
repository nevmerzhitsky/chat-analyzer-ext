from flask import Blueprint

test_bp = Blueprint('test', __name__)


@test_bp.route("/test-page", methods=["GET"])
def test_page():
    return "test works!"
