
from flask import Blueprint, render_template, request, flash

# it has urls  so we set blueprint

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        data=request.form.get('email')
        print(f'data is here: {data}')
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return '<p>logout up</p>'



@auth.route('/sign-up',methods=['GET', 'POST'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        if len(email) < 4:
            flash('email must be greater than 4 character', category='error')
        elif len(password1) != len(password2):
            flash('password not match!', category='error')

        elif len(password1) < 7:
            flash('password must be greater than 7 character', category='error')
        else:
            flash('Account Created', category='success')


    return render_template('sign-up.html')
