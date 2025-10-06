def Z(n):
    s = str(n)
    if len(s) != 4 or not s.isdigit():
        raise ValueError("Входное число должно быть четырёхзначным.")
    e = [(int(d) + 7) % 10 for d in s]
    e[0], e[2] = e[2], e[0]
    e[1], e[3] = e[3], e[1]
    b = ''.join(map(str, e))
    return int(b)
x = int(input("Введите четырёхзначное число: "))
с = Z(x)
print("Зашифрованное число:", с)


