# Iterative approach time complexy O(n^2)



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



