import sys;
input = sys.stdin.readline
from collections import deque

N = int(input())    # 컴퓨터의 수 (노드의 수)
E = int(input())    # 연결 개수 (간선의 수)
graph = [[] for _ in range(N+1)]
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node):
    visited = [False] * (N+1)
    q = deque([node])

    while q:
        n = q.popleft()
        visited[n] = True   # 방문 처리

        for next in graph[n]:   # 인접 노드 방문
            if visited[next]:
                continue
            q.append(next)

    result = 0
    for i in range(2, N+1):
        if visited[i]:
            result += 1

    print(result)

bfs(1)