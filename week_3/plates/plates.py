def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")





def is_valid(s):
  """
  Checks if a given string is a valid vanity plate based on the specified rules.

  Args:
      plate: The string to validate.

  Returns:
      True if the plate is valid, False otherwise.
  """

  # Check minimum and maximum length
  if len(s) < 2 or len(s) > 6:
    return False

  # Ensure at least two letters at the beginning
  if not s[:2].isalpha():
    return False

  # 0 is not in the bignning
  i = 0
  while i < len(s):
    if s[i].isalpha() == False:
        if s[i] == '0':
           return False
        else :
           break

    i += 1


  for i in range(2, len(s) - 1):
          if s[i].isdigit() and s[i + 1].isalpha():
              return False






  # No periods, spaces, or punctuation
  for char in s:
    if not char.isalnum():
      return False

  return True







main()
