
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import DevelopmentConfig, ProductionConfig
from info import create_app, db, set_logs

app = create_app(DevelopmentConfig)
set_logs(app)
# 添加拓展命令行
manager = Manager(app)
# 数据库迁移命令
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
