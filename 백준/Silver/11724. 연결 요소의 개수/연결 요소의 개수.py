import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)

def bfs(start):
    q = [start]
    visited[start] = True
    while q:
        v = q.pop(0)
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

cnt = 0
for n in range(1, N+1):
    if not visited[n]:
        cnt += 1 
        bfs(n)

print(cnt)

