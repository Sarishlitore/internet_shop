from flask import Blueprint, render_template, redirect, url_for, flash, session

from app.admin.forms import LoginForm

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


def login_admin():
    session['admin_logged'] = 1


def is_logged():
    return True if session.get('admin_logged') else False


def logout_admin():
    session.pop('admin_logged', None)


@admin.route('/')
def index():
    return redirect(url_for('.login', logged=is_logged()))


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.login.data == 'admin' and form.psw.data == '12345':
            login_admin()
            return redirect(url_for('.index'))
        else:
            flash('Неверная пара логин/пароль', 'error')
    return render_template('admin/login.html', form=form, logged=is_logged())


@admin.route('/logout')
def logout():
    if not is_logged():
        return redirect(url_for('.login'))
    logout_admin()
    return redirect(url_for('.login', logged=is_logged()))
