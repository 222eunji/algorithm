from collections import deque

def find_start_shark(grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                grid[i][j] = 0
                return i, j
    return None

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
def find_fish(shark_size, start_r, start_c):
    visited = [[False] * N for _ in range(N)]

    # 위치(r, c), 이동 횟수
    q = deque([(0, start_r, start_c)])
    visited[start_r][start_c] = True
    candidates = [] # 먹을 수 있는 물고기 후보, 이걸 따로 관리해야 함

    while q:
        dist, r, c = q.popleft()

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                # 이미 방문한 곳은 지나가기
                if visited[nr][nc]:
                    continue

                if fish[nr][nc] <= shark_size:
                    visited[nr][nc] = True
                    q.append((dist+1, nr, nc))
                    if 0 < fish[nr][nc] < shark_size:
                        candidates.append((dist+1, nr, nc))

    if not candidates:  # 물고기 후보가 없다면
        return None

    candidates.sort()
    return candidates[0]

def move_shark():
    r, c = find_start_shark(fish)
    shark_size = 2
    eat_fish = 0
    move_time = 0

    while True:
        result = find_fish(shark_size, r, c)
        if result is None:  # 먹을 물고기가 없음
            return move_time

        dist, r, c = result
        move_time += dist
        eat_fish += 1
        fish[r][c] = 0

        if eat_fish == shark_size:
            shark_size += 1
            eat_fish = 0

N = int(input())
fish = [list(map(int, input().split())) for _ in range(N)]
print(move_shark())
