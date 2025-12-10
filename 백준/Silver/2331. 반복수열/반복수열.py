import sys
input = sys.stdin.readline

A, P = map(int, input().split())
seq = [A]

idx = 0
while True:
  num = seq[idx]
  v = 0
  # 다음 값 구하기
  while num > 0:
    v += (num%10)**P
    num //= 10

  # 반복 확인하기
  repeat = -1
  for i in range(len(seq)):
    if v == seq[i]:
      repeat = i
  if repeat != -1:
    print(repeat)
    break
  seq.append(v)
  idx += 1

