def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

def prime_generator():
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1

prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen))

