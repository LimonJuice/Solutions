#Intro to Tutorial Challenges

a = input()
b = input()
print(input().split().index(a))



#Insertions Sort-pt1

n = int(input())
arr = [int(x) for x in input().split()]


def insertion_sort(arr):
    e = arr[len(arr) - 1]
    ar = arr[0:len(arr) - 1]
    l = len(ar)
    last = l - 1
    parr = []
    while last > -1:
        tmp = ar[last]
        if tmp < e:
            break
        parr = ar[0:last] + [tmp] + ar[last:l]

        print(" ".join(str(s) for s in parr))
        last = last - 1
    parr[last + 1] = e
    print(" ".join(str(s) for s in parr))


insertion_sort(arr)


#Insertion Sort-pt2

b=int(input())
a=[int(x) for x in input().strip().split(' ')]
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
    print(*a)


#Correctness and the Loop Invariants


def insertion_sort(l):
    for i in range(1, len(ar)):
        a = ar[i]
        j = i - 1
        while a < ar[j] and j >= 0:
            ar[j + 1] = ar[j]
            ar[j] = a
            j = j - 1

    return (" ".join(map(str, ar)))


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str, ar)))



#Running Time Algorithm


def insertion_sort(l):
    count = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j+1] = l[j]
            count +=1
            j -= 1
        l[j+1] = key
    return count

m = input()
l = [int(i) for i in input().strip().split()]

print(insertion_sort(l))

#Quicksort 1-Partition

n = int(input())
arr = [int(i) for i in input().split()]
l, r = [], []
eq = [arr[0]]

for i in range(1, n):
    if arr[i] < arr[0]:
        l.append(arr[i])
    elif arr[i] == arr[0]:
        eq.append(arr[i])
    elif arr[i] > arr[0]:
        r.append(arr[i])
sum = l + eq + r

print(' '.join([str(i) for i in sum]))


#Counting Sort 1

n = int(input())
a = [0]*100
for i in map(int,input().split()):
    a[i]+=1
print(*a)



#Counting Sort2

from collections import Counter
n, a =int(input()), list(map(int, input().split()))
print(*(Counter(sorted(a)).elements()))


#The Full Counting Sort

n = int(input())

arr = []
for i in range(n):
    if i < n//2:
        a, b = input().strip().split()
        arr.append((int(a),'-'))
    else:
        a,b = input().strip().split()
        arr.append((int(a),b))

arr.sort(key=lambda tup: tup[0])
print(*[x[1] for x in ar])


#Find the Median


import statistics
n=int(input())
l=[int(i) for i in input().split()]
l.sort()
print(statistics.median(l))