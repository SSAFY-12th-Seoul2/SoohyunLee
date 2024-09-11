# 캐슬 디펜스
from collections import deque
from itertools import combinations

def bfs(archer_x, archer_y, grid):
    # BFS 초기화
    queue = deque([(archer_x, archer_y, 0)])
    visited = set([(archer_x, archer_y)])
    
    closest_target = None
    
    while queue:
        x, y, dist = queue.popleft()
        
        if dist > D:
            continue
        
        if grid[x][y] == 1:
            # print(closest_target)
            if closest_target is None or dist < closest_target[2] or (dist == closest_target[2] and y < closest_target[1]):
                closest_target = (x, y, dist)
        
        for dx, dy in [(-1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))
    
    if closest_target:
        return (closest_target[0], closest_target[1])
    return None

def simulate(gungsus):
    total_kill = 0
    copy_grid = [row[:] for row in grid]

    for _ in range(N):  # N번의 턴
        killed = set()
        for gungsu in gungsus:
            target = bfs(N, gungsu, copy_grid)
            if target:
                killed.add((target[0], target[1]))
        
        total_kill += len(killed)
        
        # 죽은 적 제거
        for x, y in killed:
            copy_grid[x][y] = 0
        
        # 적 아래로 이동
        copy_grid = [[0] * M] + copy_grid[:-1]

    return total_kill

# 캐슬 디펜스
N, M, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)] + [[-1] * M]
kill_max = 0

for gungsus in combinations(range(M), 3):
    kill_max = max(simulate(gungsus), kill_max)

print(kill_max)
