# 1 способ нахождения совершенных чисел
def ideal_number():
    for i in range(1,10000):
        s = 1
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                s += j
        if s == i and i > 1:
            print(i)
    print('\nВсе совершенные числа в диапозоне от 1 до 1000000 найдены\n')

# 2 способ нахождения совершенных чисел
def ideal_number2():
    print(6)
    sum = 1
    counter = 1
    for i in range(3,16,2):
        sum += i**3
        counter +=1
        if not(counter & (counter - 1)):
            print (sum)
    print('\nВсе совершенные числа в диапозоне от 1 до 1000000 найдены\n')



# 1 способ нахождения дружественных пар
def friendly_number_1():
    for i in range(1, 100000):
        sum1 = friendly_number1_inner(i)
        sum2 = friendly_number1_inner(sum1)
        if ((sum2 == i) and (sum1 != sum2) and (i < sum1)):
            print(i, sum1)
    print('\nВсе дружественные числа в диапозоне от 1 до 100000 найдены\n') 

def friendly_number1_inner(value):
    res = 1
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            res += i + value // i
    return res

# 2 способ нахождения дружественных пар
def friendly_number2():
    for i in range(1, 100000):
        j = friendly_number2_inner(i)
        if i < j <= friendly_number2_inner(i) and i == friendly_number2_inner(j):
            print(i, j)
    print('\nВсе дружественные числа в диапозоне от 1 до 100000 найдены\n') 


def friendly_number2_inner(n):
    s = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            s += k
    return s


ideal_number()
ideal_number2()
friendly_number_1()
friendly_number2()
