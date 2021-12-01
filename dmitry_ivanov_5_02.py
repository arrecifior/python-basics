#################################################################
###                                                           ###
###   This program calculates Fibonacci numbers               ###
###                                                           ###
#################################################################

def fibo(num):
    fib1 = 0
    fib2 = 1
    if num < 2:
        return None
    else:
        for i in range(2, num + 1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2

print("This program finds Fibonacci sequence for n.")
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(fibo(i))
