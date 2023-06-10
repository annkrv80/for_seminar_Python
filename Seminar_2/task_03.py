num = int(input('Введите целое число '))


def conver(num: int, system: int ):

    result = list()
    while num > 0:
        result.append(str(num % system))
        num = num // system
    result.reverse()
    return ''.join(result)


print(f"Число {num} в двоичной системе {bin(num)}")
print(conver(num, 2))

print(f"Число {num} в восьмеричной системе {oct(num)}")
print(conver(num, 8))
