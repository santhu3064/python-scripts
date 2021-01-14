# The challenge
# “7777…8?!??!“, exclaimed Bob, “I missed it again! Argh!” Every time there’s an interesting number coming up, he notices and then promptly forgets. Who doesn’t like catching those one-off interesting mileage numbers?
#
# Let’s make it so Bob never misses another interesting number. We’ve hacked into his car’s computer, and we have a box hooked up that reads mileage numbers. We’ve got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).
#
# It’s up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is “interesting” (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.
#
# Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.
#
# “Interesting” Numbers
# Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
#
# Any digit followed by all zeros: 100, 90000
# Every digit is the same number: 1111
# The digits are sequential, incementing†: 1234
# The digits are sequential, decrementing‡: 4321
# The digits are a palindrome: 1221 or 73837
# The digits match one of the values in the awesome_phrases array
# † For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
# ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
# # "boring" numbers
# is_interesting(3, [1337, 256])  # 0
# is_interesting(3236, [1337, 256])  # 0
#
# # progress as we near an "interesting" number
# is_interesting(11207, [])  # 0
# is_interesting(11208, [])  # 0
# is_interesting(11209, [])  # 1
# is_interesting(11210, [])  # 1
# is_interesting(11211, [])  # 2
#
# # nearing a provided "awesome phrase"
# is_interesting(1335, [1337, 256])  # 1
# is_interesting(1336, [1337, 256])  # 1
# is_interesting(1337, [1337, 256])  # 2

# test.describe("Basic inputs")
# test.it("Should handle {0}".format(format_msg(0, "boring numbers")))
# test.assert_equals(is_interesting(1, []), 0, result_msg(1, 0))
# test.assert_equals(is_interesting(30, []), 0, result_msg(30, 0))
# test.assert_equals(is_interesting(88, []), 0, result_msg(88, 0))
# test.assert_equals(is_interesting(97, []), 0, result_msg(97, 0))
# test.assert_equals(is_interesting(7382, []), 0, result_msg(7382, 0))
# test.assert_equals(is_interesting(99919911, []), 0, result_msg(99919911, 0))
#
# test.it("Should handle {0}".format(format_msg(0, "ordered yet still boring numbers")))
# test.assert_equals(is_interesting(7540, []), 0, result_msg(7540, 0))
# test.assert_equals(is_interesting(1590, []), 0, result_msg(1590, 0))
def is_incrementing(number): return str(number) in '1234567890'


def is_decrementing(number): return str(number) in '9876543210'


def is_palindrome(number):   return str(number) == str(number)[::-1]


def is_round(number):        return set(str(number)[1:]) == set('0')


def is_interesting(number, awesome_phrases):
   tests = (is_round, is_incrementing, is_decrementing,
            is_palindrome, awesome_phrases.__contains__)

   for num, color in zip(range(number, number + 3), (2, 1, 1)):
      if num >= 100 and any(test(num) for test in tests):
         return color
   return 0

# Method 2
def is_good(n, awesome):
   return n in awesome or str(n) in "1234567890 9876543210" or str(n) == str(n)[::-1] or int(str(n)[1:]) == 0


def is_interesting(n, awesome):
   if n > 99 and is_good(n, awesome):
      return 2
   if n > 97 and (is_good(n + 1, awesome) or is_good(n + 2, awesome)):
      return 1
   return 0

# Method 3
def is_incrementing(number):
   if  str(number) in '1234567890':
      return True
   else:
      return False


def is_decrementing(number):
   if  str(number) in '9876543210':
      return True
   else:
      return False


def is_palindrome(number):
   if str(number) == str(number)[::-1]:
      return True
   else:
      return False


def is_round(number):
   return set(str(number)[1:]) == set('0')


def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
            is_palindrome, awesome_phrases.__contains__)

    if number > 99:
        if any(test(number) for test in tests):
            return 2
        elif any(test(number+1) for test in tests):
                return 1
        elif any(test(number+2) for test in tests):
                return 1
        else:
            return 0
    elif number == 98:
        if any(test(number+1) for test in tests):
                return 1
        elif any(test(number+2) for test in tests):
                return 1
        else:
            return 0
    elif number == 99:
        if any(test(number+1) for test in tests):
            return 1
        elif any(test(number+2) for test in tests):
            return 1
        else:
            return 0
    else:
        return 0


