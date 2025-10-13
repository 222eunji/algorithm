def solution(info, edges):
    # 트리를 인접 리스트로 만들기
    answer = []
    visited = [False] * len(info)
    
    def dfs(sheeps, wolves):
        if sheeps > wolves:
            answer.append(sheeps)
        else:
            return
        
        for p, c in edges:
            # 부모는 방문하였지만 자식은 방문 안한 경우만 진행
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheeps + 1, wolves)
                else:
                    dfs(sheeps, wolves+1)
                visited[c] = False
    
    # 노드 0은 항상 양이기 때문에
    visited[0] = True
    dfs(1, 0)
    
    return max(answer)
                    
    
#     def dfs(current, sheep, wolf, can_visited):
#         nonlocal max_sheep  # 함수 안의 함수라서 global이 아닌 nonlocal, 테케를 여러번 돌려서 nonlocal 사용하는 것이 안전
#         if info[current] == 0:
#             sheep += 1
#         else:
#             wolf += 1
        
#         # 늑대가 양보다 많으면 종료
#         if wolf >= sheep:
#             return
        
#         max_sheep = max(max_sheep, sheep)
        
#         next_can_visited = can_visited.copy()
#         next_can_visited.remove(current)
        
#         for c in tree[current]:
#             next_can_visited.add(child)
        
#         # 갈 수 있는 모든 노드 탐색
#         for next_node in next_can_visited:
#             dfs(next_node, sheep, wolf, next_can_visited)
    
#     dfs(0, 0, 0, {0})
#     return max_sheep
