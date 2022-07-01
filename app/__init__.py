from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY'] = 'zmdqCUp0ZZO_yuzWgKhx8Q'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"

from app.shopdb.shop_db import ShopDB

shop_db = ShopDB(db.session)

from app.user.user import user

app.register_blueprint(user, url_prefix='/user')

from app.shop.shop import shop

app.register_blueprint(shop, url_prefix='/shop')

from app.admin.admin import admin

app.register_blueprint(admin, url_prefix='/admin')
