
def find_start():
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'X':
                return (x, y)

# 시계 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향이 같으면(idx) +0
# 다를 경우
# 2로 나눈 나머지가 같으면 +2, 다르면 +1
# 현재위치 (x,y), 현재방향(d) 조작횟수(cnt), 나무자른횟수(cut)
def dfs(x, y, d, cnt, cut):
    global min_cnt
    # 할 일
    if arr[x][y] == 'Y':
        min_cnt = min(min_cnt, cnt)

    # 방문 체크
    visited[x][y] = True

    # 네방향 탐색
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
            # 지나갈 수 있는 길이 거나, 나무 자를 횟수가 남아 있을 경우
            # 리모콘 조작 횟수 카운트
            change = 1
            if d == i:  # 방향이 같을 경우
                pass
            else:   # 방향이 다를 경우
                if d%2 == i%2:  # 상-하 또는 좌-우
                    change += 2
                else:
                    change += 1

            if arr[nx][ny] != 'T':
                dfs(nx, ny, i, cnt + change, cut)
            elif arr[nx][ny] == 'T' and cut < K:
                dfs(nx, ny, i, cnt + change, cut+1)
                
    visited[x][y] = False


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    min_cnt = float('inf')
    x, y = find_start()
    dfs(x, y, 0, 0, 0)
    if min_cnt == float('inf'):
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {min_cnt}')
