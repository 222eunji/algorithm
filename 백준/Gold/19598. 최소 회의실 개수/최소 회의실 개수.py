import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
meetings = []
for _ in range(N):  # 입력 받기
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort()

rooms = []
for s, e in meetings:
    if rooms and rooms[0] <= s:
        heappop(rooms)  # 첫번째 시간 빼고
    heappush(rooms, e)

print(len(rooms))
