from flask_admin.contrib.sqla import ModelView
from wtforms.fields.numeric import FloatField
from flask_admin import BaseView, expose
from eapp import app, db
from flask_admin import Admin
from eapp.models import Category, Product

admin = Admin(app=app, name = "E - commerce'Admin")

class ProductView(ModelView):
    column_list = {'id', 'name', 'price', 'category_id'}
    column_searchable_list = ['name']
    can_export = True
    edit_modal = True
    column_editable_list = ['name']
    column_filters = ['name', 'price']
    form_overrides = {
        'price':FloatField
    }

class StastView(BaseView):
    @expose('/')
    def __index__(self):
        return self.render('admin/stats.html')

admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StastView(name='Thong ke'))