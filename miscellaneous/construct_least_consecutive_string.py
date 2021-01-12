# Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.¶


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






t = get_final_string('AAABCCDDDDGGGBSASSASSSSSAAA')
print(t)

finalString = ""
for s,k in t:
   mul = s * k
   ad = s + str(k)

   if len(ad) < len(mul):
      finalString += ad
   else:
      finalString += mul

print(finalString)









