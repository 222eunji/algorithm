from collections import deque

# 탈출 여부, 얼마나 빨리 탈출할 수 있는지 결정
# 상하좌우 이동
# 불도 번져 !!!!
# 지훈이는 미로의 가장자리에 접한 공간에서 탈출
# 지훈이와 불은 벽이있는 공간은 통과 못해


R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
#-벽 /.-이동가능 / J-지훈이 초기위치, 비면 지나가는 공간 / F-불이난 공간


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_jihun_fire():
    jihun = True
    fire_q = deque([])
    fire_time = [[float('inf')] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if jihun and grid[i][j] == 'J':
                ji, jj = i, j
                jihun = False
            if grid[i][j] == 'F':
                fire_q.append((i, j, 0))
                fire_time[i][j] = 0
    return ji, jj, fire_q, fire_time     # 지훈 i,j 그리고 불 위치


# 불이 이동하는 bfs를 돌려서, 각 칸에 도달하는 시간 계산
def fire_bfs(fire_q, fire_time):
    while fire_q:
        i, j, time = fire_q.popleft()

        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C:
                if grid[ni][nj] != '#' and fire_time[ni][nj] == float('inf'):
                    fire_time[ni][nj] = time+1
                    fire_q.append((ni, nj, time+1))

    return fire_time

def jihun_bfs(ji, jj, fire_time):
    jihun_q = deque([(ji, jj, 0)])
    visited = [[False] * C for _ in range(R)]
    visited[ji][jj] = True

    while jihun_q:
        i, j, time = jihun_q.popleft()

        if i == 0 or i == R-1 or j == 0 or j == C-1:
            return time+1

        for idx in range(4):
            ni, nj = i+d[idx][0], j+d[idx][1]
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
                if grid[ni][nj] != '#':    # 벽이면 통과 못함
                    if time + 1 < fire_time[ni][nj]:
                        visited[ni][nj] = True
                        jihun_q.append((ni, nj, time+1))

    return 'IMPOSSIBLE'

ji, jj, fire_q, fire_time = find_jihun_fire()
fire_bfs(fire_q, fire_time)
print(jihun_bfs(ji, jj, fire_time))
