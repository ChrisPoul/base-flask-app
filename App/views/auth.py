from flask import (
    Blueprint, render_template, flash,
    redirect, url_for
)
from flask_login import login_user
from App.models.user import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    if True:
        user = User.get_by(name="Chris")
        login_user(user)

        flash('Logged in successfully.')

        return redirect(url_for("home.index"))
    return render_template('login.html', form=form)
