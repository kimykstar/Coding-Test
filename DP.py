#fib
def fib(num):
    if num == 1 or num == 2:
        return 1
    
    return fib(num - 1) + fib(num - 2)

store = [0] * 101

# 탑다운(하향식)
# dp를 이용한 fib함수
def fib_dp(num):
    if num == 1 or num == 2:
        return 1
    if store[num] != 0:
        return store[num]
    store[num] = fib_dp(num - 1) + fib_dp(num - 2)
    return store[num]
    
# print(fib(40))
print(fib_dp(99))

# 바텀업(상향식)
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])