"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import pytest

def primes(number_of_primes):
    if (number_of_primes <= 0):
        raise ValueError
    list = []
    number = 2
    while (len(list) != number_of_primes):
        if (isPrime(number)):
            list.append(number)
        number+=1
    return list

def isPrime(number):
    for x in range(2,int(number/2)+1):
        if (number % x == 0):
            return False
    return True
