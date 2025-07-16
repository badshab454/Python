#python // 
#Loops
#Give me the even numbers

def sum_even_nums_in_range(start, stop):
    total_sum = 0
    even_lst = []
    for i in range(start, stop + 1):
        if i % 2 == 0:
            even_lst.append(i)
    
    return sum(even_lst)


print(sum_even_nums_in_range(10, 20))

