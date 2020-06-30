import time


def is_economical2(n):
    b = time.time()
    prm, pow = [], []
    prm = prime_fact(n)
    pow = power(prm, pow, n)
    if sum([len(str(i)) for i in pow + prm if i != 1]) == len(str(n)):
        return f"Equadigital {round(time.time() - b, 5)} saniyede  getirdik."
    elif sum([len(str(i)) for i in pow + prm if i != 1]) > len(str(n)):
        return f"Wasteful {round(time.time() - b, 5)} saniyede getirdik."
    else:
        return f"Frugal {round(time.time() - b, 5)} saniyede  getirdik."


def is_prime(n):
    return all([n % i for i in range(2, n)]) and n != 1


def prime_fact(n):
    return [i for i in range(2, n + 1) if is_prime(i) and not n % i]


def power(prm, pow, num):
    count = 0
    for i in prm:
        while (not num % i):
            num /= i
            count += 1
        pow.append(count)
        count = 0
    return pow


print(is_economical2(150528))
