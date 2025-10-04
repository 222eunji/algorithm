import sys;
input = sys.stdin.readline

from collections import deque

def solution(N):
    q = deque(range(10))    # 0~9로 시작
    result = []

    while q:
        num = q.popleft()
        result.append(num)

        last_num = num % 10
        for next_num in range(last_num):
            q.append(num*10 + next_num)

        if N+1 == len(result):      # 0부터 시작하기 때문에 +1 하기
            print(result[N])
            return

    print(-1)
    return

N = int(input())
solution(N)
