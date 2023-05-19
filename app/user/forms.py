from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, EqualTo, InputRequired


class LoginForm(FlaskForm):
    username = StringField('Логин: ', validators=[InputRequired()])
    password = PasswordField('Пароль: ', validators=[InputRequired()])
    remember = BooleanField('Запомнить', default=False)
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Логин: ', validators=[InputRequired(message='Введите логин'),
                                                  Length(min=6, max=31,
                                                         message="Логин должно быть от 4 до 31 символов")])
    password = PasswordField('Пароль: ', validators=[InputRequired(message='Введите пароль'),
                                                     Length(min=7, max=127,
                                                            message="Пароль должен содержать минимум 6 символов")])
    password2 = PasswordField('Повтор пароля: ', validators=[InputRequired(message='Повторите пароль'),
                                                             EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Регистрация')
