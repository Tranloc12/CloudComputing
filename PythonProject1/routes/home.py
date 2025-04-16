from flask import Blueprint, render_template
from models import Product
from utils.auth_guard import login_required

product_bp = Blueprint("product", __name__)

@product_bp.route("/", methods=["GET"])
def home():
    products = Product.query.all()
    return render_template("home.html", products=products)



