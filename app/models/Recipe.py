from app import db
from app.models.category import Category
from app.models.user_model import User


class Recipe(db.Model):
    """This class represent Recipe Table"""

    __tablename__ = 'Recipe'

    recipe_id = db.Column(db.Integer(), primary_key=True, authoincrement=True)

    recipe_name = db.Column(db.String(256))

    ingredients = db.Column(db.String(256))

    directions = db.Column(db.String(256))

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))

    category_id = db.Column(db.Integer, db.ForeignKey(Category.category_id))

    def __init__(self, recipe_id, recipe_name, user_id, category_id, directions=None, ingredients=None):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.user_id = user_id
        self.category_id = category_id
        self.directions = directions
        self.ingredients = ingredients
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Recipe.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Recipe: {}>".format(self.name)



