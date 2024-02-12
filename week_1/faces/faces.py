def converter(value):
    value = value.replace(":)","🙂")
    value = value.replace(":(","🙁")
    return value


def main():
    user_input = input("Enter the input ")
    output = converter(user_input)
    print(output)


main()
