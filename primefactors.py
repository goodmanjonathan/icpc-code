import math

# Num is the number pre-factorial
def find_prime_factors(num):
    factors = []
    for i in range(2, num + 1):
        factors.append(i)

    return factors

def isprime(num):
    if num == 1 or num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(1, num, 2):
        if num % i == 0:
            return False

testcase_amt = input()
for _ in testcase_amt:
    prime_factors = find_prime_factors(int(input()))
    print(prime_factors)
