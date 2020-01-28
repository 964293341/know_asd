def ya(n):
    L = list(range(n + 1))
    m = 1
    for x in L:
        if x == L[0]:
            continue
        else:
            m = m * x
    return m
###
def e(n):
    L = list(range(n + 1))
    e = 0
    for x in L:
        e = e + (1 / ya(x))
    return e

