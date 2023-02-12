import sys
input = sys.stdin.readline

# recursion
def binary_search(array, start, end, target):
    if start > end:
        return None
    middle = (start + end) // 2
    if array[middle] == target:
        return middle
    else:
        if target > array[middle]:
            return binary_search(array, middle + 1, end, target)
        elif target < array[middle]:
            return binary_search(array, start, middle - 1, target)

n, target = map(int, input().strip().split())
array = list(map(int, input().strip().split()))

#for
def binary_search2(array, target):
    right = len(array) - 1
    left = 0
    middle = (left + right) // 2
    result = -1
    
    while left <= right:
        if target > array[middle]:
            left = middle + 1
            middle = (left + right)  // 2
        elif target < array[middle]:
            right = middle - 1
            middle = (left + right) // 2
        elif target == array[middle]:
            result = middle
            break
        
    return result

print(binary_search(array, 0, len(array) - 1, target))
print(binary_search2(array, target))