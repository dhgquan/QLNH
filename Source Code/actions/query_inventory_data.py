from utils import (
    get_products,
    select_by_id_or_name,
    safe_input
)


def query_inventory_data():

    print("---Thuc don---")
    print("Chon san pham?")

    list_products = get_products()

    for products in list_products:
        print(products['name'], products['id'])

    this_product = select_by_id_or_name(list_products, 'product')

    print("Mo ta:", this_product["description"])
    print("Ma san pham:", this_product["id"])
    print("Don gia:", this_product["price"])
    print("Ton kho:", this_product["quantity"])
    print("Tinh trang:", this_product["season"])
    print("Danh muc:", this_product["type"], "-", this_product["sub_type"])
