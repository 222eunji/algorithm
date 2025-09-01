def change_distance(direction, distance):
    if direction==1:    # 북
        changed_distance = distance
    elif direction==2:  # 남
        changed_distance = 2*w+h-distance
    elif direction==3:  # 서
        changed_distance = 2*w+2*h-distance
    else:               # 동
        changed_distance = w+distance
    return changed_distance


def cal_min_distance(now, store):
    d1 = abs(now-store)
    d2 = total - d1
    if d1 < d2:
        return d1
    else:
        return d2


w, h = map(int, input().split())
N = int(input())
stores = []
for _ in range(N):
    direction, distance = map(int, input().split())
    stores.append(change_distance(direction, distance))

a, b = map(int, input().split())
now = change_distance(a, b)
total = 2 * (w + h)

sum_v = 0
for store in stores:
    sum_v += cal_min_distance(now, store)

print(sum_v)