from utils import (
    safe_input,
    get_products,
    get_employees,
    get_sales
)

from actions import (
    register_sale,
    register_product_arrival,
    query_inventory_data,
    employees_with_most_sales,
    most_sold_items
)


def main():
    print("SALES AND INVENTORY SYSTEM")
    print("""
Select an action

1. Dang nhap ban hang
2. Dang nhap thu kho
3. Xem thuc don
4. Nhan vien ban nhieu nhat
""")

    while True:
        
        action = safe_input('int_positive', 'Action: ')

        if action > 0 and action < 6:
            break

        print("Vui long nhap tu 1 den 4")

    
    if action == 1:
        register_sale()
    elif action == 2:
        register_product_arrival()
    elif action == 3:
        query_inventory_data()
    elif action == 4:
        employees_with_most_sales()
    print("Cam on da su dung he thong\n")


while True:
    main()

    again = input("Ban co muon thu lai ? (y/n) ").strip()[0].lower()

    if (again == 'y'):
        continue
    else:
        print("Hen gap lai -w-\n")
        break
