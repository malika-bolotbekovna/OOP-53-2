# big O нотация
# import time

# target = 99999
# arr = list(range(1000000000))
# O(1)
# def get_element(arr, index):
#     return(arr[index])

# print(get_element([1, 65, 34, 23, 87, -5, 12, 34, 2], 6))


# O(log n)
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
        
#         elif arr[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1
#         return -1

# arr = [1, 3, 5, 7, 9, 11, 13]
# target = 7


# print(binary_search(arr, target))


# O(n)
# arr = [1, 3, 5, 7, 9, 11, 13]
# target = 7

# def find_element(arr, target):
#     for i, value in enumerate(arr):
#         if value == target:
#             return i
#     return -1


# print(find_element(arr, target))


# start_1 = time.time()
# binar = binary_search(arr, target)
# end_1 = time.time()

# start_2 = time.time()
# binar = find_element(arr, target)
# end_2 = time.time()

# print(f"binary: {start_1 - end_1}:6f")
# print(f"find: {start_1 - end_1}:6f")
# enumerate - может возвращать и индекс и значение


# пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[i] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# arr = [5, 1, 4, 2, 8]
# print(bubble_sort(arr))

nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return[num_map[complement], index]
        num_map[num] = index
        
print(two_sum(nums, target))

