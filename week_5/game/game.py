import random

while True:
    try:
        user_input = int(input("Level: "))
        num = random.randint(1,user_input)
        guss_num = int(input("Guess: "))
        if guss_num == num :
                print("Just right!")
                break
        elif guss_num > num :
                print("Too large!")
        elif  guss_num < num:
                print("Too small!")

    except:
        pass



