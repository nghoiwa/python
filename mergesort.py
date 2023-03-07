data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
data2 = [4, 2, 3, 6, 9, 5, 7]


def mergesort(data, left, right):
    if left >= right:
        return data
    middle = int((left+right)/2)
    mergesort(data, left, middle)
    mergesort(data, middle+1, right)
    merge(data, left, middle, right)


def merge(data, left, middle, right):
    tmp = []
    n = right-left+1
    l =left
    secondleft = middle+1
    while left <= middle and secondleft <= right:
        if data[left] < data[secondleft]:
            tmp.append(data[left])
            left += 1
        else:
            tmp.append(data[secondleft])
            secondleft += 1
    while left <= middle:
        tmp.append(data[left])
        left += 1
    while secondleft <= right:
        tmp.append(data[secondleft])
        secondleft += 1
    for i in range(0 ,n):
        data[l+i] = tmp[i]

mergesort(data2, 0, len(data2)-1)
print(data2)
