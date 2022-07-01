from flask import Blueprint, render_template

from app.shop.forms import SearchForm

shop = Blueprint('shop', __name__, template_folder='templates', static_folder='static')


@shop.route('/')
def index():
    srch_form = SearchForm()
    if srch_form.validate_on_submit():
        return 'There should be product searching'
    return render_template('shop/main.html', srch_form=srch_form)


@shop.route('/products')
def products():
    srch_form = SearchForm()
    if srch_form.validate_on_submit():
        return 'There should be product searching'
    return render_template('shop/products.html', srch_form=srch_form)


@shop.route('/about')
def about():
    srch_form = SearchForm()
    if srch_form.validate_on_submit():
        return 'There should be product searching'
    return render_template('shop/about.html', srch_form=srch_form)
