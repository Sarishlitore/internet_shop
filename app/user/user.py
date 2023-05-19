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
    log_form = LoginForm()
    if log_form.validate_on_submit():
        usr = shop_db.get_user_by_username(log_form.username.data)
        if usr and check_password_hash(usr.password, log_form.password.data):
            user_login = UserLogin().create(usr)
            login_user(user_login)
            return redirect(url_for('.profile'))
    return render_template('user/login.html', log_form=log_form)


@user.route('/registration', methods=['GET', 'POST'])
def registration():
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        hash_psw = generate_password_hash(reg_form.password.data)
        if shop_db.add_user(username=reg_form.username.data, password=hash_psw):
            flash("Вы успешно зарегистрированы", "success")
            return redirect(url_for('.profile'))
        else:
            flash("Ошибка при добавлении в БД", "error")
    return render_template('user/registration.html', reg_form=reg_form)


@user.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('user/profile.html')


@login_required
@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
