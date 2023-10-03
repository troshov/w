a = input()
ko1 = 0
ko0 = 0
while 1:
    if len(a)>0:
        s = a[0]
        a = a[1::]
        if s == '1': ko1 += 1
        elif s == '0': ko0 += 1
    else:break
if(ko1 == ko0):print('yes')
else:print('no')
