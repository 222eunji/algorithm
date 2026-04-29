T = int(input().strip())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    answer = 0
    for n in lst:
        if (n % 2):
            answer += n
    print(f'#{tc} {answer}')