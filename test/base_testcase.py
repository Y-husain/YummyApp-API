import os
import json
import unittest
from faker import Faker
from app.models.user_model import User
from app import create_app, db


class BaseTestCase(unittest.TestCase):
    """Base test class"""

    def setUp(self):
        """defines test variable and initialize app"""
        self.app = create_app('testing')
        self.fake = Faker()
        self.client = self.app.test_client()
        self.user ={'first_name': self.fake.first_name(), 'last_name': self.fake.last_name(),
                    'email': self.fake.email(), 'password':self.fake.password()}

        # binds the app to the current context
        with self.app.app_context():

            # create all tables
            db.create_all()
            user = User(first_name='test_FirstName', last_name='test_LastName',
                        email='test_email', password='test_password')
            db.session.add(user)
            db.session.commit()

    if __name__ == '__main__':
        unittest.main()










