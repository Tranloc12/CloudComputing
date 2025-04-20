from flask import Blueprint, render_template, flash
from models import Product
from utils.auth_guard import login_required
from flask import redirect, url_for, session

products = [
    {"name": "iPhone 14 Pro", "category": "iphone", "description": "Điện thoại Apple", "price": 25000000, "image_filename": "iphone14pro.png"},
    {"name": "Galaxy S23", "category": "samsung", "description": "Điện thoại Samsung", "price": 22000000, "image_filename": "samsungs25.png"},
    {"name": "MacBook Air M2", "category": "macbook", "description": "Laptop Apple", "price": 30000000, "image_filename": "macbookpro.png"},
    {"name": "iphone 13", "category": "iphone", "description": "", "price": 1500000, "image_filename": "iphone13.png"},
    {"name": "iphone 15", "category": "iphone", "description": "", "price": 2500000, "image_filename": "iphone15.png"},

    # Thêm sản phẩm khác...
]
product_bp = Blueprint("product", __name__)

@product_bp.route("/", methods=["GET"])
def home():
    products = Product.query.all()
    return render_template("home.html", products=products)


@product_bp.route('/<category>')
def product_by_category(category):
    filtered = [p for p in products if p["category"] == category.lower()]
    return render_template('home.html', products=filtered)

@product_bp.route('/buy/<product_id>', methods=['GET', 'POST'])
def buy(product_id):
    if not session.get('user'):
        # Chuyển hướng người dùng đến trang đăng nhập nếu chưa đăng nhập
        return redirect(url_for('auth.login'))
    # Tiếp tục xử lý nếu người dùng đã đăng nhập
    # ...

