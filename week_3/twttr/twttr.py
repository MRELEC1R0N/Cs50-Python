user_input = input("Input : ")
output = ""


for c in user_input:
      if c.lower() in ['a','e','i','o','u']:
            pass
      else:
            output += c

print(f"Output : {output}")
