#python // 
#Language fundamentals
#Harvard CS50
# Sum numbers

def sum_numbers(n):
    lst = []
    total_sum = 0
    for i in range(1, n + 1):
        lst.append(i)
    
    for i in lst:
        total_sum += i
    
    return total_sum

print(sum_numbers(5))        