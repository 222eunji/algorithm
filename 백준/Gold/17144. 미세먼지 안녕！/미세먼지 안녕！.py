import sys;
input = sys.stdin.readline

# R, C, T
# R개의 줄에 Arc
# 공기청정기가 설치된 곳은 Arc가 -1
# 나머지는 미세먼지의 양
# 공기청정기는 가장 아랫행, 윗행과 두칸 이상 떨어짐

# 집의 크기 R*C (행,열)
# 공기청정기는 항상 1번 열, 크기는 두행
#
# 1. 미세먼지 확산
# - 동시에, 인접한 4방향으로 확산 (1/5)씩 나눠주고, 남은건 그대로
# 2. 공기청정기 작동
# - 공기청정기는 바람이 나와
# - 위쪽은 반시계방향으로 순환, 아래쪽은 시계방향으로 순환
# - 바람이 불면 미세먼지가 바람의 방향대로 모두 한칸씩 이동
# - 공기청정기로 들어간 미세먼지는 모두 정화
# T초가 지난 후 남아있는 미세먼지의 양

# 1. 미세먼지 확산 함수
# - True/False가 있는 grid를 만들어 원래 먼지가 있는 위치들 관리
# - True일때마다 4방향으로 미세먼지 퍼트리기
#     - 인덱스 체크, -1아닌지 체크
#     - 1/5로 나누고, 이동한 먼지만큼 현재 위치에서 빼기
#
# 2. 공기청정기 실행 함수
# - 윗쪽행에서 우,상,좌,하로 먼지 이동시키기 (반대로)
# - 아랫쪽행에서 우,하,좌,상으로 먼지 이동시키기 (반대로)
# - 먼지 다음 이동이 -1이면 먼지 제거하기

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

# 0. 공기 청정기 위치 찾기
def find_air_purifier():
    for r in range(R):
        if room[r][0] == -1:
            return r


# 1. 미세 먼지 확산 함수
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def fine_dust():
    # 처음 존재 하는 미세 먼지 위치 체크
    dust_exist = [[(False, 0) for _ in range(C)] for _ in range(R)]
    # dust_exist = [[False, 0]*R for _ in range(C)]
    for i in range(R):
        for j in range(C):
            if room[i][j] >= 1:
                dust_exist[i][j] = (True, room[i][j])

    for i in range(R):
        for j in range(C):
            if dust_exist[i][j][0]:    # 미세먼지가 존재할 때
                share_dust = dust_exist[i][j][1] // 5
                share_cnt = 0
                for di, dj in d:    # 4방향으로 퍼트리기
                    ni, nj = i+di, j+dj
                    # 인덱스 체크, -1아닌지 체크
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        room[ni][nj] += share_dust
                        share_cnt += 1
                room[i][j] -= share_dust*share_cnt


# 2. 공기청정기 실행 함수
up_d = [(-1,0), (0,1), (1,0), (0,-1)]
down_d = [(1,0),(0,1),(-1,0),(0,-1)]
def run_air_purifier(start_r):
    # start_r:  공기청정기 상단 위치

    # 윗쪽 행 공기 청정기 동작
    r, c = start_r-1, 0
    for i in range(4):
        while True:
            nr, nc = r+up_d[i][0], c+up_d[i][1]
            if 0 <= nr < start_r+1 and 0 <= nc < C and room[nr][nc] != -1:
                room[r][c] = room[nr][nc]
                r, c = nr, nc
            else:
                if i == 3 and room[nr][nc] == -1:
                    room[r][c] = 0
                break

    # 아랫쪽 행 공기 청정기 동작
    r, c = start_r+2, 0
    for i in range(4):
        while True:
            nr, nc = r+down_d[i][0], c+down_d[i][1]
            if start_r+1 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                room[r][c] = room[nr][nc]
                r, c = nr, nc
            else:
                if i == 3 and room[nr][nc] == -1:
                    room[r][c] = 0
                break



start_r = find_air_purifier()
# T초 동안 실행
for _ in range(T):
    fine_dust()
    run_air_purifier(start_r)

# 공기청정기 값 -1,-1 미리 더하기
total = 2
for i in range(R):
    total += sum(room[i])

print(total)