a = input()
if not a.isdigit():
    print("Неверный ввод")
else:
    a = int(a)
    a8 = a
    a16 = a
    a2 = a
    str2 = ''
    while a2 > 0:
        str2 += str(a2 % 2)
        a2 //= 2


    str8 = ''
    while a8 > 0:
        str8 += str(a8 % 8)
        a8 //= 8


    str16 = ''
    while a16 > 0:
        i = a16 % 16
        if (i == 10):str16 += 'A'
        elif (i == 11):str16 += 'B'
        elif (i == 12):str16 += 'C'
        elif (i == 13):str16 += 'D'
        elif (i == 14):str16 += 'E'
        elif (i == 15):str16 += 'F'
        else:str16 += str(i)
        a16 //= 16

    print(str2[::-1], str8[::-1], str16[::-1])
