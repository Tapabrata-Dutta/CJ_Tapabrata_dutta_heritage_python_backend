def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check up to √n
        if n % i == 0:
            return False
    return True


print('Prime numbers between 1 and 50:')
primes = [n for n in range(2, 51) if is_prime(n)]
print(primes)
