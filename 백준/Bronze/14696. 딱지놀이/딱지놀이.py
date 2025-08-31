def solution(A, B):
    # A, B 딱지 값 리스트에 정렬 하기
    A_card = [0] * 5
    for i in range(1, len(A)):
        A_card[A[i]] += 1
    B_card = [0] * 5
    for i in range(1, len(B)):
        B_card[B[i]] += 1


    # 결과 판정 하기
    for i in range(4, 0, -1):
        if A_card[i] > B_card[i]:
            return 'A'

        elif A_card[i] < B_card[i]:
            return 'B'

        else:
            continue
    else:
        return 'D'


T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(solution(A, B))

