# 미세먼지 확산

def dust(grid, R, C):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    new_grid = [[0]*C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                value = grid[i][j] // 5
                cnt = 0
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1:
                        new_grid[ni][nj] += value
                        cnt += 1
                new_grid[i][j] += grid[i][j] - (value * cnt)
            elif grid[i][j] == -1:
                new_grid[i][j] = -1
    
    return new_grid

# 공청기 가동
def clean(cleaner, direction, grid, R, C):
    # 위에 있는 공청기
    if direction == 'up':
        for i in range(cleaner - 1, 0, -1):
            grid[i][0] = grid[i-1][0]
        for i in range(C-1):
            grid[0][i] = grid[0][i+1]
        for i in range(cleaner):
            grid[i][C-1] = grid[i+1][C-1]
        for i in range(C-1, 1, -1):
            grid[cleaner][i] = grid[cleaner][i-1]
        grid[cleaner][1] = 0
    
    # 아래에 있는 공청기
    elif direction == 'down':
        for i in range(cleaner + 1, R - 1):
            grid[i][0] = grid[i+1][0]
        for i in range(C-1):
            grid[R-1][i] = grid[R-1][i+1]
        for i in range(R-1, cleaner, -1):
            grid[i][C-1] = grid[i-1][C-1]
        for i in range(C-1, 1, -1):
            grid[cleaner][i] = grid[cleaner][i-1]
        grid[cleaner][1] = 0

R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

# 공청기 위치 찾기
for i in range(R):
    if grid[i][0] == -1:
        cleaner_up = i
        cleaner_down = i + 1
        break

for _ in range(T):
    grid = dust(grid, R, C)  # 미세먼지 확산
    clean(cleaner_up, 'up', grid, R, C)  # 위쪽 공기청정기 작동
    clean(cleaner_down, 'down', grid, R, C)  # 아래쪽 공기청정기 작동

# 남은 미세먼지 합산
result = sum([g for gr in grid for g in gr if g > 0])
print(result)