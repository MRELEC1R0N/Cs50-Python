food_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def order(prompt):
    total = 0
    while True:
        try:
            item = input(prompt)
            if item.title() in food_items:
                total += float(food_items[item.title()])
                print("${:.2f}".format(total))
                continue
            else:
                print(item.title())
                pass


        except EOFError:
            print()
            return total



output = order("Item: ")

