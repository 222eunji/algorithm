import sys
input = sys.stdin.readline


# 집의 수 m, 길의 수 n
# x번 집, y번 집, 양방향 도로의 거리 z미터
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


while True:
    m, n = map(int, input().split())
    if m == 0 and n==0:
        break
    edges = []
    total_cost = 0
    # 간선 리스트 만들기
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total_cost += z

    parent = list(range(m))

    edges.sort()
    mst_cost = 0
    count = 0

    for cost, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            mst_cost += cost
            count += 1
            if count == m - 1:
                break

    print(total_cost - mst_cost)