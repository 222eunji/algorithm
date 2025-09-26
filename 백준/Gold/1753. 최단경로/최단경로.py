import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    dist = [float('inf')] * (V+1)
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        now_dist, now = heapq.heappop(hq)

        # 이미 더 짧은 경로가 있으면 p패스
        if dist[now] < now_dist:
            continue

        for nxt, w in graph[now]:
            new_dist = now_dist + w
            if dist[nxt] > new_dist:
                dist[nxt] = new_dist
                heapq.heappush(hq, (new_dist, nxt))
    return dist

# 입력
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 실행
dist = dijkstra(K)
for i in range(1, V+1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])
