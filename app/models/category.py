from app import db
from .user_model import User


class Category(db.Model):
    """This table represent category recipe"""

    __tablenmame__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    category_name = db.Column(db.String(255))

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    date_modified = db.Column( db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))

    recipes = db.relationship('Recipe', order_by='Recipe.recipe_id', cascade="all, delete-orphan")

    def __init__(self, category_name, user_id, recipes=None, category_id=None, ):
        """initialize category table"""
        self.category_id = category_id
        self.category_name = category_name
        self.recipes = recipes

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Category: {}>".format(self.category_name)