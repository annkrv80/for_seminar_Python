def prime(n):
    for i in range(2, int((n**0.5)+1)):
        if n % i == 0:
            return False
        else:
            return True


def gener_ptime_num(num):
    count = 0
    yield 2
    number = 3
    while count < num - 1:
        if prime(number):
            yield number
        count += 1
        number += 1

print(*gener_ptime_num(11))