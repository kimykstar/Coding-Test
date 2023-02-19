import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().strip().split())
start = int(input().strip())
distance = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]
# 노드와 간선정보 입력받기
for _ in range(m):
    idx, node, dis = map(int, input().strip().split())
    graph[idx].append((node, dis))
    
def dijkstra(start):
    # 큐 선언
    q = []
    # heap에 거리와 노드의 정보를 q에넣는다.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 거리정보와 노드의 정보를 q에서 pop한다.
        dist, now = heapq.heappop(q)
        # 만약 지금 노드의 거리가 새로 pop한 거리보다 작다면 다시 반복문 실행
        if distance[now] < dist:
            continue
        # 현재 노드의 인접노드들의 간선을 살펴본다.
        for i in graph[now]:
            # 인접노드까지의 거리를 계산
            current = dist + i[1]
            # 이전에 계산된 인접노드의 거리와 방금 계산한 인접노드를 비교하여 최소값을 저장한다.
            if current < distance[i[0]]:
                distance[i[0]] = current
                # 우선순위큐에 거리와 노드의 번호를 넣는다.
                heapq.heappush(q, (current, i[0]))
                
dijkstra(start)

for i in range(1, n + 1):
    print(distance[i])
        
        
        