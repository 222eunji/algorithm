import sys
input = sys.stdin.readline

N = int(input())
p_nums = []
n_nums = []
p_cnt = n_cnt = 0
zero = one = 0

for _ in range(N):
    num = int(input())
    if num == 1:
        one += 1
    elif num == 0:
        zero += 1
    elif num > 1:
        p_nums.append(num)
        p_cnt += 1
    else:
        n_nums.append(num)
        n_cnt += 1

p_nums.sort(reverse=True)
n_nums.sort()

result = one

# ✅ 양수 처리
for i in range(0, p_cnt - 1, 2):
    result += p_nums[i] * p_nums[i + 1]
if p_cnt % 2 == 1:
    result += p_nums[-1]

# ✅ 음수 처리
for i in range(0, n_cnt - 1, 2):
    result += n_nums[i] * n_nums[i + 1]
if n_cnt % 2 == 1 and not zero:
    result += n_nums[-1]

print(result)
