i = input()
n = int(input())

shift = ord(i) + n
if shift < ord('a'):
    shift += 26
elif shift > ord('z'):
    shift -= 26
otv = chr(shift)
print(otv)
