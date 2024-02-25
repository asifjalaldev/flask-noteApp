
from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

# it has urls  so we set blueprint

views = Blueprint('views',__name__)
# register this view in __init__
@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)


