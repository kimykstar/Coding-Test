import sys
input = sys.stdin.readline
# n : 떡의 개수, m : 요청한 떡의 길이
n, m = map(int, input().strip().split())

height = list(map(int, input().strip().split()))

cm = max(height)

sum = 0
while sum < m:
    cm -= 1
    sum = 0
    for i in height:
        if i - cm > 0:
            sum += (i - cm)

print(cm)