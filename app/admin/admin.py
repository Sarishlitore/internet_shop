from flask import Blueprint
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from app.user.models import User


class AdminBlueprint(Blueprint):
    views = None

    def __init__(self, *args, **kwargs):
        self.views = []
        super(AdminBlueprint, self).__init__('admin', __name__, template_folder='templates', static_folder='static')

    def add_view(self, view):
        self.views.append(view)

    def register(self, app, options):
        admin_page = Admin(app, name='Магазин', template_mode='bootstrap3', index_view=DashBoardView(),
                           endpoint='admin')

        for view in self.views:
            admin_page.add_view(view)
        return super(AdminBlueprint, self).register(app, options)


class DashBoardView(AdminIndexView):
    @expose('/')
    def add_data_db(self):
        all_users = User.query.all()
        return self.render('admin/dashboard_index.html', all_users=all_users)

    def is_accessible(self):
        return current_user.get_id() == '1'


class Controller(ModelView):
    def is_accessible(self):
        return current_user.get_id() == '1'


class AnyPageView(BaseView):
    @expose('/')
    def any_page(self):
        return self.render('admin/any_page/index.html')

    def is_accessible(self):
        return current_user.get_id() == '1'
