a = input()
otv = ''
while 1:
    if len(a) != 0:
        s = a[0]
        a = a[1::]
        if s != "-" and s != ")" and s !="(" and s !=" ":
            otv += s
    else:break
print(otv)
