title = """
   _____                                _______   _            
  / ____|                              |__   __| | |           
 | |  __   _   _    ___   ___   ___       | |    | |__     ___ 
 | | |_ | | | | |  / _ \ / __| / __|      | |    | '_ \   / _ \\
 | |__| | | |_| | |  __/ \__ \ \__ \      | |    | | | | |  __/
  \_____|  \__,_|  \___| |___/ |___/      |_|    |_| |_|  \___|
          _   _                       _                     _  
         | \ | |                     | |                   | |  ™
         |  \| |  _   _   _ __ ___   | |__     ___   _ __  | | 
         | . ` | | | | | | '_ ` _ \  | '_ \   / _ \ | '__| | | 
         | |\  | | |_| | | | | | | | | |_) | |  __/ | |    |_| 
         |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|    (_)  

Guess The Number! is © 1993 Packerland Programmers. All rights reserved.

"""


print(title)
print("""

How To Play: I choose a four digit number (0 to 9999), and you 
guess it in 10 tries or less to win.  Each try is for a single digit! 
The first digit is digit 0...

""")

import numpy as np
import sys

x = np.random.randint(0,10000)
s = '{:4}'.format(x).replace(' ', '0')
x = list(map(int, list(s)))
found = [0, 0, 0, 0]

max_guesses = 10

if len(sys.argv) > 1 and sys.argv[1] == "godmode":
    print("\nGOD MODE: the answer is {}\n".format(s))

count = 0
while True:

    print("\nYou have {} guesses left.\n".format(max_guesses - count))


    count += 1
    display = ''
    for i in range(4):
        if found[i]:
            display += str(x[i])
        else:
            display += 'X'
    print("You currently have: ", display)


    loc = int(input("Which digit to guess? "))
    if found[loc]:
        print("\nYou already got that one!\n")
        continue

    val = int(input("Which value do you guess? "))
    if val == x[loc]:
        found[loc] = 1
        print("\nYou chose, wisely!\n")
    else:
        print("\nYou chose, poorly!\n")


    if sum(found) == 4:
        print("You win!")
        break

    if count >= max_guesses:
        print("You lose!")
        break 


     
