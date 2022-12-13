5. 
def max(lst):
    max_ele = lst[0]
    for ele in lst[1:]:
        if max_ele < ele:
            max_ele = ele 
    return max_ele



lst = [45,30, 284, 484.5, 544,]
print(max(lst))


7. 
import random
def Odd(lst):
    odd = 0
    for e in lst:
        if e % 2 != 0:
            odd = odd + 1
    return odd
lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(Odd(lst))


8.
def addsum(EvenList):
    sum=0
    for i in EvenList:
        if i%2==0:
            sum+=i
    print("The sum of even numbers in the list : ",sum)
EvenList=[1,2,3,4,5,6,7,8,9,10]
addsum(EvenList)
