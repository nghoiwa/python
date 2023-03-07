nums = [2,2,2,2,2]
target = 8
def two_sum(nums, target):
    hashmap = {}
    for index, number in enumerate(nums):
        tmp = target - number
        if tmp not in hashmap:
            hashmap[number] = index
        else:
            return [hashmap[tmp], index]
    return False
def three_sum(nums, target):
    if len(nums) < 3:
        return 0
    nums = sorted(nums)
    hashmap = set()
    for i in range(len(nums)):
        start = i+1
        end = len(nums)-1
        want = target - nums[i]
        while start < end:
            if nums[start] + nums[end] == want:
                hashmap.add((nums[i], nums[start], nums[end]))
                start += 1
                end -=1
            elif nums[start] + nums[end] > want:
                end -= 1
            else:
                start += 1
    return list(hashmap)
def four_sum(nums, target):
    if len(nums) < 4:
        return 0
    nums = sorted(nums)
    hashmap = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            want = target - nums[i] - nums[j]
            start = j+1
            end = len(nums)-1
            while start < end:
                if nums[start] + nums[end] == want:
                    hashmap.add((nums[i], nums[j] , nums[start], nums[end]))
                    start += 1
                    end -=1
                elif nums[start] + nums[end] > want:
                    end -= 1
                else:
                    start += 1
    return list(hashmap)
print(four_sum(nums, target))