"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

def primes(number_of_primes):
    if (number_of_primes <= 0):
        raise ValueError
        
    list = [2]
    candidate = 3
    while (len(list) < number_of_primes):
        i = 0
        isPrime = True
        while (list[i] <= math.sqrt(candidate)):
            if (not (candidate % list[i])):
                isPrime = False
                break
            i += 1

        if (isPrime):
            list.append(candidate)

        candidate += 2

    return list
