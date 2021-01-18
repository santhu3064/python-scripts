
# Number time a prime number present ina factorial

def get_power(n, a):
   sum = 0
   while n // a > 0:
      sum += n // a
      n //= a
   return sum
