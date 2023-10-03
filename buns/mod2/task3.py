abc = input()
ind1 = abc.find(" ")
a = int(abc[:ind1])
ind2 = abc.find(" ", ind1+1)
b = int(abc[ind1+1:ind2])
c = int(abc[ind2+1:])
if (a > b):
    if (c > a): print(a)
    elif (c > b): print(c)
    else:print(b)
elif(c > b):print(b)
else:
    if (a > c):print(a)
    else:print(c)
