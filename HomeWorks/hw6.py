nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return i, j

        
print(two_sum(nums, target))
