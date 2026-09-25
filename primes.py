"""Поиск простых чисел до заданного предела."""


def primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


if __name__ == "__main__":
    print(primes_up_to(100))
