from math import sqrt

def calculate(b, c):
    D = b*b + 4*c  # считаем дискриминант
    if D > 0:  # если дискриминанат > 0 - два корня
        sq = sqrt(D)/2
        p = b/2
        x1 = p-sq
        x2 = p+sq
        return [x1, x2]

def main():
    b = int(input('Enter sum: '))
    c = -int(input('Enter mul: '))
    print(calculate(b, c))