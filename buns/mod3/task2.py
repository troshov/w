n = int(input())
print("Неверный ввод" if n < 0 else " ".join([bin(n)[2:], oct(n)[2:], hex(n)[2:] ]))
