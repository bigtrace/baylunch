
from flask import request,render_template,Blueprint
from app.models import Order


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page',1,type=int)
    orders = Order.query.order_by(Order.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template('home.html',orders=orders)

@main.route("/about")
def about():
    return render_template('about.html', title='About')
