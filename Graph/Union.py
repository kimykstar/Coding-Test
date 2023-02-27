import sys
input = sys.stdin.readline

# x의 부모노드를 찾는다.
def find_parent(parent, x):
    if parent[x] == x:
        return parent[x]
    else:
        # 경로 압축기법(부모노드 갱신)
        parent[x] = find_parent(parent, parent[x])
        return parent[x]
        # 경로 압축 X
        # return find_parent(parent, parent[x])

# a와 b노드를 union한다.
def union_parent(parent, a, b):
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)
    if a_parent >= b_parent:
        parent[a] = b_parent
    else:
        parent[b] = a_parent
# 노드, 간선의 개수 입력받기
v, e = map(int, input().strip().split())
parent = [0] * (v + 1)
# 부모노드 초기화
for i in range(1, v + 1):
    parent[i] = i
    
# union연산 노드 입력받기
for _ in range(e):
    a, b = map(int, input().strip().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합:", end=' ')
for i in range(1, len(parent)):
    print(find_parent(parent, i), end=' ')
print()

print("부모 테이블: ", end='')
for i in range(1, len(parent)):
    print(parent[i], end=' ')