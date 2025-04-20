from flask import Blueprint, request, jsonify, session, redirect, url_for, flash, render_template
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth = Blueprint("auth", __name__)
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        full_name = request.form.get("full_name")

        if User.query.filter_by(email=email).first():
            flash("Email đã tồn tại.")
            return redirect(url_for("auth.register"))

        new_user = User(email=email, password=password, full_name=full_name)
        db.session.add(new_user)
        db.session.commit()

        flash("Đăng ký thành công.")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password_input = request.form.get('pswd')

        if not email or not password_input:
            flash("Vui lòng điền đầy đủ thông tin.")
            return redirect(url_for('auth.login'))

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password_input):
            login_user(user)  # Đăng nhập người dùng
            # Kiểm tra nếu người dùng là admin thì chuyển đến /admin, nếu không thì về trang chủ
            if user.is_admin:
                return redirect(url_for('admin.index'))
            session['user'] = user.email
            flash("Đăng nhập thành công.")
            return redirect(url_for('product.home'))
        else:
            flash("Email hoặc mật khẩu không đúng.")
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))
