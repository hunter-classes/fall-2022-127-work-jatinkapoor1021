Exercise 4: 

  
def average(numlist):

    total = 0
    for num in numlist:
        total = total + num

    return total / len(numlist)



6.

import random
xs = []
for i in range(3):
    xs.append(random.randint(0,75))

def sum_of_squares(xs):
    sum_of_squares=0  
    for i in (xs):
        squared = i * i  
        sum_of_squares += squared  
    return sum_of_squares

print (sum_of_squares(xs))
