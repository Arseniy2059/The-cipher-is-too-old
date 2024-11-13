def f(p):
    a = 1
    s = ''
    while a < p:
        b = a + 1
        while b < p:
            if p %(a+b) == 0:
                s += str(a) + str(b)
            b += 1
        a += 1
    return s


print(f(14))