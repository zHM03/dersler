from models import Order, OrderItem

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 201
product_bp = Blueprint('product', __name__)

@order_bp.route('/orders')
if 'user_id' not in session:
    return redirect(url_for('login'))
orders = Order.query.filter_by(user_id=session['user_id']).all()
return render_template('orders.html', orders=orders)