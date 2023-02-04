import sys
input = sys.stdin.readline
nums = list(map(int, input().strip().split()))
# array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 선택 정렬 (오름차순)
def selectSort(nums, reverse):
    lens= len(nums)
    # 오름차순 reverse == False
    if reverse == False:
        for i in range(lens, 0, -1):
            max_idx = 0
            for k in range(0, i):
                if nums[max_idx] < nums[k]:
                    max_idx = k
            #스왑
            nums[max_idx], nums[k] = nums[k], nums[max_idx]
            
    # 내림차순 reverse == True
    elif reverse == True:
        for i in range(lens, 0, -1):
            min_idx = 0
            for k in range(0, i):
                if nums[min_idx] > nums[k]:
                    min_idx = k
            nums[min_idx], nums[k] = nums[k], nums[min_idx]
        
# 삽입 정렬 (오름차순)
def insertSort(nums, reverse):
    lens = len(nums)
    # 오름차순 정렬
    if reverse == False:
        for i in range(1, lens):
            for k in range(i, 0, -1):
                if nums[k] < nums[k - 1]:
                    nums[k], nums[k - 1] = nums[k - 1], nums[k]
                else:
                    break
    # 내림차순 정렬
    elif reverse == True:
        for i in range(1, lens):
            for k in range(i, 0, -1):
                if nums[k] > nums[k - 1]:
                    nums[k], nums[k - 1] = nums[k - 1], nums[k]
                else:
                    break
                
# 퀵정렬
def quickSort(nums, start, end, reverse):
    if start >= end:
        return
    lens = end - start + 1
    # 피벗 설정
    piv = start
    right = end
    left = start + 1
    
    # 퀵정렬(오름차순)
    if reverse == False:
        while left <= right:
            while left <= end and nums[left] <= nums[piv]:
                left += 1
            while right > start and nums[right] >= nums[piv]:
                right -= 1
            # 엇갈렸다면 피벗과 작은 데이터를 교체
            if right < left:
                nums[piv], nums[right] = nums[right], nums[piv]
            else:
                nums[left], nums[right] = nums[right], nums[left]
        
        quickSort(nums, start, right - 1, False)
        quickSort(nums, right + 1, end, False)
        
    # 퀵정렬(내림차순)
    elif reverse == True:
        while left <= right:
            while left <= end and nums[left] >= nums[piv]:
                left += 1
            # right > start로 놓는 이유 : right와 piv의 자리를 변경하는데 인덱스가 start와 end 사이의 범위로 벗어날 수 있기 때문에
            # 범위 벗어나기 억제 역할을 '<' 가 해줌... 따라서 left > right일때 pivot과 바꿀 인덱스를 억제하기 위해서 < 부등호를 쓴다.
            while right > start and nums[right] <= nums[piv]:
                right -= 1
            if right < left:
                nums[right], nums[piv] = nums[piv], nums[right]
            else:
                nums[left], nums[right] = nums[right], nums[left]
        quickSort(nums, start, right - 1, True)
        quickSort(nums, right + 1, end, True)

# 계수정렬
def countSort(nums, reverse):
    array = [0] * (max(nums) + 1)
    result = []
    
    for i in nums:
            array[i] += 1
    
    if reverse == False:
        for i in range(len(array)):
            for k in range(array[i]):
                result.append(i)
    
    elif reverse == True:
        for i in range(len(array) - 1, -1, -1):
            for k in range(array[i]):
                result.append(i)
    return result

# 선택정렬(오름차순)
selectSort(nums, False)
print("Select Incre:", nums) 
# 선택정렬(내림차순)
selectSort(nums, True)
print("Select Dec", nums)
# 삽입정렬(오름차순)
insertSort(nums, False)
print("Insert Incre:", nums)
# 삽입정렬(내림차순)
insertSort(nums, True)
print("Insert Dec:", nums)
# 퀵정렬(오름차순)
quickSort(nums, 0, len(nums) - 1, False)
print("Quick Incre:",nums)
# 퀵정렬(내림차순)
quickSort(nums, 0, len(nums) - 1, True)
print("Quick Dec:",nums)
# 계수정렬(오름차순)
result = countSort(nums, False)
print("Count Incre", result)
# 계수정렬(내림차순)
result = countSort(nums, True)
print("Count Dec", result)