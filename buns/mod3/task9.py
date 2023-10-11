with open('данные.txt', 'r') as file:
    a = file.readline()
    
a = int(a)
x, y = 0, 0

while a > 0:
    if x == y and x >= 0:
        while x != -y - 1 and a > 0:
            a -= 1
            x -= 1

    if x == -y -1:
        while x != y and x < 0 and a > 0:
            a -= 1
            y -= 1
            
    if x == y and x < 0:
        while x != -y and a > 0:
            a -= 1
            x += 1

    if x == -y:
        while x != y and x > 0 and a > 0:
            a -= 1
            y += 1
        

with open('данные.txt', 'a') as file:
    file.write('\n' + str(x) + ' ' + str(y))
