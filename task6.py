#task6 fibonacci sequence
a,b = 0,1 
for i in range(1,11): #to iterate upto  1 to 11
    print(a, end=" ") 
    a,b = b,a+b 