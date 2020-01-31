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
    quality_s = random.randint(1, 13)
    health = health + quality_s
    if lan == 1:
        print('血量增加%d' % (quality_s))
    elif lan == 2:
        print('health increase %d' % (quality_s))
#
quality_n = 0
while quality_n < 2:
    quality_n = quality_n + 1
    quality_s = random.randint(1, 13)
    armor = armor + quality_s
    if lan == 1:
        print('护甲增加%d' % (quality_s))
    elif lan == 2:
        print('armor increase %d' % (quality_s))
#
quality_n = 0
while quality_n < 2:
    quality_n = quality_n + 1
    quality_s = random.randint(1, 13)
    attack = attack + quality_s
    if lan == 1:
        print('攻击增加%d' % (quality_s))
    elif lan == 2:
        print('attack increase %d' % (quality_s))
#
quality_n = 0
while quality_n < 2:
    quality_n = quality_n + 1
    quality_s = random.randint(1, 13)
    money = money + quality_s
    if lan == 1:
        print('金钱增加%d' % (quality_s))
    elif lan == 2:
        print('money increase %d' % (quality_s))
#
quality_n = 0
while quality_n < 2:
    quality_n = quality_n + 1
    quality_s = random.randint(1, 13)
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
    if lan == 1:
        event = ['半兽人', '骷髅', '营地', '商店']
    elif lan == 2:
        event = ['orc', 'skeleton', 'camp', 'shop']
    w = random.randint(1, 4)
    a = random.randint(1, 4)
    d = random.randint(1, 4)
    s = random.randint(1, 4)
    wstr = event[w - 1]
    astr = event[a - 1]
    dstr = event[d - 1]
    sstr = event[s - 1]
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
        non_health = random.randint(1, 13)
        battle_s = 0
        while battle_s == 0:
            print('#')
            player = 'Health:%d, Armor:%d, Attack:%d, Money:%d, Food:%d' % (health, armor, attack, money, food)
            print(player)
            if lan == 1:
                print('敌人：', non_health)
            elif lan == 2:
                print('enemy:', non_health)
            non_attack = random.randint(1, 13)
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
            money = money + random.randint(1, 13)
            if lan == 1:
                print('金钱增加')
            elif lan == 2:
                print('money increase')
            food = food + random.randint(1, 13)
            if lan == 1:
                print('食物增加')
            elif lan == 2:
                print('food increase')
            food = food - random.randint(1, 13)
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
        non_health = random.randint(1, 13)
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
            non_attack = random.randint(1, 13)
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
            money = money + random.randint(1, 13)
            if lan == 1:
                print('金钱增加')
            elif lan == 2:
                print('money increase')
            food = food + random.randint(1, 13)
            if lan == 1:
                print('食物增加')
            elif lan == 2:
                print('food increase')
            food = food - random.randint(1, 13)
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
            print('[A 食物->金钱, B 金钱->食物, C 金钱->护甲, D 金钱->攻击, E 离开]')
        elif lan == 2:
            print('[A food->money, B money->food, C money->armor, D money->attack, E quit]')
        shop_choose = input('choose:')
        shop_s = random.randint(1, 13)
        if shop_choose == 'A':
            food = food - shop_s
            money = money + shop_s
        else:
            if money - shop_s >= 0:
                if shop_choose == 'B':
            	    food = food + shop_s
            	    money = money - shop_s
                elif shop_choose == 'C':
                    armor = armor + shop_s
                    money = money - shop_s
                elif shop_choose == 'D':
                    attack = attack + shop_s
                    money = money - shop_s
            else:
                if lan == 1:
                    print('金钱不足')
                elif lan == 2:
                    print('more money needed')
        print('#####')
    

        
        
