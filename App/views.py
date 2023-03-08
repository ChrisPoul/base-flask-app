from flask import Blueprint, render_template
from .models.message import Message

bp = Blueprint('home', __name__)


@bp.route('/')
def index():

    return render_template(
        "index.html"
    )
