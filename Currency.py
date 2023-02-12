import sys
input = sys.stdin.readline

# n : 화폐의 종류, m : 가치의 합
n, m = map(int, input().strip().split())
money = []
d = [10001] * (m + 1)
d[0] = 0
for i in range(n):
    money.append(int(input().strip()))

for i in range(0, len(money)):
    for k in range(money[i], m + 1):
        if d[k - money[i]] != 10001:
            d[k] = min(d[k], d[k - money[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])