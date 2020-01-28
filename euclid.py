def eu_count(a, b):
    '''测量measure'''
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
	'''判整is it an integer'''
    if eu_count(a, 1) == 0:
        return True
    else:
        return False
###
def gcd(a, b):
	'''最大公因数greatest common factor'''
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
def prime_2num(a, b):
	'''判互质are them coprime'''
    if gcd(a, b) == 1:
        return True
    else:
        return False
###
def prop_2num(a, b):
	'''最简数对simplest num_pair'''
    if prime_2num(a, b) == True:
        return(a, b)
    else:
        c = gcd(a, b)
        return(a / c, b / c)
###
def lcm(a, b):
	'''最小公倍数least common multiple'''
    c = prop_2num(a, b)[0]
    return b * c

        
