a = input()
alf = 'ёуеыаоэяию'
gl = 0
sogl = 0
while 1:
    if len(a)!= 0:
        s = a[0]
        a = a[1::]
        l = alf.find(s)
        if (l == -1) and (s != " "): sogl += 1
        elif (l != -1) : gl += 1
    else:break
print(gl, sogl)
