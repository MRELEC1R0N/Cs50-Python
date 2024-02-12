def main():
    grocery_list = make_list()
    item = sorted(grocery_list)
    for i in item:
        print(f"{grocery_list[i]} {i.upper()}")




def make_list():
    grocery_list = {}

    while True:
        try:
            item = input()
            key_value = grocery_list.get(item)
            if key_value != None:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1


        except EOFError:
            print()
            return grocery_list






main()
