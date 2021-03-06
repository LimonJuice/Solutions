#Solve Me First

def solveMeFirst(a, b):
    num1 = a
    num2 = b
    return (a + b)


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1, num2)
print(res)


#Simple Array Sum

import sys


def simpleArraySum(n, ar):
    return (sum(ar))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)



#Compare The Triplets

def solve(a0, a1, a2, b0, b1, b2):
    a = (1 if a0 > b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0)
    b = (1 if a0 < b0 else 0) + (1 if a1 < b1 else 0) + (1 if a2 < b2 else 0)
    return (a, b)


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))


#A Very Big Sum

def aVeryBigSum(n, ar):
    return (sum(ar))


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)


#Diagonal Difference

n = int(input().strip())
a = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a += a_t[a_i] - a_t[n - a_i - 1]

print(abs(a))



#Plus-Minus

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos = 0
neg = 0
none = 0
for i in arr:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        none += 1
print(pos/len(arr))
print(neg/len(arr))
print(none/len(arr))



#Staircase

n = int(input())
for i in range(1,n+1):
    print(('#'*i).rjust(n,' '))



#Mini-Max Sum

arr = list(map(int, input().strip().split(' ')))
max=-sys.maxsize-1
min=sys.maxsize
sum=0
for i in arr:
    sum+=i
    if i>max:
        max=i
    if i<min:
        min=i
print (sum-max,sum-min)





#Birthday Cake Candles

from collections import *
def birthdayCakeCandles(n, ar):
    res = Counter(ar)
    return res.most_common()[0][1]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)




#Time Conversion

import time

def timeConversion(time):
    if time[-2:] == "AM" and time[:2] == "12":
        return("00" + time[2:8])
    elif time[-2:] == "PM" and time[:2] == "12":
        return("12" + time[2:8])
    elif time[-2:] == "AM":
        return(time[:-2])
    else:
        print(str(int(time[:2]) + 12) + time[2:8])

time = input().strip()
timeConversion(time)
s = input().strip()
result = timeConversion(s)
print(result)


