import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_v = float('inf')
max_v = -float('inf')

def recur(i, v, add, sub, mul, div):   # 계산 위치, 현재 값, 남은 연산자 수
    global min_v, max_v

    if i == N:    # 끝까지 도착했다면
        min_v = min(min_v, v)
        max_v = max(max_v, v)
        return

    # 더하기
    if add: # 남아있다면
        recur(i+1, v+num[i], add-1, sub, mul, div)

    # 빼기
    if sub: # 남아있다면
        recur(i+1, v-num[i], add, sub-1, mul, div)

    # 곱하기
    if mul: # 남아있다면
        recur(i+1, v*num[i], add, sub, mul-1, div)

    # 나누기
    if div: # 남아있다면
        if v >= 0:
            recur(i+1, v//num[i], add, sub, mul, div-1)
        else:
            v *= (-1)
            v //= num[i]
            v *= (-1)
            recur(i+1, v, add, sub, mul, div-1)

recur(1, num[0], add, sub, mul, div)
print(max_v)
print(min_v)
