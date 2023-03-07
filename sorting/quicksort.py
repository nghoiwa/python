import random
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
data2 = [4, 2, 3, 6, 9, 5, 7]


def quicksort(data, left, right):
    if left >= right:
        return
    pivot = random.randint(left, right)
    pivotNewposition = partition(data, left, right, pivot)
    quicksort(data, left, pivotNewposition-1)
    quicksort(data, pivotNewposition+1, right)


def partition(data, left, right, pivot):
    pivotVal = data[pivot]
    data[pivot], data[right] = data[right], data[pivot]
    nextsmallpos = left
    for i in range(left, right):
        if data[i] < pivotVal:
            data[i], data[nextsmallpos] = data[nextsmallpos], data[i]
            nextsmallpos += 1
    data[nextsmallpos], data[right] = data[right], data[nextsmallpos]
    return nextsmallpos


quicksort(data, 0, len(data)-1)
print(data)
