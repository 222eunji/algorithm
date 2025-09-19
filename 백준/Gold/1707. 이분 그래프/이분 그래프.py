from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, color):
    q = deque([start])
    visited[start] = color

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if visited[nxt] == 0:  # 아직 방문 안 함
                visited[nxt] = -visited[now]  # 반대 색깔
                q.append(nxt)
            elif visited[nxt] == visited[now]:  # 같은 색이면 이분 그래프 X
                return False
    return True


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (V+1)  # 0=방문X, 1=빨강, -1=파랑
    result = True

    for i in range(1, V+1):
        if visited[i] == 0:
            if not bfs(i, 1):
                result = False
                break

    print("YES" if result else "NO")
