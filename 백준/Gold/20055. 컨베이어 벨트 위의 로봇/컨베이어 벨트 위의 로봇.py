import sys
input = sys.stdin.readline
from collections import deque

# 1. **접근 방법**
#     - 문제 이해가 어렵다.
#     - 어떻게 문제를 해석했는지, 어떤 알고리즘을 선택했는지
# 2. **핵심 아이디어**
#     - 시간 복잡도 고려, 자료구조 선택 이유 등
# 3. **시행착오**
# 문제 해석이 어려웠다.
# 1단계부터 벨트를 회전 후, 새로운 로봇을 올려야 하는데, 로봇부터 올리는 것으로 오해했다.

#     - 틀렸던 부분, 디버깅 과정, 실수 기록


# 1. 벨트 회전 (로봇과 함께)
# 2. 가장 먼저 올라간 로봇부터 이동할 수 있다면 이동, 없다면 가만히
# 3. 로봇 이동 조건: 로봇이 없으며, 이동 칸의 내구도가 1 이상
# 4. 올리는 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올림
# 5. 내구도 0인 칸 k개 이상이면 종료, 아니면 1번으로 돌아감
# 종료 되었을 때 몇 단계 진행 중인가


N, K = map(int, input().split())
durability = deque(list(map(int, input().split())))
robot = deque([False]*N)

def belt_move():
    x = durability.pop()
    durability.appendleft(x)
    y = robot.pop()
    robot.appendleft(y)

def robot_move():
    # 내리는 위치는 안봐도 되니까 N-1까지
    for i in range(N-2, -1, -1):    # 인덱스 뒤에서 2번째 부터 이동 시키기 (먼저 들어온 순서로)
        if robot[i]:    # 로봇이 있다면 (뒤에서 2번째 부터 접근, 인덱스 조정으로 각 -1, 총 -2)
            if not robot[i+1] and durability[i+1]:    # 다음 칸에 로봇이 없고, 내구성이 있다면
                robot[i] = False
                robot[i+1] = True   # 로봇 옮기기
                durability[i+1] -= 1  # 옮긴 곳 내구성 1 감소시키기

def remove_robot():
    if robot[N-1]:
        robot[N-1] = False


def put_robot():
    # 내구성이 0이 아니라면, 로봇 올리기
    if durability[0]:
        robot[0] = True
        durability[0] -= 1


rotation = 0
zero_dur = 0
while zero_dur < K:
    rotation += 1
    zero_dur = 0
    # 벨트 회전
    belt_move()
    remove_robot()

    # 로봇 이동
    robot_move()
    remove_robot()

    # 로봇 올리기
    put_robot()

    for v in durability:
        if v == 0:
            zero_dur += 1

print(rotation)