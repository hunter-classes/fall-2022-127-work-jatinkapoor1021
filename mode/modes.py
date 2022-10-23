
First function:
  
  

list1 = [20, 5, 8, 63, 44, 85]
 
list1.sort()
print("Smallest element is:", list1[0])



Second function:
  
def frequency(l, v):
    count = 0
     
    for i in l:
        if i == v: count += 1
    return count
 
l = [1, 2, 2, 3, 6, 2, 4]
v = 2
print(frequency(l, v))
