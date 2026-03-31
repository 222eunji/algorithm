import sys
input = sys.stdin.readline
N = int(input())
score = []
for _ in range(N) :
  name, kor, en, math = input().split()
  score.append((int(kor),int(en), int(math), name))

score.sort(key = lambda x:(-x[0], x[1], -x[2], x[3]))

for i in range(N):
  print(score[i][3])