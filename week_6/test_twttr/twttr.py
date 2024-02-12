
def main():
      user_input = input("Input : ")
      output = shorten(user_input)
      print(f"Output : {output}")




def shorten(word):
      output = ""
      for c in word:
            if c.casefold()  in ['a','e','i','o','u']:
                  pass
            else:
                  output += c

      return output

if __name__ == "__main__":
      main()
