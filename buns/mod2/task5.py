In = input()
ind = In.find(",")
i = In[:ind]
n = int(In[ind+1:])
shift = ord(i) + n
if shift < ord('a'):
    shift += 26
elif shift > ord('z'):
    shift -= 26
otv = chr(shift)
print(otv)
