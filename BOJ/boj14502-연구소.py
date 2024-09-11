# 연구소

from itertools import combinations
from collections import deque

def virus_diffusion(grid_case, virus_position):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque(virus_position)

    # BFS 시작
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            # 유효한 위치인지 확인
            if 0 <= nx < N and 0 <= ny < M:
                # `0`인 경우만 `2`로 바꾸고 큐에 추가
                if grid_case[nx][ny] == 0:
                    grid_case[nx][ny] = 2
                    queue.append((nx, ny))
    
    return grid_case
                
            

N, M = map(int, input().split())
null_space = []
virus_position = []
grid = []
for i in range(N):
    arr = list(map(int, input().split()))
    virus_position += [(i, j) for j in range(M) if arr[j] == 2]
    null_space += [(i, j) for j in range(M) if arr[j] == 0]
    grid.append(arr)


wall_sets = combinations(null_space, 3)
max_value = 0

for wall in wall_sets:
    grid_case = [g[:] for g in grid]
    for wall_i, wall_j in wall:
        grid_case[wall_i][wall_j] = 1
    
    max_value = max(sum(virus.count(0) for virus in virus_diffusion(grid_case, virus_position)), max_value)
print(max_value)
