#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('#####')
s1 = 0
while s1 == 0:
    s1 = 1
    print('计算器')
    s_no1 = input('the first number:')
    no1 = int(s_no1)
    print(' ')
    print('[', '+', '-', '*', '/', ']')
    function = input('the function:')
    print(' ')
    s_no2 = input('the second number:')
    no2 = int(s_no2)
    print(' ')
    if function == '+':
        print('%s + %s =' % (s_no1, s_no2), no1 + no2)
        print(' ')
        s2 = input('quit please input\'q\', continue please input\'c\':')
        if s2 == 'q':
            exit()
        elif s2 == 'c':
            s1 = 0
            print(' ')
    elif function == '-':
        print('%s - %s =' % (s_no1, s_no2), no1 - no2)
        print(' ')
        s2 = input('quit please input\'q\', continue please input\'c\':')
        if s2 == 'q':
            exit()
        elif s2 == 'c':
            s1 = 0
            print(' ')
    elif function == '*':
        print('%s * %s =' % (s_no1, s_no2), no1 * no2)
        print(' ')
        s2 = input('quit please input\'q\', continue please input\'c\':')
        if s2 == 'q':
            exit()
        elif s2 == 'c':
            s1 = 0
            print(' ')
    elif function == '/':
        print('%s / %s =' % (s_no1, s_no2), no1 / no2)
        print(' ')
        s2 = input('quit please input\'q\', continue please input\'c\':')
        if s2 == 'q':
            exit()
        elif s2 == 'c':
            s1 = 0
            print(' ')
        
    
