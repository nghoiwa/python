data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
data2 = [4, 2, 3, 6, 9, 5, 7]
def bubble_sort(data):
    swap = False
    for i in range(len(data)):
        for j in range(0, len(data)-i-1):
            if data[j] > data[j+1]:
                swap = True
                print(data)
                data[j], data[j+1] = data[j+1], data[j]
                print(data)
        if not swap:
            return
    return data
print(bubble_sort(data2))