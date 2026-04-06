W, M, I = map(int, input().split())

# 1. 여자로 구성할 수 있는 최대 팀
w = W//2
# 2. 남자로 구성할 수 있는 최대 팀
m = M
# 3. 전체 인원 수로 구성할 수 있는 최대 팀
t = (W+M-I)//3

print(min(w, m, t))