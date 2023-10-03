a = input()
otv = ''
sim = ''
while 1:
    if len(a) != 0:
        s = a[0]
        if s!=" ":
            sim = s
            a = a[1::]
        else:
            otv += sim
            a = a[1::]
    else:
        otv += sim
        break
print(otv)
