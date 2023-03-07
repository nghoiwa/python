data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
data2 = [4, 2, 3, 6, 9, 5, 7]
def selecion_sort(data):
    for i in range(len(data)):
        minindex = i
        for j in range(i+1, len(data)):
            if data[j] < data[minindex]:
                minindex = j
        if minindex != i:
            data[i], data[minindex] = data[minindex], data[i]
    return data
print(selecion_sort(data))
