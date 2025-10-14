import sys;
input = sys.stdin.readline

# 첫째줄: 회사 직원 n명/최초의 칭찬 회수 m, 직원은 1번부터 n번 까지
# 둘째줄: 직원 n명의 직속 상사 번호, 직속 상사 번호는 자신의 번호 보다 작음, 1번 사장
# m줄: 직속 상사로 부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w

n, m = map(int, input().split())
senior = list(map(int, input().split()))  # 직속 상사 입력 받기
connection_lst = [[] for _ in range(n+1)]   # 직속 부하 관계 리스트
# 직원별 직속 부하 입력
for i in range(1, n):
    connection_lst[senior[i]].append(i+1) # 인덱스+1로 보정 하기

points = [0] * (n+1)    # 칭찬 포인트

for _ in range(m):  # 칭찬해주기
    employee, compliment = map(int, input().split())
    points[employee] += compliment


# dfs로 칭찬 받은 직원들 점수 올리기
# def dfs(empl):
#     for junior in connection_lst[empl]:
#         points[junior] += points[empl]
#         dfs(junior)
def dfs(start):
    stack = [start]
    while stack:
        empl = stack.pop()
        for junior in connection_lst[empl]:
            points[junior] += points[empl]
            stack.append(junior)

dfs(1)

for i in range(1, n+1):
    print(points[i], end=" ")
