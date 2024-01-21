'''
    Sieve of Eratosthenes
'''

import sys

# read the parameter from command line using sys
n = int(sys.argv[1])

# your implementation for printing the list of prime numbers
num = [x for x in range(2, n+1)]
last_prime = 2
last_prime_index = 0
while last_prime <= n:
    num = [x for x in num if (x % last_prime != 0) or (x <= last_prime)]
    if last_prime_index < len(num)-1:
        last_prime_index += 1
        last_prime = num[last_prime_index]
    else:
        break
print(num)


