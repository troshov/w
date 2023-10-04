a = input()
otv = ''
while 1:
    if len(a) > 0:
        st = a[len(a) - 1]
        if st!= '.':
            otv += st
            a = a[:-1]            
        else:
            print(otv[::-1])
            a = a[:-1]
            otv = ''
    else:
        print(otv[::-1])
        break
        
