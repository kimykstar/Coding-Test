import sys
input = sys.stdin.readline

n = int(input().strip())

d = [0] * 30001

# 바텀 업 방식
# 제일 천천히 줄어드는 계산을 먼저 진행한다.
def f1(n):
    for i in range(2, n + 1):
        # 1로 뺀 경우
        d[i] = d[i - 1] + 1
        # 2로 나누어지는 경우
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    return d[n]

def f2(n):
    if n == 1:
        return 1
    
    if n % 5 == 0:
        f2(n // 5)
    if n % 3 == 0:
        f2(n // 3)
    if n % 2 == 0:
        f2(n // 2)
    f2(n - 1)
  
    
    d[n] = d[n - 1] + 1
    if n % 2 == 0:
        d[n] = min(d[n], d[n // 2] + 1)
    if n % 3 == 0:
        d[n] = min(d[n], d[n // 3] + 1)
    if n % 5 == 0:
        d[n] = min(d[n], d[n // 5] + 1)
    
    return d[n]
print(f1(n))
print(f2(n))