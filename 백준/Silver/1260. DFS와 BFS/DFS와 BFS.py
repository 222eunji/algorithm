import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

# dfs 풀이
visited_d = [False] * (N+1)
def dfs(v):
    visited_d[v] = True
    print(v, end=' ')
    for nxt in graph[v]:
        if not visited_d[nxt]:
            dfs(nxt)


# bfs 풀이
visited_b = [False] * (N+1)
def bfs(start):
    q = [start]
    visited_b[start] = True
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for nxt in graph[v]:
            if not visited_b[nxt]:
                visited_b[nxt] = True
                q.append(nxt)

dfs(V)
print()
bfs(V)