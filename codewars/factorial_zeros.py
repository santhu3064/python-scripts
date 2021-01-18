# How many trailing zeroes would be found in 4617!, upon expansion?
# I'll apply the procedure from above:
#
# 51 :  4617 ÷ 5 = 923.4, so I get 923 factors of 5
# 52 :  4617 ÷ 25 = 184.68, so I get 184 additional factors of 5
# 53 :  4617 ÷ 125 = 36.936, so I get 36 additional factors of 5
# 54 :  4617 ÷ 625 = 7.3872, so I get 7 additional factors of 5
# 55 :  4617 ÷ 3125 = 1.47744, so I get 1 more factor of 5
# 56 :  4617 ÷ 15625 = 0.295488, which is less than 1, so I stop here.
# #



def zeros(n):
    a = n // 5
    if a >= 5:
        return a + zeros(a)
    else:
        return a


def get_zeros(n):
   a =5
   sum =0
   while n//a >0:
      sum += n//a
      a *= 5
   return sum



# 5's: 4617 ÷ 5 = 923.4 (write down 923), 923.4 ÷ 5 = 184.68 (write down 184), 184.68 ÷ 5 = 36.936 (write down 36), 36.936 ÷ 5 = 7.3827 (write down 7), 7.3827 ÷ 5 = 1.47744 (write down 1), and 1.47744 ÷ 5 is goint to be less than 1, so you'
#
# 've written down the whole numbers, and sum them to get 1151.


def get_n_zeros(n):
   sum =0
   while n/5 > 0:
      sum += n//5
      n //= 5
   return sum

print(get_n_zeros(10000))
print(get_zeros(10000))
