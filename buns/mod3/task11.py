a = []
a.append(input())
for i in range(len(a[0]) - 1):
    a.append(input())

               
st = True
for i in a:
    if len(set(i)) == 1:
        print(i[0])
        st = False
        break

a2 = []

if st:
    for i in range(len(a)):
        a2.append("")
        for k in range(len(a)):
            a2[i] += a[k][i]


for i in a2:
    if len(set(i)) == 1:
        print(i[0])
        st = False
        break

if st:print("Ничья")
