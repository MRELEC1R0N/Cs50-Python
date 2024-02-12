user_input = input("Enter the Camel case : ")
output = ""



for c in user_input:
    if 'A' <= c <= 'Z':
        output += ("_"+ c.lower())
    else :
        output += c




print(output)
