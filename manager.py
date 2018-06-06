
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import DevelopmentConfig, ProductionConfig
from info import create_app, db

app = create_app(DevelopmentConfig)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():

    return ''


if __name__ == '__main__':
    manager.run()
