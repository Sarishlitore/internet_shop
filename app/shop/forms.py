from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField


class ProductForm(FlaskForm):
    submit = SubmitField('Купить')


class SearchForm(FlaskForm):
    category = SelectField('Category', choices=[('1', 'All'), ('2', 'Computers')])
    value = StringField('')
