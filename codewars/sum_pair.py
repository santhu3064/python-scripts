
def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

print(sum_pairs(l1, 8))
print(sum_pairs(l2, -6))
print(sum_pairs(l3, -7))
print(sum_pairs(l4, 2))
print(sum_pairs(l5, 10))
print(sum_pairs(l6, 8))
print(sum_pairs(l7, 0))
print(sum_pairs(l8, 10))


