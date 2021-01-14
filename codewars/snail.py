#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

#array = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
#snail(array) #=> [1,2,3,6,9,8,7,4,5]
#For better understanding, please follow the numbers of the next array consecutively:

#array = [[1,2,3],
 #        [8,9,4],
  #       [7,6,5]]
#snail(array) #=> [1,2,3,4,5,6,7,8,9]
#This image will illustrate things more clearly:

#NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

#NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

def snail(snail_map):
    output = []
    
    while len(snail_map) > 0:
        output += snail_map[0]
        del(snail_map[0])
    
        if len(snail_map) > 0:
            for i in range(len(snail_map)):
                output.append(snail_map[i][-1])
                del(snail_map[i][-1])
            if snail_map[-1]:
                output += snail_map[-1][::-1]
                del(snail_map[-1])
#             print(output)
            
            for j in reversed(snail_map):
                output += [j[0]]
                del [j[0]]
                
    return output
            
        
        
        
