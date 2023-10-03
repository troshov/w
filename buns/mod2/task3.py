a = int(input())
b = int(input())
c = int(input())
if (a > b):
    if (c > a): print(a)
    elif (c > b): print(c)
    else:print(b)
elif(c > b):print(b)
else:
    if (a > c):print(a)
    else:print(c)
