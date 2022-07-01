from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    login = StringField('Логин: ', validators=[InputRequired()])
    psw = PasswordField('Пароль: ', validators=[InputRequired()])
    submit = SubmitField('Войти')


class DepartmentForm(FlaskForm):
    name = StringField('Категория:')
    submit = SubmitField('Добавить:')


class BrandForm(FlaskForm):
    name = StringField('Категория:')
    submit = SubmitField('Добавить:')
