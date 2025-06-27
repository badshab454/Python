#python // 
#Language fundamentals
#Harvard CS50
#Add the index

def nth_smallest(lst, n):
  sorted_list = sorted(lst)
  return sorted_list [n - 1]

print(nth_smallest([1, 3, 2], 3)) # 1, 2, 3