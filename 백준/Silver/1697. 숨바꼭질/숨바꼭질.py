from collections import deque

N, K = map(int, input().split())

def hide(N, K):
    queue = deque([(N, 0)])
    visited = [False] * 100_001

    while queue:
        pos, time = queue.popleft()
        if pos < 0 or pos > 100_000:
            continue
        if pos == K:
            return print(time)
        if visited[pos] != 0:   # 이미 방문했다면
            continue

        visited[pos] = time
        queue.append((pos-1, time+1))
        queue.append((pos+1, time+1))
        queue.append((pos*2, time+1))

hide(N, K)