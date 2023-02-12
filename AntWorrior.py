import sys
input = sys.stdin.readline

n = int(input().strip())
store = list(map(int, input().strip().split()))

d = [0] * 100

d[0] = store[0]
d[1] = store[1]
for i in range(2, n):
    d[i] = max(store[i - 1], store[i - 2] + store[i])
    
print(d[n - 1])