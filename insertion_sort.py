data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
data2 = [4, 2, 3, 6, 9, 5, 7]
def insertion_sort(data):
    if len(data) == 1:
        return data
    for i in range(1,len(data)):
        for j in range(i, 0, -1):
            if data[j] > data[j-1]:
                break
            data[j], data[j-1] = data[j-1], data[j]
    return data
print(insertion_sort(data))