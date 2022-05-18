from utils import (
    get_products,
    select_by_id_or_name,
    safe_input,
    update_products
)


def register_product_arrival():
    print("--- Dang nhap thu kho ---\n")
    print("Chon san pham")

    menu = get_products()

    for thing in menu:
        print(thing['name'], thing['id'])

    chooosen_product = select_by_id_or_name(menu, 'product')

    arrival_quantity = safe_input('int_positive', 'Recent arrival quantity:')

    chooosen_product['quantity'] += arrival_quantity

    print('Thanh cong. Ban da them %s %s ' %
          (arrival_quantity, chooosen_product['name']))
    print('Ton kho %s' % chooosen_product['quantity'])
    update_products(menu)
