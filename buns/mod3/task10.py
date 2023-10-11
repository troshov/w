a = int(input())
otv = []
otv2 = []
for i in range(0,a):
    otv.append([])
    otv2.append([])
    for k in range(0, a):
        otv[i].append(k+1)
        otv2[i].append(i+1)

for i in range(a):
    for k in range(a):
        if k != a - 1:
            print(otv[i][k], end = ", ")
        else:
            print(otv[i][k])

print()

for i in range(a):
    for k in range(a):
        if k != a - 1:
            print(otv2[i][k], end = ", ")
        else:
            print(otv2[i][k])

