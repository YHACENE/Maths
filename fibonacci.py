#coding: utf-8
"""
def febonacci(n):

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
       return febonacci(n - 1) + febonacci(n - 2)

for n in range(1, 101):
    print(n, " : ", febonacci(n))
"""
# Amelioration of the algorithm using memorization
"""
fibonacci_cache = {}
def fibonacci_a(n):
    #if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    #compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_a(n - 1) + fibonacci_a(n - 2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 1001):
    print(n, " : ", fibonacci_a(n))
"""
# Another way to calculate fibonacci sequence

from functools import lru_cache

@lru_cache(maxsize = 1000)

def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(1, 501):
    print(n , " : ", fibonacci(n))
