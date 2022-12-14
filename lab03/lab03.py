def falling(n, k):
    """Рассчитать убывающий факториал от n глубины k.

    >>> falling(6, 3)  
    120
    >>> falling(4, 3) 
    24
    >>> falling(4, 1)
    4
    >>> falling(4, 0)
    1
    """

# "*** YOUR CODE HERE ***"

    factor = n
    if k == 0:
        return 1
    for i in range(1, k):
        n = n-1
        factor *= n
    return factor




def sum_digits(y):
    """Сложить все цифры числа y.

    >>> sum_digits(10) 
    1
    >>> sum_digits(4224) 
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123)
    >>> a
    6
    """

# "*** YOUR CODE HERE ***"
    y = str(y)
   
    sum = 0
    for i in y:
        sum += int(i)
    return sum




def double_eights (n):
    """Возвращает True если в n есть две цифры 8 подряд.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """

# "*** YOUR CODE HERE ***"

    return '88' in str(n)
