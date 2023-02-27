import sys
from collections import deque
input = sys.stdin.readline

# 노드와 간선 입력받기
v, e = map(int, input().strip().split())
# 모든 노드의 진입 차수 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 입력받기 위한 graph선언
graph = [[] for i in range(v + 1)]

for _ in range(e):
    start, end = map(int, input().strip().split())
    graph[start].append(end)
    indegree[end] += 1
    
# 위상정렬 함수
def TopologySort():
    result = []
    queue = deque()
    
    # 진입차수가 0인 노드를 큐에 넣는다.
    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        result.append(node)
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    for i in result:
        print(i, end=' ')
TopologySort()