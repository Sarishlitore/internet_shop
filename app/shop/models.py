from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.Integer, db.ForeignKey('department.id'))
    price = db.Column(db.Integer, numllable=False)
    count = db.Column(db.Integer, nullable=False)
    info = db.relationship('Info', backref='product', uselist=False)

    def __repr__(self):
        return f'<Product {self.id}>'


class Info(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Category {self.id}>'
