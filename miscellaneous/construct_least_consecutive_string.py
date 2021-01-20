# Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.¶

import unittest

def get_final_string(word):

   a =[ i for i in word]
   length_of_word = len(word)
   i=0
   k = 1
   h =[]

   while i < length_of_word-1:
      if (a[i] == a[i+1]):
         k += 1
      else:
         h.append((a[i],k))
         k=1
      i = i+1
   h.append((a[i], k))
   return h


def get_consecutive(word):
   t = get_final_string(word)
   finalString = ""
   for s,k in t:
      mul = s * k
      ad = s + str(k)

      if len(ad) < len(mul):
         finalString += ad
      else:
         finalString += mul

   return finalString



class TestLeastConsecutiveString(unittest.TestCase):
   def test_scenario_one(self):
      self.assertEqual(get_consecutive('ABCDEFG'),'ABCDEFG',"pass")

   def test_scenario_two(self):
      self.assertEqual(get_consecutive('AABBCCDDEEFF'),'AABBCCDDEEFF',"pass")

   def test_scenario_three(self):
      self.assertEqual(get_consecutive('AABCCDDDDGGGBSASSASSSSSAAA'),'AABCCD4G3BSASSAS5A3',"pass")

   def test_scenario_four(self):
      self.assertEqual(get_consecutive('ZZHJSIKLKKJKSIIIKAJAHSHHA'),'ZZHJSIKLKKJKSI3KAJAHSHHA',"pass")

if __name__ == "__main__":
   unittest.main()

#





