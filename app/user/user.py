from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import login_manager, shop_db
from app.user.forms import LoginForm, RegistrationForm
from app.user.user_login import UserLogin

user = Blueprint('user', __name__, template_folder='templates', static_folder='static')


@user.route('/')
def index():
    return 'user'


@login_manager.user_loader
def load_user(user_id):
    return UserLogin().from_db(user_id, shop_db)


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usr = shop_db.get_user_by_email(form.email.data)
        if usr and check_password_hash(usr.psw, form.psw.data):
            user_login = UserLogin().create(usr)
            login_user(user_login)
            return redirect(url_for('profile'))
    return render_template('user//login.html', form=form)


@user.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        hash_psw = generate_password_hash(form.psw.data)
        if shop_db.add_user(name=form.name.data, email=form.email.data, hash_psw=hash_psw):
            flash("Вы успешно зарегистрированы", "success")
            return redirect(url_for('index'))
        else:
            flash("Ошибка при добавлении в БД", "error")
    return render_template('user/registration.html', form=form)


@login_required
@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
