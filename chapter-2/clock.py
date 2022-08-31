
1. all the answers for this question are
5 ** 2=10
9 * 5=45
15 / 12=1.25
12 / 15=0.8
15 // 12=1
12 // 15=0
5 % 2=10
9 % 5=45
15 % 12=3
12 % 15=12
6 % 6=0
0 % 7=0



2. 2 + (3 - 1) * 10 / 5 * (2 + 3), it would be first (3-1) and (2+3) unlocked, then (3-1) would be multiplied by 10, 
divided by 5, and then multiplied by the result of (2+3) before being added by 2

3. 
current_time= input("What is the current time? ")
waiting_time = input("How many hours do you have to wait? ")

current_time = int(current_time)
waiting_time = int(waiting_time)

hours = current_time + waiting_time

timeofday = hours % 24

print(timeofday)


4. 
def which_day(start, nights):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
            'Thursday', 'Friday', 'Saturday']
    return days[(start + nights) % 7]

print(which_day(3, 10))  



