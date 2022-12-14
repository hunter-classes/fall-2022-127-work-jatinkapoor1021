
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








Download modes.py (I have copied pasted it here):
  import datetime
import random

def findLargest(dataset):
    largeSoFar = dataset[0]
    for item in dataset[1:]:
        if item > largeSoFar:
            largeSoFar = item
    return largeSoFar



def freq(dataset,v):
    # since this loops over the
    # entire data set once
    # it takes n time 
    #count = 0
    #for item in dataset:
    #    if item == v:
    #        count = count + 1
    #return count
    return len([x for x in dataset if x == v])

def buildRandomList(size,maxvalue):
    #result = []
    #for x in range(size):
    #    result.append(random.randrange(maxvalue))
    #return result
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 


def mode(dataset):
    """
    Returns a mode of the dataset, that is
    the value that appears most frequently

    if multiple values appear the same # of times and are
    most frequent, return any of them.

    Ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the most
    mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4 since
    both of those values appear 3 times which is the most

    Strategy:
    assume the first value is the mode
    we can grab its frequency

    for each remaining item in the dataset:
      count that items frequence and see if it's the new
      mode so far    
    """
    modeSoFar = dataset[0]
    freqSoFar = dataset.count(modeSoFar)
    for item in dataset[1:]: #outer loop -> n
        # calling freq each time is n
        # if freq(dataset,item) > freqSoFar:
        if dataset.count(item) > freqSoFar:
            modeSoFar = item
            freqSoFar = dataset.count(item)
    return modeSoFar


def fastMode(dataset):
    # assume all values in dataset
    # are between 0 and 99 inclusive

    # 1. make a list of 100 slots
    # and set them all to 0
    # this will store our tallies

    # 2. Loop through our dataset
    # and for each item incremement
    # (add 1) to the appropriate
    # slot in the tallies list

    # 3. the index with the highest
    # value in tallies is the mode

    pass

    
def testMode(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = mode(dataset)
    print("Mode: ",m)

def testFindLargest(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    
    
    
    
    fastmode:
      
def fastMode(dataset):
    
    slots=[]
    for i in range(100):
        slots.append(0)
        

    for i in dataset:
        slots[i]+=1
    
    
    index=0
    for i in range(len(slots)):
        if slots[i]>slots[index]:
            index=i
    return index
print(fastMode([1,2,3,3,3,4,7,7,6,8]))
