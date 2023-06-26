def number(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            yield 'FrizzBuzz'
        elif i % 5 == 0:
            yield 'Buzz'
        elif i % 3 == 0:
            yield 'Friiz'
        else:
            yield i

print(*number(100), sep='\n')