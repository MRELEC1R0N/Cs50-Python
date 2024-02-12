user_input = input("Enter the values : ")

value = user_input.split(" ")

value_1 = float(value[0])
value_2 = float(value[2])


if(value[1] == "+"):
    print(value_1 + value_2)

elif(value[1] == "-"):
    print(value_1 - value_2)

elif(value[1] == "*"):
    print(value_1 * value_2)

elif(value[1] == "/"):
    print(value_1 / value_2)

else:
    print("Wrong arguments were passed")
