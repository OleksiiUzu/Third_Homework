from flask import Flask
from view import *

"""
Тут я намагався обробити лише GET запити
У деяких ендпоінтів є темплейти
З ендпоінтами сортування і пошуку поки проблемки
"""

app = Flask(__name__)

app.add_url_rule('/', view_func=start_page)  # ok
app.add_url_rule('/about', view_func=about)  # ok

app.add_url_rule('/cart', view_func=cart)  # ok
app.add_url_rule('/cart/order', view_func=cart_order)  # [POST]
app.add_url_rule('/cart/add', view_func=cart_add)  # [POST]

app.add_url_rule('/user', view_func=user)  # ok
app.add_url_rule('/user/register', view_func=user_register)  # [POST]
app.add_url_rule('/user/sign_in', view_func=user_sign_in)  # [POST]
app.add_url_rule('/user/logout', view_func=user_logout)  # [POST]
app.add_url_rule('/user/restore', view_func=user_restore)  # [POST]
app.add_url_rule('/user/history', view_func=user_orders_history)  # ok
app.add_url_rule('/user/history/<order_id>', view_func=user_order)  # ok
app.add_url_rule('/user/addresses', view_func=user_address_list)  # ok
app.add_url_rule('/user/addresses/<address_id>', view_func=user_address)  # ok

app.add_url_rule('/menu', view_func=menu)  # ok
app.add_url_rule('/menu/categories', view_func=categories)  # ok
app.add_url_rule('/menu/categories/<cat_id>', view_func=category_dishes)  # ok
app.add_url_rule('/menu/categories/<cat_id>/<dish_id>', view_func=dish)  # ok
app.add_url_rule('/menu/categories/<cat_id>?order_by=ccal/price/rate/name', view_func=category_sort)  # not ok
app.add_url_rule('/menu/all_dishes', view_func=dishes)  # ok


app.add_url_rule('/menu/search', view_func=search)  # not ok
app.add_url_rule('/menu/all_dishes?order_by_var=ccal/price/rate/dish_name&order=ASC/DESC', view_func=dish_sort)  # not ok

app.add_url_rule('/admin/dishes', view_func=admin_dishes)   # ok
app.add_url_rule('/admin/dishes/<dish_id>', view_func=admin_dish)  # ok
app.add_url_rule('/admin/orders', view_func=admin_orders)  # ok
app.add_url_rule('/admin/orders/<order_id>', view_func=admin_order)  # ok
app.add_url_rule('/admin/orders?status={new/in_progress}', view_func=admin_sort_order_status)  # not ok
app.add_url_rule('/admin/orders/<id>/status', view_func=admin_set_order_status)  # not ok
app.add_url_rule('/admin/categories', view_func=admin_show_categories)  # ok
app.add_url_rule('/admin/categories/<cat_id>', view_func=admin_category_edit)  # [POST]
app.add_url_rule('/admin/search', view_func=admin_search)  # not ok

if __name__ == '__main__':
    app.run(debug=True)
