
from flask import Blueprint, render_template

# it has urls  so we set blueprint

views = Blueprint('views',__name__)
# register this view in __init__

@views.route('/')
def home():
    return render_template('home.html', text='some text from view')


