from flask import Flask, session, redirect
from sqlalchemy import false

from config import Config
from routes.auth import auth
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from models import db
from routes.auth import auth

from routes.home import product_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:%s@localhost/db?charset=utf8mb4' %  quote('Admin@123')
# app.py hoặc config.py
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Abc.123456@database-to-ec2.czc0ueg02zl8.us-east-1.rds.amazonaws.com/webdb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'yabhcnjdkmasj145236afw'

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(product_bp)


if __name__ == '__main__':
    app.run(debug=True)

