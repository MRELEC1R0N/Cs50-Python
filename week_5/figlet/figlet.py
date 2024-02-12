import sys
import random
from pyfiglet import Figlet


figlet = Figlet()
font_list = random.choice(figlet.getFonts())
sys_args = sys.argv[1:4]

if sys_args:
    if sys_args[0] in ['-f' , '-font']:
                figlet.setFont(font = sys_args[1])



    else:
            sys.exit("Invalid usage")



else:
    figlet.setFont(font = font_list)































user_input = input("Input: ")
print(figlet.renderText(user_input))
