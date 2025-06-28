#python // 
#Language fundamentals
#Harvard CS50
#Remove Enemies

def remove_enemies(names, enemies):
    result = []
    for i in names:
        if i != enemies:
            result.append(i)
    return result

print(remove_enemies(["Adam", "Emmy", "Tanya"], "Emmy"))#Adam, Tanya