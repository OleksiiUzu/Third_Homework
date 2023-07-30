from flask import Flask


app = Flask(__name__)


@app.route('/')
def start_page():
    return "<p>Start Page</p>"


@app.route('/cart', methods=['GET', 'PUT'])
def cart():
    return


@app.route('/cart/order', methods=['POST'])
def cart_order():
    return


@app.route('/cart/add', methods=['POST', 'PUT'])
def cart_add():
    return


@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    return


@app.route('/user/register', methods=['POST'])
def user_register():
    return


@app.route('/user/sign_in', methods=['POST'])
def user_sign_in():
    return


@app.route('/user/logout', methods=['POST', 'GET'])
def user_logout():
    return


@app.route('/user/restore', methods=['POST'])
def user_restore():
    return


@app.route('/user/history', methods=['GET'])
def user_orders_history():
    return


@app.route('/user/history/<oder_id>', methods=['GET'])
def user_order(order_id: int):
    return


@app.route('/user/address', methods=['GET', 'POST'])
def user_address_list():
    return


@app.route('/user/address/<address_id>', methods=['GET', 'PUT', 'DELETE'])
def user_address(address_id: int):
    return


@app.route('/menu', methods=['GET'])
def menu():
    return


@app.route('/menu/<cat_name>', methods=['GET'])
def category(cat_name: str):
    return


@app.route('/menu/<cat_name>/<dish>', methods=['GET'])
def dishes():
    return


@app.route('/menu/<cat_name>/<dish_id>/review', methods=['POST'])
def dish(cat_name: str, dish_id: str):
    return


@app.route('/menu/search', methods=['GET', 'POST'])
def search():
    return


@app.route('/menu?order_by={ccal/price/rate/name}&dec=True', methods=['GET', 'POST'])
def dish_sort():
    return


@app.route('/menu/<cat_name>?order_by={ccal/price/rate/name}&dec=True', methods=['GET', 'POST'])
def category_sort():
    return


if __name__ == '__main__':
    app.run()
