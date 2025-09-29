from collections import deque

# 입력
N, M = map(int, input().split())    # 세로 가로 길이
cheeze = [list((map(int, input().split()))) for _ in range(N)]

# 구현 방법 BFS
# grid BFS는 어떻게 하지
# 델타 탐색 하기..
# 1초당 치즈 녹을때마다 카운트하기 ( 한군데라도 0이 노출되어있을 경우 !!)
d = [(-1 , 0), (1, 0), (0, -1), (0, 1)]
def bfs():
    visited = [[0]*M for _ in range(N)]
    q = deque([(0,0)])
    visited[0][0] = 1
    melt = []

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c +dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = 1
                if cheeze[nr][nc] == 0:  # 공기라면 BFS
                    q.append((nr, nc))
                elif cheeze[nr][nc] == 1:  # 치즈 만나면 녹을 예정
                    melt.append((nr, nc))
    return melt

time = 0
last_cheese = 0

while True:
    melt = bfs()
    if not melt:
        break

    last_cheese = len(melt)
    for r, c in melt:
        cheeze[r][c] = 0
    time += 1


# 출력
# 1. 치즈가 모두 녹아서 없어지는데 걸리는 시간
# 2. 모두 녹기 한 시간 전에 남아 있는 치즈 조각 칸의 개수
print(time)
print(last_cheese)