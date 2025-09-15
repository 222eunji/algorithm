
def dfs(v):
    print(v, end=' ')
    visited_dfs[v] = True
    for i in graph[v]:
        if visited_dfs[i] == False:
            dfs(i)

def bfs(n):
    q = [n]
    visited_bfs[n] = True
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in graph[v]:
            if visited_bfs[i] == False:
                visited_bfs[i] = True
                q.append(i)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
dfs(V)
print()
bfs(V)