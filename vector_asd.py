print('''An vector,is['math/phy', (a, b, c), x, y, z]''')
def vec_2count(a, x, b):
    if a[0] == 'math' and b[0] == 'math':
        c = ['math', (0, 0, 0), 0, 0, 0]
    elif a[0] == 'phy' and b[0] == 'math':
        c = ['phy', a[1], 0, 0, 0]
    elif a[0] == 'math' and b[0] == 'phy':
        c = ['phy', b[1], 0, 0, 0]
    else:
        if a[1] == b[1]:
            c = ['phy', a[1], 0, 0, 0]
        else:
            print('TypeError')
            pass
    if x == '+':
        c[2] = a[2] + b[2]
        c[3] = a[3] + b[3]
        c[4] = a[4] + b[4]
        return c
    elif x == '-':
        c[2] = a[2] - b[2]
        c[3] = a[3] - b[3]
        c[4] = a[4] - b[4]
        return c
    elif x == '*':
        d = a[2] * b[2] + a[3] * b[3] + a[4] * b[4]
        return d
