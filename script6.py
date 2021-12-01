#!/usr/bin/env python3
d = ''
mask_list = []
count = 0
b = input().split('.')

c = b[3].split('/')
b[3] = c[0]

for i in range(32):
    if i < int(c[1]): 
        d += '1'
    else:
        d += '0'

d = d[0:int(c[1])] + '0' * (32 - int(c[1]))

d.split()
c1 = list(str(d[0:8])[::-1])
c2 = list(str(d[8:16])[::-1])
c3 = list(str(d[16:24])[::-1])
c4 = list(str(d[24:32])[::-1])

for i in range(8):
    if int(c1[i]) == 1:
        count += (2 ** i)    
mask_list.append(count)

count = 0

for i in range(8):
    if int(c2[i]) == 1:
        count += (2 ** i)    
mask_list.append(count)

count = 0

for i in range(8):
    if int(c3[i]) == 1:
        count += (2 ** i)    
mask_list.append(count)

count = 0

for i in range(8):
    if int(c4[i]) == 1:
        count += (2 ** i)        
mask_list.append(count)
octat4 = count
count = 0

b[3] = octat4

print('Network:')
for i in b:
    print(i, end= ' ' * (10 - len(str(i))))
print()
for i in b:
    print(bin(int(i))[2:].zfill(8), end ='  ')
print()
print('Mask:')
print(c[1])



for i in mask_list:
    print(i, end=' ' * (10 - len(str(i))))
print()
for i in range(4):
    print(bin(int(mask_list[i]))[2:].zfill(8), end ='  ')
