def main():
    user_input = input("Greetings : ").lower().strip()
    output = value(user_input)
    print(output)




def value(greeting):
    greeting = greeting.lower()
    if("hello" in greeting):
        return 0
    elif(greeting != "hello" and greeting[0]== "h" ):
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()
