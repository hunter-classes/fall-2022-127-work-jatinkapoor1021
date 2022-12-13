def addlist(list1, list2):
    newlist = []
    for i in range(0, len(list1)):
        newlist.append(list1[i] + list2[i])
        
    return newlist

list1 = [1,2,3]
list2 = [10,20,30]
addlist = addlist(list1, list2)
print(addlist) 
