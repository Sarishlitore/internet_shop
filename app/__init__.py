import os

from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY'] = 'zmdqCUp0ZZO_yuzWgKhx8Q'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"

from app.shopdb.shop_db import ShopDB

shop_db = ShopDB(db.session)

from app.user.user import user

app.register_blueprint(user, url_prefix='/user', name='customer')

from app.shop.shop import shop

app.register_blueprint(shop, url_prefix='/shop')

from app.admin import admin

app.register_blueprint(admin, name='admin_page', url_prefix='/admin')

db.create_all()


@app.route('/')
def index():
    return redirect(url_for('shop.index'))
