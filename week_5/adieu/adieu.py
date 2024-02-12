import inflect
p = inflect.engine()

names = []


while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)
        continue
    except EOFError:
        print()
        break


new_names = p.join(names)
print(f"Adieu, adieu, to {new_names}")

