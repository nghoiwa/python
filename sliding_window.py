haystack = "sadbutsad"
needle = "sad"
def slidingwindows(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        check = True
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                check = False
        if check == True:
            return i
    return -1
def slidingwindows2(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
print(slidingwindows2(haystack, needle))
        