import sys;
input = sys.stdin.readline


# 사람의 수 N,
# 진실을 아는 사람,
# 각 파티에 오는 사람들의 번호,
#
# 지민이는 모든 파티에 참가
# 거짓말 쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티의 개수 최댓값

# 입력
N, M = map(int, input().split())
temp = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(M)]


# 0명 이상일 때 카운트하는 함수 구하기
def solution():
    # 진실을 아는 사람 / 알게될 사람 표시 하기 (True, 모르면 False)
    party_people = [False] * (N+1)

    # 파티에 연결된 사람들 구하기
    person_connection = [[] for _ in range(N + 1)]
    for party in parties:
        party_person_total = party[0]
        for i in range(1, party_person_total):
            for j in range(i + 1, party_person_total + 1):
                person_connection[party[i]].append(party[j])
                person_connection[party[j]].append(party[i])

    # 진실을 아는 사람과, 연관된 사람 모두 True 처리 하기
    for i in temp[1:]:
        party_people[i] = True
        # for friend in person_connection[i]:
        #     party_people[friend] = True
    # 변롸가 없을 때 까지 반복 (Claude 도음)
    changed = True
    while changed:
        changed = False
        for i in range(1, N+1):
            if party_people[i]:
                for friend in person_connection[i]:
                    if not party_people[friend]:
                        party_people[friend] = True
                        changed = True

    result = 0
    # 모르는 사람들만 있는 파티 개수 카운트하기
    for party in parties:
        for man in party[1:]:
            if party_people[man]:  # 진실을 아는 사람이 나온다면 그 파티는 거짓말 할 수 없음
                break
        else:
            result += 1

    return result


# 아는 사람이 없을 때, 모든 파티에서 거짓말 가능
if temp[0] == 0:
    print(M)
# 사람이 0명 이상일 때
else:
    print(solution())
