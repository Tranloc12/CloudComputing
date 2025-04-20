from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from flask import request, redirect, url_for
from models import db


from models import User, Product

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
@login_required
def index():
    return render_template('admin/index.html')

@admin_bp.route('/users')
@login_required
def manage_users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)


@admin_bp.route('/products')
@login_required
def manage_products():
    products = Product.query.all()
    return render_template('admin/products.html', products=products)


@admin_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if not current_user.is_admin:
        abort(403)

    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        db.session.commit()

        return redirect(url_for('admin.manage_users'))

    return render_template('admin/edit_user.html', user=user)


@admin_bp.route('/users/<int:user_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        abort(403)  # Kiểm tra quyền admin

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('admin.manage_users'))



@admin_bp.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if not current_user.is_admin:
        abort(403)

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        new_product = Product(name=name, price=price)

        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('admin.manage_products'))  # Chuyển đến trang quản lý sản phẩm

    return render_template('admin/add_product.html')


@admin_bp.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    if not current_user.is_admin:
        abort(403)

    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu

        return redirect(url_for('admin.manage_products'))

    return render_template('admin/edit_product.html', product=product)


@admin_bp.route('/delete_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        abort(403)

    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('admin.manage_products'))
