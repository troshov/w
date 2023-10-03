a = input()
otv = ''
while 1:
    if len(a) > 0:
        st = a[0]
        if st!= '.':
            otv += st
            a = a[1::]
        else:
            print(otv)
            a = a[1::]
            otv = ''
    else:
        print(otv)
        break
        
