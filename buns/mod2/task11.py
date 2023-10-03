a = input()
s = False
while 1:
    for i in range(0, len(a)):
        for k in range(0, len(a)):
            if i!=k:
                if a[i] == a[k] and a[i] != " ":
                    s = True
                    break
    break
print(s)
