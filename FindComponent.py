import sys
input = sys.stdin.readline
n = int(input().strip())
component = list(map(int, input().strip().split()))
m = int(input().strip())
request = list(map(int, input().strip().split()))

# 재귀버전 이진탐색
def binary_search(array, start, end, target):
    middle = (start + end) // 2
    if start > end:
        return None
    else:
        if array[middle] < target:
            return binary_search(array, middle + 1, end, target)
        elif array[middle] > target:
            return binary_search(array, start, middle - 1, target)
        elif array[middle] == target:
            return middle

def binary_search2(array, target):
    start = 0
    end = len(array) - 1
    
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            start = middle + 1
        elif array[middle] > target:
            end = middle - 1

            
    return None

# 계수정렬을 이용한 탐색
def count_search(component, target):
    array = [0] * 1000001
    for i in range(len(component)):
        array[component[i]] += 1
    
    if array[target] > 0:
        return True

    return False

def set_search(component, target):
    s = set(component)
    
    if target in s:
        return True
    
    return False
        
    
# 오름차순으로 정렬
component.sort()

for i in request:
    if binary_search(component, 0, len(component) - 1, i) != None:
        print("yes", end=' ')
    else:
        print("No", end=' ')
print()
for i in request:
    if binary_search2(component, i) != None:
        print("yes", end=' ')
    else:
        print("No", end=' ')
print()
for i in request:
    if count_search(component, i) != False:
        print("yes", end=' ')
    else:
        print("No", end=' ')
print()
for i in request:
    if set_search(component, i) != False:
        print("yes", end=' ')
    else:
        print("No", end=' ')
print()

