import random

n = 5

def TestCase(n):
    TestLst = []
    for i in range(n):
        numcasual = random.randint(1, 100)
        TestLst.append(numcasual)
    return (TestLst)


print(TestCase(n))

a = (TestCase(n))


def MergeSort(lst):
    if len(lst) == 1:
        return lst

    left = lst[0:len(lst) // 2]
    right = lst[len(lst) // 2:]

    left = MergeSort(left)
    right = MergeSort(right)

    return Merge(left, right)


def Merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    while len(left) > 0:
        res.append(left.pop())

    while len(right) > 0:
        res.append(right.pop())

    return res


MergeSort(a)
print('MergeSort: ', a)


def Partition(ls, p, r):
    pivot = ls[p]
    i = p
    j = r
    while (1):
        while (ls[i] < pivot and ls[i] != pivot):
            i += 1
        while (ls[j] > pivot and ls[j] != pivot):
            j -= 1

        if (i < j):
            t = ls[i]
            ls[i] = ls[j]
            ls[j] = t
        else:
            return j


def QuickSort(ls, p, r):
    if (p < r):
        q = Partition(ls, p, r)
        QuickSort(ls, p, q)
        QuickSort(ls, q + 1, r)


QuickSort(a, 0, len(a) - 1)
print('QuickSort: ', a)




