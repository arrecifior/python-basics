def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for v in powers_of_2(8):
    print(v)

t = list(powers_of_2(3))
print(t)

for i in range(20):
    if i in powers_of_2(4):
        print(i)

t = [x for x in powers_of_2(5)]
print(t)


def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)

