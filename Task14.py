n = int(input('введите число N: '))
k = 0
for i in range(n):
  if 2**k < n:
    print(k)
    k +=1
print(k)    