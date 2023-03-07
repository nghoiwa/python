from collections import defaultdict


f = open('F:\python\question1\wordlist.txt', 'r')
text = []
lines = f.readlines()
for i in lines:
    text.append(i.replace("\n",""))

def binary_search(s, target, start, end):
    if end >= start:
        middle = (start+end)//2
        if target == s[middle]:
            return middle
        elif target > s[middle]:
            return binary_search(s, target, middle+1, end) 
        elif target < s[middle]:
            return binary_search(s, target, start, middle-1) 
    else:
        return False
    
def binary_search2(s, target):
    left = 0
    right = len(s)-1
    while left <= right:
        mid = (right+left)//2
        if s[mid] == target:
            return mid
        elif s[mid] > target:
            right = mid-1
        else:
            left = mid
    return False

def diff(target, word):
    wcnt = 0
    if len(target) == len(word):
        for i in range(len(word)):
            if target[i] != word[i]:
                wcnt += 1
            if wcnt > 1:
                return False
        return wcnt == 1
    return False

dict1 = defaultdict(list)
newlist =[[x for x in text if len(x) == i] for i in range (len(max(text,key=len)))]


"""for tmp in range(len(newlist)):
    x = 0
    while x < len(newlist[tmp]):
        j = x
        print(newlist[tmp][x])
        while j < len(newlist[tmp]):
            if newlist[tmp][j]!=newlist[tmp][x] and diff(newlist[tmp][x],newlist[tmp][j]) == True:
                dict1[newlist[tmp][x]].append(newlist[tmp][j])
                dict1[newlist[tmp][j]].append(newlist[tmp][x])
            j += 1
        x += 1
"""
"""
list1 = []
for i in text:
    list1.append(binary_search(text, i, 0, len(text)-1))"""

"""
result = []
j = 0
for word in text:
    print(word)
    for w in text:
        wcnt = 0
        if len(word) == len(w):
            for i in range(len(word)):
                if w[i] != word[i]:
                    wcnt += 1
            if wcnt == 1:
                result.append(w)
    j+=1"""



