import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
# Replace your_user_name with the user name you configured for the database
# Replace your_password with the password you specified for the database user
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}?driver=SQL+Server+Native+Client+11.0".format(DB_USER="test", DB_PASS="123qwe", DB_ADDR="serv-sql", DB_NAME="flask_notifications")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') 