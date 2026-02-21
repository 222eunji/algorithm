import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]
    dp = list([0, 0, 0] for _ in range(n))
    # 아무 것도 안뗐을 때, 윗행 떼기, 아랫행 떼기 3가지 상태 저장
    dp[0][1], dp[0][2] = score[0][0], score[1][0] # 초기값 세팅

    for i in range(1, n):
        # 윗 행 스티커 뗄 경우
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + score[0][i]
        # 아랫 행 스티커 뗄 경우
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + score[1][i]
        # 둘 다 안뗄 경우
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

    print(max(dp[n-1]))