from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    # 큐가 비어 있을때 까지
    while queue:
        # 큐에서 값을 pop한 후 출력
        v = queue.popleft()
        print(v, end='')
        # pop한 노드의 인접 노드들을 차례로 방문한다(방문되지 않은 노드라면)
        # 방문한 노드를 큐에 추가한다.
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)