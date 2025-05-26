from collections import deque # bfs (append, popleft)
# deque : 양방향 큐

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

# Graph 구현 방법 : 링크드 리스트, 2차원 배열, 딕셔너리

# 깊이 우선 탐색 depth first search
def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A') + i), end=' ')

    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)


# 너비 우선 탐색 breadth first search -> sns나 네트워크 탐색에서 많이 사용
def bfs(g, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        i = queue.popleft()
        print(chr(ord('A') + i), end=' ')
        for j in range(len(g)):
            if g[i][j] == 1 and not visited[j]:
                visited[j] = 1
                queue.append(j)


visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 6, visited_dfs)
print()
bfs(graph, 4, visited_bfs)