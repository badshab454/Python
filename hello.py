#python // 
#Control flow
#Even odd transform

def even_odd_transform(lst, n):
    add_to_odd = n * 2
    minus_to_even = n * 2
    result = []
    
    for i in lst:
        if i % 2 == 0:
            result.append(i - minus_to_even)
        else:
            result.append(i + add_to_odd)
    return result


print(even_odd_transform([3, 4, 9], 3))



