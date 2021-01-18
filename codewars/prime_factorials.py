# n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
# since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.
#
# n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"
#
# n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
# Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.
#
# Notes
#
# the function is decomp(n) and should return the decomposition of n! into its prime factors in increasing order of the primes, as a string.
# factorial can be a very big number (4000! has 12674 digits, n can go from 300 to 4000).
# In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.


import math
# def get_primes(n):
#     a= int(math.sqrt(n)+1)
#     total = []
#     for i in range(2,n+1):
#         prime = True
#         for j in range(2,i):
#             if i%j ==0:
#                 prime = False
#         if prime:
#             total.append(i)
#     return total


import time

# Faster method as looping is reduced
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


print(get_primes(100))


def get_power(n, a):
   sum = 0
   while n // a > 0:
      sum += n // a
      n //= a
   return sum


def decomp(n):
   # your code here
   finalcount = ""
   primes = get_primes(n)
   print(primes)
   for i in primes:
      powers = get_power(n, i)
      if powers == 1:
         finalcount += str(i) + " * "
      if powers > 1:
         finalcount += str(i) + "^" + str(powers) + " * "
   return finalcount.rstrip(" * ")

