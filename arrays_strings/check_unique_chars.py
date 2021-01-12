# Implemnet an alogorithm if the string has all unique algorithms what if you cannot use additional data structures
import unittest

def get_unique(word):
   unique= []
   for i in word:
      if i not in unique:
         unique.append(i)
   if len(unique) != len(word):
      return False
   else:
      return True

# Assuming general ascii 128 if extend ascii can use 256
def get_unique_ascii(word):
   if len(word) > 128:
      return False

   character_set = [ False for _ in range(128)]

   for j in word:
      val = ord(j)
      if character_set[val]:
         return False
      character_set[val] = True
   return True

class Test(unittest.TestCase):

   passdata = ["gjsai","327gsae"]
   faildata = ["notnunique","1hhj27"]

   def test_valid(self):
      for string in self.passdata:
         self.assertTrue(get_unique_ascii(string))

   def test_invalid(self):
      for string in self.faildata:
         self.assertFalse(get_unique_ascii(string))


if __name__ == "__main__":
    unittest.main()
