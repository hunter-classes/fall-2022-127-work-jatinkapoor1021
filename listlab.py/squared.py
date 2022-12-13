def square(list):
    newlist = []
    for i in list:
        newlist.append(i ** 2)
    return newlist

list = [1, 2, 3, 4]
newlist = square(list)
print(newlist)
