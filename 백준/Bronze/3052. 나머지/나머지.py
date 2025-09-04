nums = [0] * 10
rests = [0] * 42    # 41 인덱스 까지 사용
cnt = 0
# 입출력
for i in range(10):
    nums[i] = int(input())

for num in nums:
    if rests[num % 42] == 0:
        rests[num % 42] += 1
        cnt += 1

print(cnt)