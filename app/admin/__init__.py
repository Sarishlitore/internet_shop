from app import db
from app.admin.admin import AdminBlueprint, AnyPageView, Controller

admin = AdminBlueprint('admin', __name__, template_folder='templates', static_folder='static')

from app.shop.models import Product, Brand, Category
from app.user.models import User

admin.add_view(Controller(User, db.session, name='Покупатели'))
admin.add_view(Controller(Product, db.session, name='Товары'))
admin.add_view(Controller(Brand, db.session, name='Брэнды'))
admin.add_view(Controller(Category, db.session, name='Категории'))
admin.add_view(AnyPageView(name='Что-то еще'))


@admin.route('/')
def index():
    return 'something'
