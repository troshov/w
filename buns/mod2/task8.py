ab = input()
ind = ab.find(",")
a = ab[:ind]
b = ab[ind+1:]
otv = 0
while 1:
    s = a[0]
    if s != b:
        otv += 1
        a = a[1::]
    else:
        otv += 1
        print(otv)
        break
