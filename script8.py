#!/usr/bin/env python3

a = input()
b = input()
c = input()
if a == 'trunk':
    print('Введите режим работы интрефейса(access/trunk):', a)
    print('Вветиде тип и номер интерфейса:', b)
    print('Введите разрешенные VLANы):', c)

if a == 'access':
    print('Введите режим работы интрефейса(access/trunk):', a)
    print('Вветиде тип и номер интерфейса:', b)
    print('Введите номер VLAN:', c)
    
access_template = [
    "switchport mode access", "switchport access vlan"+ " " + str(c),
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "swithport trunk encapsulation dot1q", "swithport mode trunk",
        "swithport trunk allowed vlan"+ " " + str(c)
]


    
if a == 'trunk':
    print('Interface', b)
    str(trunk_template).split(',')
    for i in range(len(trunk_template)):
        print(trunk_template[i])
if a == 'access':
    print('Interface', b)
    str(access_template).split(',')
    for i in range(len(access_template)):
        print(access_template[i])
