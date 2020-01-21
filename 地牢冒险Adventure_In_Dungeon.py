#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
print('#####')
print('''地牢冒险 Adventure in Dungeon
        By asd''')
lan = 2
s0 = 0
while s0 == 0:
    print('[start, language, exit]')
    s1 = input('choose:')
    if s1 == 'exit':
        exit()
    elif s1 == 'language':
        s2 = 0
        while s2 == 0:
            s2 = 1
            print('[Chinese, English]')
            lan_s = input('choose:')
            if lan_s == 'Chinese':
                lan = 1
            elif lan_s == 'English':
                lan = 2
            else:
                print('')
                print('TypeError')
                print('')
                s2 = 0
    elif s1 == 'start':
        s0 = 1
    else:
        print('')
        print('TypeError')
        print('')
#####
print('#####')
health = 0
armor = 0
attack = 0
money = 0
food = 0
#
quality_n = 0
while quality_n < 3:
    quality_n = quality_n + 1
    quality_s = int(random.uniform(1,14))
    health = health + quality_s
    if lan == 1:
        print('血量增加%d' % (quality_s))
    elif lan == 2:
        print('health increase %d' % (quality_s))
#
quality_n = 0
while quality_n < 3:
    quality_n = quality_n + 1
    quality_s = int(random.uniform(1,14))
    armor = armor + quality_s
    if lan == 1:
        print('护甲增加%d' % (quality_s))
    elif lan == 2:
        print('armor increase %d' % (quality_s))
#
quality_n = 0
while quality_n < 1:
    quality_n = quality_n + 1
    quality_s = int(random.uniform(1,14))
    attack = attack + quality_s
    if lan == 1:
        print('攻击增加%d' % (quality_s))
    elif lan == 2:
        print('attack increase %d' % (quality_s))
#
quality_n = 0
while quality_n < 2:
    quality_n = quality_n + 1
    quality_s = int(random.uniform(1,14))
    money = money + quality_s
    if lan == 1:
        print('金钱增加%d' % (quality_s))
    elif lan == 2:
        print('money increase %d' % (quality_s))
#
quality_n = 0
while quality_n < 2:
    quality_n = quality_n + 1
    quality_s = int(random.uniform(1,14))
    food = food + quality_s
    if lan == 1:
        print('食物增加%d' % (quality_s))
    elif lan == 2:
        print('food increase %d' % (quality_s))
#
player = 'Health:%d, Armor:%d, Attack:%d, Money:%d, Food:%d' % (health, armor, attack, money, food)
#####
print('#####')
s3 = 0
armor_s = armor
health_s = health
while s3 == 0:
    if food <= 0:
                health = health - 1
                if lan == 1:
                    print('扣血')
                elif lan == 2:
                    print('health decrease')
    if health <= 0:
        print('DIED')
        quit()
    elif armor <= 0:
        armor = 0
    else:
        armor = armor_s
    player = 'Health:%d, Armor:%d, Attack:%d, Money:%d, Food:%d' % (health, armor, attack, money, food)
    print(player)
    w = int(random.uniform(1,5))
    a = int(random.uniform(1,5))
    d = int(random.uniform(1,5))
    s = int(random.uniform(1,5))
    #
    if w == 1:
        if lan == 1:
            wstr = '半兽人'
        elif lan == 2:
            wstr = 'orc'
    elif w == 2:
        if lan == 1:
            wstr = '骷髅'
        elif lan == 2:
            wstr = 'skeleton'
    elif w == 3:
        if lan == 1:
            wstr = '营地'
        elif lan == 2:
            wstr = 'camp'
    elif w == 4:
        if lan == 1:
            wstr = '商店'
        elif lan == 2:
            wstr = 'shop'
    #
    if a == 1:
        if lan == 1:
            astr = '半兽人'
        elif lan == 2:
            astr = 'orc'
    elif a == 2:
        if lan == 1:
            astr = '骷髅'
        elif lan == 2:
            astr = 'skeleton'
    elif a == 3:
        if lan == 1:
            astr = '营地'
        elif lan == 2:
            astr = 'camp'
    elif a == 4:
        if lan == 1:
            astr = '商店'
        elif lan == 2:
            astr = 'shop'
    #
    if d == 1:
        if lan == 1:
            dstr = '半兽人'
        elif lan == 2:
            dstr = 'orc'
    elif d == 2:
        if lan == 1:
            dstr = '骷髅'
        elif lan == 2:
            dstr = 'skeleton'
    elif d == 3:
        if lan == 1:
            dstr = '营地'
        elif lan == 2:
            dstr = 'camp'
    elif d == 4:
        if lan == 1:
            dstr = '商店'
        elif lan == 2:
            dstr = 'shop'
    #
    if s == 1:
        if lan == 1:
            sstr = '半兽人'
        elif lan == 2:
            sstr = 'orc'
    elif s == 2:
        if lan == 1:
            sstr = '骷髅'
        elif lan == 2:
            sstr = 'skeleton'
    elif s == 3:
        if lan == 1:
            sstr = '营地'
        elif lan == 2:
            sstr = 'camp'
    elif s == 4:
        if lan == 1:
            sstr = '商店'
        elif lan == 2:
            sstr = 'shop'
    #
    print('''    [%s]
[%s]    [%s]
    [%s]''' % (wstr, astr, dstr, sstr))
    move = input('choose[w, a, s, d]:')
    if move == 'w':
        act = w
    elif move == 'a':
        act = a
    elif move == 's':
        act = s
    elif move == 'd':
        act = d
    if act == 1:
        print('#####')
        if lan == 1:
            print('开战')
        elif lan == 2:
            print('battle!')
        non_attack = 0
        non_health = int(random.uniform(1, 14))
        battle_s = 0
        while battle_s == 0:
            print('#')
            player = 'Health:%d, Armor:%d, Attack:%d, Money:%d, Food:%d' % (health, armor, attack, money, food)
            print(player)
            if lan == 1:
                print('敌人：', non_health)
            elif lan == 2:
                print('enemy:', non_health)
            non_attack = int(random.uniform(1, 14))
            if lan == 1:
                print('受击%d' % (non_attack))
            elif lan == 2:
                print('hurt%d' % (non_attack))
            player_attack = attack
            if lan == 1:
                print('攻击%d' % (player_attack))
            elif lan == 2:
                print('hit%d' % (player_attack))
            if player_attack >= non_attack:
                non_health = non_health - 1
            else:
                if armor > 0:
                    armor = armor - (non_attack - player_attack)
                else:
                    armor = 0
                    health = health - (non_attack - player_attack)
            if non_health <= 0:
                battle_s = 1
            elif health <= 0:
                battle_s = 2
            else:
                wugan = input('[Enter]')
        if battle_s == 1:
            money = money + int(random.uniform(1, 14))
            if lan == 1:
                print('金钱增加')
            elif lan == 2:
                print('money increase')
            food = food + int(random.uniform(1, 14))
            if lan == 1:
                print('食物增加')
            elif lan == 2:
                print('food increase')
            food = food - int(random.uniform(1, 14))
            if lan == 1:
                print('吃饭')
            elif lan == 2:
                print('have lunch')
        print('#####')
    if act == 2:
        print('#####')
        if lan == 1:
            print('开战')
        elif lan == 2:
            print('battle!')
        non_attack = 0
        non_health = int(random.uniform(1, 14))
        battle_n = 0
        battle_s = 0
        while battle_s == 0:
            print('#')
            battle_n = battle_n + 1
            player = 'Health:%d, Armor:%d, Attack:%d, Money:%d, Food:%d' % (health, armor, attack, money, food)
            print(player)
            if lan == 1:
                print('敌人：', non_health)
            elif lan == 2:
                print('enemy:', non_health)
            non_attack = int(random.uniform(1, 14))
            if lan == 1:
                print('受击%d' % (non_attack))
            elif lan == 2:
                print('hurt%d' % (non_attack))
            player_attack = attack
            if lan == 1:
                print('攻击%d' % (player_attack))
            elif lan == 2:
                print('hit%d' % (player_attack))
            if battle_n < 3:
                if player_attack >= non_attack:
                    non_health = non_health - 1
                else:
                    if armor > 0:
                        armor = armor - (non_attack - player_attack)
                    else:
                        armor = 0
                        health = health - (non_attack - player_attack)
            else:
                if player_attack >= non_attack:
                    non_health = non_health
                else:
                    if armor > 0:
                        armor = armor - (non_attack - player_attack)
                    else:
                        armor = 0
                        health = health - (non_attack - player_attack)
                battle_n = 0
            if non_health <= 0:
                battle_s = 1
            elif health <= 0:
                battle_s = 2
            else:
                wugan = input('[Enter]')
        if battle_s == 1:
            money = money + int(random.uniform(1, 14))
            if lan == 1:
                print('金钱增加')
            elif lan == 2:
                print('money increase')
            food = food + int(random.uniform(1, 14))
            if lan == 1:
                print('食物增加')
            elif lan == 2:
                print('food increase')
            food = food - int(random.uniform(1, 14))
            if lan == 1:
                print('吃饭')
            elif lan == 2:
                print('have lunch')
        print('#####')
    if act == 3:
        print('#####')
        health = health_s
        if lan == 1:
            print('回血')
        elif lan == 2:
            print('health increase')
        print('#####')
    if act == 4:
        print('#####')
        if lan == 1:
            print('[A 食物->金钱, B 金钱->食物, C 离开]')
        elif lan == 2:
            print('[A food->money, B money->food， C quit]')
        shop_choose = input('choose:')
        shop_s = int(random.uniform(1, 14))
        if shop_choose == 'A':
            food = food - shop_s
            money = money + shop_s
        elif shop_choose == 'B':
            food = food + shop_s
            money = money - shop_s
        else:
            print('OK')
        print('#####')
    

        
        
