user_input = input("What is the answer to the Great Question of Life, the Universe and Everything ? ").lower().strip()

if(user_input in ("42", "forty-two" , "forty two" ) ):
    print("Yes",end ="")
else:
    print("No",end="")
