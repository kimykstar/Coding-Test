import sys
input = sys.stdin.readline

# n : 노드의 갯수, m : 간선의 갯수
n, m = map(int, input().strip().split())
start = int(input().strip())
INF = int(1e9)
distance = [INF] * (n + 1)
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    idx, node, dis = map(int, input().strip().split())
    graph[idx].append([node, dis])

def get_smallest_node():
    s_node = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < s_node and visited[i] == False:
            s_node = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
        
    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
            current = distance[now] + i[1]
            if current < distance[i[0]]:
                distance[i[0]] = current


dijkstra(start)

for i in range(1, n + 1):
    print(distance[i])