a = input()
chet = 0
nechet = 0
lor = True
while 1:
    if len(a)!= 0:
        s = a[0]
        a = a[1::]
        if lor:
            nechet += int(s)
            lor = False
        else:
            chet += int(s)
            lor = True
    else:break
if (3 * chet + nechet) %10 == 0:print('yes')
else:print('no')
