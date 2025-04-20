from flask import Flask
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

from admin.admin import admin_bp
from models import User  # Import model User bạn đã định nghĩa
from config import Config
from models import db
from routes.auth import auth
from routes.home import product_bp


app = Flask(__name__)


# ✅ Dùng cấu hình SQLAlchemy kết nối RDS:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:%s@user-system-db.czc0ueg02zl8.us-east-1.rds.amazonaws.com/db?charset=utf8mb4' % quote('Abc.123456')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'yabhcnjdkmasj145236afw'





# Khởi tạo db
db.init_app(app)

# Đăng ký blueprint
app.register_blueprint(auth)
app.register_blueprint(product_bp)
login_manager = LoginManager(app)
app.register_blueprint(admin_bp)

login_manager.login_view = 'auth.login'  # Đường dẫn đến trang login nếu người dùng chưa đăng nhập

# Định nghĩa user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Route kiểm tra kết nối RDS
@app.route('/test-db')
def test_db():
    try:
        with app.app_context():
            result = db.session.execute("SELECT NOW();").fetchone()
        return f"Kết nối thành công! Thời gian RDS: {result[0]}"
    except Exception as e:
        return f"Lỗi kết nối: {str(e)}"




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
