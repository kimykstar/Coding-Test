import sys
input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent

# 노드, 간선        
v, e = map(int, input().strip().split())
parent = [0] * (v + 1)

edges = []
sum = 0
 
for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b, dist = map(int, input().strip().split())
    edges.append((dist, a, b))

# 간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않은 경우
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        sum += cost

print(sum)