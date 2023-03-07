def isValid(s):
        if len(s)%2 != 0: return False
        stack = []
        dict1 = {"(": ")", "{": "}", "[" : "]"}
        for i in s:
            print(stack)
            if len(stack) == 0:
                stack.append(i)
            else:
                tmp = stack.pop()
                print(dict1[tmp])
                stack.append(tmp)
                stack.append(i) 
        return len(stack) == 0
print(isValid("([)]"))