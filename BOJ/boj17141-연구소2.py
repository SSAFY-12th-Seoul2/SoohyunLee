# 연구소2
from collections import deque
from itertools import combinations

def bfs(virus_set):
    queue = deque(virus_set)
    visited = [[-1] * N for _ in range(N)]

    for i, j in virus_set:
        visited[i][j] = 0

    time = 0
    while queue:
        i, j = queue.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1 and grid[ni][nj] != 1:
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))
                time = max(time, visited[ni][nj])

    for i in range(N):
        for j in range(N):
            if grid[i][j] != 1 and visited[i][j] == -1:  
                return -1
    return time

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

virus_posi = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 2]

min_time = float('inf')
for virus_set in combinations(virus_posi, M):
    time = bfs(virus_set)
    if time != -1:  
        min_time = min(min_time, time)

if min_time == float('inf'):
    print(-1)
else:
    print(min_time)
