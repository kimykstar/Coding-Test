import sys
from collections import deque
input = sys.stdin.readline

# 듣고자 하는 강의의 수
n = int(input().strip())
# 진입차수 정의
indegree = [0] * (n + 1)
# 간선 정의
graph = [[] for i in range(n + 1)]
time = [0] * (n + 1)

# 간선정보 받기
for i in range(1, n + 1):
    # 시간, 진입간선 노드, -1
    data = list(map(int, input().strip().split()))
    # 과목 이수시간 저장
    time[i] = data[0]
    # 선수과목이 있는 경우
    if len(data) != 2:
        graph[data[1]].append(i)
        indegree[i] += 1

# 강의 수강의 최소시간을 출력
def topologySort():
    # time리스트를 그대로 복사함
    result = time.copy()
    queue = deque()
    # 진입차수가 0인 노드를 큐에 넣는다.
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        # 인접노드를 살펴본다.
        for i in graph[node]:
            result[i] = max(result[i], result[node] + time[i])
            # 인접노드의 진입차수 -1
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    for i in result:
        print(i, end=' ')

topologySort()
