import sys
input = sys.stdin.readline

T = int(input())

def bfs(node):
    global flag
    q = [node]
    mark[node] = 1
    while q:
        # num이 1이라면 나머지는 -1, 반대라면 1
        v = q.pop(0)
        for n in graph[v]:
            if not mark[n]:
                mark[n] = -mark[v]
                q.append(n)
            else:
                if mark[n] == mark[v]:
                    flag = True
                    return

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    mark = [0] * (V+1)
    flag = False

    # 그래프 값 입력
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    
    # 이분 그래프 탐색하기
    for node in range(1, V+1):
        if not mark[node]:
            bfs(node)
            if flag:
                print("NO")
                break
    if not flag:
        print("YES")