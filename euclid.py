def eu_count(a, b):
    '''测量'''
    if a < b:
        m = b
        n = a
    else:
        m = a
        n = b
    
    x = 0
    while x == 0:
        c = m - n
        if c >= n:
            m = c
        else:
            return c
###
def z_num(a):
    if eu_count(a, 1) == 0:
        return True
    else:
        return False
###
def gcd(a, b):
    if z_num(a) == True and z_num(b) == True:
        if a > b:
            m = a
            n = b
        else:
            m = b
            n = a
        x = 1
        while x > 0:
            x = m - n
            if x > n:
                m = x
            elif x == 0:
                return n
            else:
                m = n
                n = x
    else:
        print('type_error')
        pass
###
def mass_2num(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False
###
def prop_2num(a, b):
    if mass_2num(a, b) == True:
        return(a, b)
    else:
        c = gcd(a, b)
        return(a / c, b / c)
###
def lcm(a, b):
    c = prop_2num(a, b)[0]
    return b * c

        
