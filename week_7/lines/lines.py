import sys


try:
    file_name = sys.argv[1]

except:
    sys.exit("Too few command-line arguments")

else:
    if '.py' not in file_name:
        sys.exit("Not a python file")


finally:
    if len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")


try:
    line_len = 0
    with open(file_name , 'r')  as file_len:
        for line in file_len:
            stripped_line = line.lstrip()

            if not stripped_line.startswith("#") and stripped_line != "":
                line_len += 1
    print(line_len)



except:
    sys.exit("File does not exist")
