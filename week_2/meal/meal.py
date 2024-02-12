def main():
    user_input = input("What time is it? ")
    output = convert(user_input)
    if(7<= output <= 8):
        print("breakfast time")
    elif(12 <=output <= 13):
        print("lunch time")
    elif(18 <= output <= 19):
        print("dinner time")
    else:
        pass

def convert(time):
    values = time.split(":")
    value_1 = float(values[0])
    value_2 = float(values[1])/60

    return (value_1+value_2)


if __name__ == "__main__":
    main()
