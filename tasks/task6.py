def F(q):
    w = 2 * q
    s = 2 * w
    e = 900 
    a = s / e
    return w, int(a)
x = int(input("Введите радиус Земли в километрах: "))
z, x = F(x)
print(z, x)
