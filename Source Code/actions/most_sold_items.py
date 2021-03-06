from utils import (
    get_sales,
    get_products
)


def most_sold_items():
    print("--- San pham ban chay ---")
    print("Top 3 San pham ban chay nhat:")

    products = get_products()
    sales_file = get_sales()

    products_sold = {}

    for sold_items in sales_file:
        products_sold[sold_items["num_products"]] = 0
    for product in products:
        product_id = product["product_id"]
        products_sold[product_id] += product["num_products"]
        print(product)
