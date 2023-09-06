# print('введите первое число: ')
# a = int(input())
# b =  int(input('введите второе число: '))
# print(a, ' + ', b, " = ", a + b)

# c = 0
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# a = 1.234
# b = 2.345
# print(round(a*b, 3))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4

# a = 1 < 4 and 2 > 1
# print(a)

# n = 234
# print(n%10 + n//10%10 + n//100)


# n = 314314
# if(n//100000 + (n%100000)//10000 + (n%10000)//1000 == (n%1000)//100 + (n%100)//10 + n%10):
#   print ('yes')
# else:
#   print ('no')

# a =  int(input('введите первое число: '))
# b =  int(input('введите второе число: '))
# c =  int(input('введите третье число: '))
# if ((a * b) - c > 0 and c != 1):
#   print('yes')
# else:
#   print('no')

# n = 345 # сумма цифр числа
# summa = 0
# while n > 0:
#   x = n % 10
#   summa = summa + x
#   n = n // 10
# print (summa)

# n = int(input()) # нахождение наименьшего делителя
# flag = True
# i = 2
# while flag:
#   if n % i == 0:
#     flag = False
#     print(i)
#   elif i > n // 2:
#     print (n)
#     flag = False
#   i += 1

# a = 'qwerty' # вывод на консоль посимвольно вертикально
# for i in a:
#   print(i)

# line = "" #вывод на печать 5 рядов звездочек
# for i in range(5):
#   line = ""
#   for j in range(5):
#     line += "*"
#   print (line)

text = 'съешь ещё этих мягких французских булок'
print(text[6:-18])