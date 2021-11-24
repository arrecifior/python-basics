############################################################
###                                                      ###
###   This frogram finds prime numbers in range [1;20]   ###
###                                                      ###
############################################################

def is_prime(num):
    if_prime = True
    for i in range(2, round(num**0.5) + 1):
        if num % (i) == 0:
            if_prime = False
            break
    return if_prime

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
