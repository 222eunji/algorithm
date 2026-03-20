from collections import deque
import sys;
input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    color[start] = 1

    while q:
        node = q.popleft()

        for next_node in graph[node]:
            if color[next_node] == 0:
                color[next_node] = -color[node]
                q.append(next_node)

            elif color[next_node] == color[node]:
                return False

    return True


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    color = [0] * (V+1)



    for idx in range(1, V+1):
        if color[idx] == 0:
            if not bfs(idx):
                print('NO')
                break
    else:
        print('YES')

