from flask_script import Manager  # class for handling set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app

app = create_app("development")
migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
