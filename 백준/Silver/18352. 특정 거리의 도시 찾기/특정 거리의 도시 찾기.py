import sys
input = sys.stdin.readline
from collections import deque

# 모든 가중치 동일, 최단 거리 => bfs
# 도시의 개수 N, 도로의 개수 M, 거리의 정보 K, 출발 도시의 번호 X

# 1. bfs 탐색
# 2. 최단 거리가 K인 도시 번호 오름차순 출력, 존재하지 않으면 -1

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)

answer = []

def bfs(node, distance):
    visited = [False] * (N + 1)
    q = deque([(node, distance)])
    visited[node] = True

    while q:
        v, d = q.popleft()

        if d == K:
            answer.append(v)

        elif d < K:
            for nxt in graph[v]:
                if visited[nxt]:
                    continue
                q.append((nxt, d+1))
                visited[nxt] = True

bfs(X, 0)
answer.sort()
if answer:
    for x in answer:
        print(x)
else:
    print(-1)
