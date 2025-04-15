#python list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []

for x in fruits:
    if "n" in x:
        newlist.append(x)

print(newlist)


