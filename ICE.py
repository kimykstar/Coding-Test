import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    # graph에 list메소드인 append를 이용하여 입력받는다.
    graph.append(list(map(int, input().rstrip())))
    
# print(graph)

def dfs(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    
    if graph[x][y] == 0:
        #상 하 우 좌 순으로 재귀 호출
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

result = 0
for i in range(n):
    for k in range(m):
        if dfs(i, k):
            result += 1
            
print(result)