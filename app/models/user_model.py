from app import db
from werkzeug.security import  generate_password_hash


class User(db.Model):
    """Represent the user table"""
    __table__ = "users_data"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.string(100), nullable=False)
    last_name = db.Column(db.string(100), nullable=False)
    email = db.Column(db.string(50), unique=True, index=True)
    password = db.Column(db.string(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func_current_timestamp(), onupdate= db.func.current_timestamp())

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()




