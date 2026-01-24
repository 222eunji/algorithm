import sys
input = sys.stdin.readline

x = int(input())

# 1을 더한다.
# 2로 나누어 떨어지면 2를 곱한다
# 3으로 나누어 떨어지면 3을 곱한다

cnt = [0] * (x+1)
# cnt = [0, 0, 1, 1]
for n in range(2, x+1):
    if n % 6 == 0:
        a = cnt[n//3]
        b = cnt[n//2]
        c = cnt[n-1]
        cnt[n] = min(a, b, c) + 1
    elif n % 3 == 0:
        a = cnt[n//3]
        c = cnt[n-1]
        cnt[n] = min(a, c) + 1
    elif n % 2 == 0:
        b = cnt[n//2]
        c = cnt[n-1]
        cnt[n] = min(b, c) + 1
    else:
        cnt[n] = cnt[n-1] + 1

print(cnt[x])
