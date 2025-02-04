#task5 - program to check guess a number

import random as x 
while True:
 gnum = int(input("guess a number : ")) # taking user input 
 a = x.randint(1,10) # to take random integer  1 to 10
 if gnum < a:
  print("too low") 
 elif gnum > a:
  print("too high") 
 else:
  print("guessed right num") 
  break 
