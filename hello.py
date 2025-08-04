#python // 
#Loops
#Sum of V0wEls

def is_equal(lst):
    a, b = lst
    sum_a = sum(int(d) for d in str(abs(a)))
    sum_b = sum(int(d) for d in str(abs(b)))
    
    return sum_a == sum_b

print(is_equal([304, 401]))