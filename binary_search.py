import bisect
def nextGreatestLetter(letters, target):
    index = bisect.bisect(letters, target)
    return letters[index % len(letters)]
list1 = ["c","f","j"]
print(nextGreatestLetter(list1, "d"))