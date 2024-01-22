'''
    Sieve of Eratosthenes
'''

import sys

# read the parameter from command line using sys


arglist = sys.argv
numEnd = sys.argv[1]
print(numEnd)

# your implementation for printing the list of prime numbers

whole = list(range(2, int(numEnd)+1))

primes = []
notprimes = []

for x in whole:
    i = whole.index(x)
    for y in whole[i+1:]:
        if(y%x == 0):
            notprimes.append(y)
    if x not in  notprimes:
        primes.append(x)
    



print(primes)

