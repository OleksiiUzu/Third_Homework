from flask import render_template, request
from db_methods import get_db_data


def start_page():
    """
    :return: Main Page.
    """
    return render_template('index.html')


def about():
    return render_template('about.html')


def cart():
    """
    Shows all dishes in cart.
    :return: data of all dishes in cart.
    """
    if request.method == 'GET':
        result = get_db_data('SELECT * FROM Orders')
        return render_template('cart.html', result=result)


def cart_order():
    """
    :return: order_data for paying.
    """
    if request.method == 'POST':
        pass


def cart_add():
    """
    Adding dish to cart.
    POST / PUT methods
    :return:  dish_data (I guess).
    """
    return


def user():
    """
    Different actions with user.
    methods=['GET', 'POST', 'PUT', 'DELETE']
    :return: user_data.
    """
    if request.method == 'GET':
        result = get_db_data("SELECT * FROM User")
        return render_template('user.html', result=result)


def user_register():
    """
    methods = [POST]
    :return:
    """
    return '<p> user register </p>'


def user_sign_in():
    """
    methods = [POST]
    :return:
    """
    return '<p> user sign_in </p>'


def user_logout():
    """
    methods=['POST', 'GET']
    :return:
    """
    return '<p> user logout </p>'


def user_restore():
    """
    methods=['POST']
    :return:
    """
    return '<p> user restore </p>'


def user_orders_history():
    """
    methods=['GET']
    :return:
    """
    return get_db_data('SELECT * FROM Orders')


def user_order(order_id: int):
    """
    Shows user order
    methods=['GET']
    :return:
    """
    return get_db_data(f"SELECT * FROM Orders WHERE ID={order_id}")


def user_address_list():
    """
    methods=['GET', 'POST']
    :return:
    """
    if request.method == 'GET':
        user_data = get_db_data("SELECT ID FROM USER")
        # user_data[1][0] or user_data[2][0]
        address_result = get_db_data(f"SELECT * FROM Address WHERE User={user_data[0][0]}")
        return address_result


def user_address(address_id: int):
    """
    methods=['GET', 'PUT', 'DELETE']
    :return:
    """
    if request.method == 'GET':
        user_data = get_db_data("SELECT ID FROM USER")
        # user_data[1][0] or user_data[2][0]
        address_result = get_db_data(f"SELECT * FROM Address WHERE User={user_data[0][0]} and ID={address_id}")
        return address_result


def menu():
    if request.method == 'GET':
        result = get_db_data("SELECT * FROM Dishes")
        return render_template('menu.html', result=result)


def categories():
    """
    methods=['GET']
    :return:
    """
    if request.method == "GET":
        result = get_db_data("SELECT * FROM Category")
        return render_template('categories.html', result=result)


def category_dishes(cat_id):
    """
    methods=['GET']
    :return:
    """
    if request.method == "GET":
        result = get_db_data(f"SELECT * FROM Dishes WHERE Category = {cat_id}")
        return render_template('category_dishes.html', result=result)


def category_sort(cat_id, order_by):
    """
    methods=['GET']
    :return:
    """
    if request.method == "GET":
        result = get_db_data(f"SELECT * FROM Dishes ORDERED BY {order_by} ASC")
        return render_template('category_dishes.html', result=result)


def dishes():
    """
    methods=['GET']
    :return:
    """
    if request.method == 'GET':
        result = get_db_data("SELECT * FROM Dishes")
        return render_template('all_dishes.html', result=result)


def dish(cat_id: int, dish_id: int):
    """
    methods=['GET', 'POST']
    :return:
    """
    if request.method == 'GET':
        result = get_db_data(f"SELECT * FROM Dishes WHERE ID = {dish_id}")
        return render_template('dish.html', result=result)


def search():
    """
    methods=['GET', 'POST']
    :return:
    """
    return


def dish_sort(order_by_var, order):
    """
    methods=['GET', 'POST']
    :return:
    """
    if request.method == 'GET':
        result = get_db_data("SELECT * FROM Dishes ORDER BY {0} {1}".format(order_by_var, order))
        return result


def admin_dishes():
    """
    methods=['GET']
    :return:
    """
    if request.method == 'GET':
        return get_db_data("SELECT * FROM Dishes")


def admin_dish(dish_id: int):
    """
    methods=['GET', 'PUT', 'DELETE']
    :return:
    """
    if request.method == 'GET':
        return get_db_data(f"SELECT * FROM Dishes WHERE ID = {dish_id}")


def admin_orders():
    """
    methods=['GET']
    :return:
    """
    if request.method == 'GET':
        return get_db_data("SELECT * FROM Orders")


def admin_order(order_id: int):
    """
    methods=['GET']
    :return:
    """
    if request.method == 'GET':
        return get_db_data(f"SELECT * FROM Orders WHERE ID = {order_id}")


def admin_sort_order_status():
    """
    methods=['GET']
    :return:
    """
    return


def admin_set_order_status():
    """
    methods=['POST']
    :return:
    """
    return


def admin_show_categories():
    """
    methods=['GET']
    :return:
    """
    if request.method == 'GET':
        return get_db_data('SELECT name FROM Category')


def admin_category_edit():
    """
    methods=['POST', 'DELETE']
    :return:
    """
    return


def admin_search():
    """
    methods=['GET']
    :return:
    """
    return
