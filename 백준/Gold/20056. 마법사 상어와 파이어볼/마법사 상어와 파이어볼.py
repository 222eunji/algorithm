
import sys
input = sys.stdin.readline

# # 입력
# N, M, K (NxN 크기의 격자, 파이어볼 M개 발사)
# 둘째 줄 부터 M개의 줄에 파이어볼 정보 제공
# 파이어볼 정보는 r,c,m,s,d로 구성 (위치r,c 질량m 속도s 방향d)
# 격자는 끝과 끝이 연결되어 있음


# 이동 1회시
# 1. 모든 파이어볼이 자신의 d방향으로 s칸만큼 이동
#     - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수 있음
# 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어 볼이 있는 경우
#     2-1. 같은칸의 파이어볼은 모두 합쳐짐
#     2-2. 파이어볼은 4개의 파이어볼로 나누어짐
#     2-3. 질량은 (합쳐진 파이어볼의 질량의 합)/5
#     2-4. 속력은 (합쳐진 파이어볼의 속력의 합)/(파이어볼의 개수)
#     2-5. 방향은
#         - 합쳐진 파이어볼의 방향이 모두 홀수거나 짝수이 경우: 0,2,4,6
#         - 그 외의 경우: 1,3,5,7
#     2-6. 질량이 0인 파이어볼은 소멸되어 없어진다.
#
# 3. 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.

# 입력
balls_org=[]
N, M, K = map(int, input().split())
for _ in range(M):
    r, c, m, s, d = map(int,input().split())
    r, c = r-1, c-1 # 인덱스 보정
    balls_org.append([r,c, m, s, d])

# 방향
dir = ((-1, 0),(-1, 1),(0, 1),(1, 1),
     (1, 0),(1, -1),(0,-1),(-1,-1))


# 파이어볼 정보는 r,c,m,s,d로 구성 (위치r,c 질량m 속도s 방향d)
# 격자는 끝과 끝이 연결되어 있음
def move(balls_info):
    # 1. 모든 파이어볼이 자신의 d방향으로 s칸만큼 이동
    #     - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수 있음
    for ball in balls_info:
        # print(f'이동 전 {ball}')
        dr, dc = dir[ball[4]]
        speed = ball[3] % N     # GPT가 알려준 팁: N으로 나눈 나머지만큼만 이동 의미 있음
        # 방향과 속도를 고려하여 이동
        ball[0] = (ball[0] + dr * speed) % N
        ball[1] = (ball[1] + dc * speed) % N

    return balls_info


def check_fire(balls_info):
    balls_pos = [list([] for _ in range(N)) for _ in range(N)]
    two_more = set()
    # 파이어 볼 위치 체크
    for ball in balls_info:
        nr, nc = ball[0], ball[1]
        balls_pos[nr][nc].append(ball)
        if len(balls_pos[nr][nc]) >= 2:
            two_more.add((nr, nc))

    return balls_pos, two_more


nxt_dir = ((0,2,4,6), (1,3,5,7))
def two_more_balls_move(balls_pos, two_more):
    new_balls = []
    for r in range(N):
        for c in range(N):
            group = balls_pos[r][c]
            if not group: continue

            if (r,c) not in two_more:
                new_balls.append(group[0])
                continue

            # 2개 이상일 때
            total_m = sum(b[2] for b in group)
            total_s = sum(b[3] for b in group)
            cnt = len(group)

            # 방향 홀짝 판별
            determin_d = [b[4] % 2 for b in group]
            same = (sum(determin_d) == 0) or (sum(determin_d) == cnt)

            m = total_m // 5
            if m == 0:
                continue

            s = total_s // cnt
            next_dirs = nxt_dir[0] if same else nxt_dir[1]

            for nd in next_dirs:
                new_balls.append([r,c,m,s,nd])

    return new_balls

# 3. 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.
def magic(K, balls_org):
    balls = balls_org
    for _ in range(K):
        balls = move(balls)
        balls_pos, two_more = check_fire(balls)    # 파이어볼 2개 이상 있는 곳 위치 체크
        balls = two_more_balls_move(balls_pos, two_more)        # 2개 이상인 곳 나누기
    print(sum(b[2] for b in balls))

magic(K, balls_org)