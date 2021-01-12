# Check sentence is palindrome
import re

def is_palindrome(word):
   my_new_string = re.sub('[!@#$%^&*;:,.\'/<>?]'," ",word).replace(" ","").upper()
   print(my_new_string)


   length_of_word = len(my_new_string) -1
   start_sequencer = 0

   while True:
      if start_sequencer > length_of_word:
         return True

      a = my_new_string[start_sequencer]
      b =my_new_string[length_of_word]

      if a != b:
         return False
      start_sequencer += 1
      length_of_word -= 1



lines = ["civic",
    "A man, a plan, a canal: Panama.",
    "A Toyota. Race fast, safe car. A Toyota.",
    "Cigar? Toss it in a can. It is so tragic.",
    "Dammit, I'm mad!",
    "Delia saw I was ailed.",
    "Desserts, I stressed!",
    "Draw, O coward!",
    "Lepers repel.",
    "Live not on evil.",
    "Lonely Tylenol.",
    "Murder for a jar of red rum.",
    "Never odd or even.",
    "No lemon, no melon.",
    "Senile felines.",
    "So many dynamos!",
    "Step on no pets.",
    "Was it a car or a cat I saw?",
    "Dot Net Perls is not a palindrome.",
    "Why are you reading this?",
    "This article is not useful."]


a= [is_palindrome(i) for i in lines]
print(a)





