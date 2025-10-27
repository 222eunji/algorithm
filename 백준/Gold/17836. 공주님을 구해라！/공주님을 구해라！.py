import sys
input = sys.stdin.readline
from collections import deque

# 마왕이 마법의 벽 여러 군데
# t시간 내에 도달해야해
#
# 명검(그람)을 찾으면, 마법의 벽이 있는 칸이라도 단숨에 갈 수 있음
# 그람은 성 어딘가에 반드시 존재,
# 그람이 있는 곳에 도착하면 바로 사용 가능 (부술 수 있는 벽 개수 제한 없음)

# 0은 빈 공간, 1은 마법의 벽, 2는 그람
# T시간 내에 도달하면 최단시간 출력,
# 구출할 수 없다면 'Fail' 출력

N, M, T = map(int,  input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


d = [(1,0), (0,1), (-1,0), (0,-1)]
def bfs():
    visited = [[[False]*M for _ in range(N)] for _ in range(2)]
    q = deque([(0,0,0,0)])  # 상태, r, c, t
    visited[0][0][0] = True
    cnt = 0

    while q:
        cnt += 1
        status, r, c, t = q.popleft()

        if r == N-1 and c == M-1:
            if t <= T:
                return t
            else:
                return 'Fail'

        if t >= T:
            continue

        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and visited[status][nr][nc] == False:
                # 검 획득
                if grid[nr][nc] == 2:
                    q.append((1, nr, nc, t+1))
                    visited[1][nr][nc] = True

                # 상태에 따라 이동 하기
                elif grid[nr][nc] <= status: # 0이면 0만 이동, 검 있으면 0,1,2 다 가능
                    q.append((status, nr, nc, t+1))
                    visited[status][nr][nc] = True

    return 'Fail'

print(bfs())