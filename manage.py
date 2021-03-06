import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app.models.user_model import User
from app.models.category import Category
from app.models.Recipe import Recipe

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    db.create_all() 