#python // 
#Language fundamentals
#Harvard CS50

#same parity?

def parity_analysis(num):
    string_num = str(num)
    total_sum = 0
    for i in string_num:
        total_sum += int(i)
    
    return total_sum % 2 == num % 2


print(parity_analysis(243))