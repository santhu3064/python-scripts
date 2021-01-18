# Iterative approach time complexy O(n^2)
import math
def get_primes(n):
    a= int(math.sqrt(n)+1)
    total = []
    for i in range(2,n+1):
        prime = True
        for j in range(2,i):
            if i%j ==0:
                prime = False
        if prime:
            total.append(i)
    return total




# Iterative approach time complexy O(n)
def is_prime(n):
   if n <= 1:
      return False

   max_div = math.floor(math.sqrt(n))
   for i in range(2, 1 + max_div):
      if n % i == 0:
         return False
   return n

def get_primes(n):
   a = []
   for i in range(1, n + 1):
      x = is_prime(i)
      if x:
         a.append(i)
   return a


# Sieve method less time complexity


def if_prime(n):
   primes =[ True for i in range(n+1)]
   a =2
   while (a * a <= n):
      if primes[a] :
         for i in range(a * a, n + 1, a):
            primes[i] = False
      a += 1
   if primes[n]:
      return n


print(if_prime(114))

for i in range(2,100):
   if if_prime(i):
      print(i)



