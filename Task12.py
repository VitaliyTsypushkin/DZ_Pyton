s = int(input('введите сумму чисел: '))
m = int(input('введите произведение: '))
a = 1
b = 2
for i in range(s-b):
    if (a*b) == m:
        print(f'\nпервое число - {a}, второе число - {b}')
        break
    else:   
        a +=1
        b = s - a