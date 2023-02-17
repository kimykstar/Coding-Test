import sys
from collections import deque
queue = deque()
input = sys.stdin.readline
# 여기서 얻을 수 있는것
# DFS가 BFS에 비해 탐색 속도가 빠르다. 이 문제에서 BFS로 풀면 시간초과
# DFS로 풀 시 케이스가 많으면 재귀호출 초과가 된다.
# 상, 하, 좌, 우
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# x, y좌표에서 너비우선 탐색
def bfs(array, row, column):
    queue.append((row, column))
    count = 0
    while queue:
        q = queue.popleft()
        row = q[0]
        column = q[1]
        # 방문처리
        if array[row][column] == 1:
            array[row][column] = 2
            count += 1
        # 상, 하, 좌, 우 탐색
        for i in range(len(move)):
            mrow = row + move[i][0]
            mcolumn = column + move[i][1]
            # 농장 범위에 해당하고 배추인 경우
            if mrow >= 0 and mrow < len(array) and mcolumn >= 0 and mcolumn < len(array[0]) and array[mrow][mcolumn] == 1:
                queue.append((mrow, mcolumn))
                
                
    return count

def dfs(array, row, column):
    if row < 0 or row >= len(array) or column < 0 or column >= len(array[0]):
        return False
    
    if array[row][column] == 1:
        array[row][column] = 2
        dfs(array, row - 1, column)
        dfs(array, row + 1, column)
        dfs(array, row, column - 1)
        dfs(array, row, column + 1)
        return True
    return False

def dfs2(array, row, column):
    stack = deque()
    stack.append((row, column))
    while stack:
        val = stack.pop()
        row = val[0]
        column = val[1]
        array[row][column] = 2
        for i, k in move:
            mrow = row + i
            mcol = column + k
            if mrow >= 0 and mrow < len(array) and mcol >= 0 and mcol < len(array[0]) and array[mrow][mcol] == 1:
                stack.append((mrow, mcol))
                
    return True

        
    
t = int(input().strip())
for _ in range(t):
    cabbage = []
    # m : 가로, n : 세로
    m, n, k = map(int, input().strip().split())
    graph = [[0] * m for _ in range(n)]
    # 배추의 위치 입력받기
    for _ in range(k):
        x, y = map(int, input().strip().split())
        graph[n - 1 - y][x] = 1
        cabbage.append([n - 1 - y, x])
    
    result = 0
    
    for i, k in cabbage:
        if graph[i][k] == 1:
            if dfs2(graph, i, k) == True:
                result += 1
                
    print(result)
