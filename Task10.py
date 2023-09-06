import random

n = int(input('введите число лежащих монет: '))
avers_count = 0
revers_count = 0
for i in range(n):
  revers = random.randint(0, 1) # 0 - орел, 1 - решка
  print(revers, end=' ')
  if revers == 0:
    avers_count +=1
  if revers == 1:
    revers_count +=1
print(f'\nмонет на орле = {avers_count}, \nмонет на решке = {revers_count}')
if avers_count < revers_count:
  print (f'\nнаименьшее число переворотов = ', avers_count)
else: 
 print (f'\nнаименьшее число переворотов = ', revers_count)