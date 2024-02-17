def show_menu(menu):
    print("Меню кав'ярні:")
    for item, price in menu.items():
        print(f"{item}: {price} грн")
def add_to_menu(menu):
    item = input("Введіть назву нового товару: ")
    price = float(input("Введіть ціну за один товар: "))
    menu[item.lower()] = price
    print(f"{item} додано в меню з ціною {price} грн")
def take_order(menu):
    order = {}
    while True:
        item = input("Введіть назву товару (або 'кінець', щоб закінчити замовлення): ").lower()
        if item == 'кінець':
            break
        if item not in menu:
            add_new = input(f"{item} немає у меню. Хочете додати його? (так/ні): ")
            if add_new.lower() == 'так':
                add_to_menu(menu)
            else:
                continue
        quantity = int(input(f"Введіть кількість {item}: "))
        order[item] = order.get(item, 0) + quantity
    return order
def calculate_total(order, menu):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total
def print_receipt(order, menu, total):
    print("\nЗамовлення:")
    for item, quantity in order.items():
        print(f"{item}: {quantity} x {menu[item]} грн = {quantity * menu[item]} грн")
    print(f"Загальна вартість: {total} грн")
def main():
    menu = {
        'американо': 35,
        'латте': 30,
        'макіято': 28,
        'еспресо': 24
    }
    while True:
        show_menu(menu)
        order = take_order(menu)
        total = calculate_total(order, menu)
        print_receipt(order, menu, total)
        another_order = input("Хочете прийняти ще одне замовлення? (так/ні): ")
        if another_order.lower() != 'так':
            break
if __name__ == "__main__":
    main()
