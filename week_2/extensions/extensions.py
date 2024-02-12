user_input = input("File : ").lower().strip()
ext_list = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']


dot_index = user_input.rfind(".")

ext_value = user_input[dot_index: ] if dot_index != -1 else " "

if ext_value in (".gif",".png"):
    print(f"image/{ext_value[1:]}")

elif ext_value in (".jpeg",".jpg"):
    print("image/jpeg")
elif ext_value == ".txt":
    print(f"text/{user_input[:-4]}")

elif ext_value in (".pdf",".zip"):
    print(f"application/{ext_value[1:]}")


else:
    print("application/octet-stream")


# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
