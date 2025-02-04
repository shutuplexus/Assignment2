#task3 - program to check no betn 10 to 20 

a = int(input("enter num : ")) # taking input from user 

if not (a < 10 or a > 20 ): # condition to check number exits betn 10 and 20
    if a % 2 == 0: # condition to check number is odd or even 
        print("given number exists betn 10  and its even ") 
    else:
        print("given number exists betn 10 and 20 and its odd") 
else:
    print("given number doesn't exists betn 10 and 20")