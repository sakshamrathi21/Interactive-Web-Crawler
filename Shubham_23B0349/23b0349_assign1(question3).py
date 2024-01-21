def check(a):
    if a<2:
        return False
    for i in range(2,a-1):
            if (a%i==0):
                return False
    return True
def prime(n):
  prime_n=[]
  for i in range(2,n+1):
       if(check(i)):
           prime_n.append(i)
  return prime_n
n=int(input("Enter number"))
prime_numbers=prime(n)
print(prime_numbers)