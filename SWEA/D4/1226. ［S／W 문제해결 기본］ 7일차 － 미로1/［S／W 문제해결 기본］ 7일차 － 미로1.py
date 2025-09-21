
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    global visited

    # 할일
    if miro[x][y] == 3:
        visited = True
        return

    # 방문 처리
    miro[x][y] = 1

    # 다음 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 16 and 0 <= ny < 16:
            if miro[nx][ny] != 1:
                dfs(nx, ny)


T = 10
for _ in range(T):
    tc = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    visited = False
    dfs(1,1)
    ans = 0
    if visited: # 좌표값 3에 도착하면,
        ans = 1
    print(f'#{tc} {ans}')