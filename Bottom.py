import sys
input = sys.stdin.readline

n = int(input().strip())

d = [0] * 10000

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = d[i - 1] + 2 * d[i - 2]

print(d[i] % 796796)