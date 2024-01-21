'''
    Sieve of Eratosthenes
'''

import sys

# read the parameter from command line using sys

# Check for arguments:
if len(sys.argv) != 2:
    print("Usage: python3 main.py <value>")
    sys.exit(1)

# Get the value from the command line argument
value_str = sys.argv[1]
num = int(value_str)

# your implementation for printing the list of prime numbers
num_list = [x for x in range(2,num+1)]
primes = []

while num_list:
    num = num_list[0]
    primes.append(num)
    num_list = [x for x in num_list if x % num != 0]

print(primes)





