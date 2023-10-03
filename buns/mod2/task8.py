a = input()
b = input()
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
