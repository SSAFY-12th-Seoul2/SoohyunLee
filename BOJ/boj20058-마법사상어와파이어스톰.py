# 마법사 상어와 파이어스톰
import sys
from queue import deque
N, Q = map(int, input().split())  # 격자 사이즈를 위한 변수/Q번 시전
grid_size = 2 ** N
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(grid_size)]
L_list = list(map(int, sys.stdin.readline().split()))

# 파이어스톰
# 파이어스톰은 먼저 격자를 2L × 2L 크기의 부분 격자로 나눈다.
# 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
# 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.

def rotate(grid, x, y, size):
    for i in range(size // 2):
        for j in range(i, size - i - 1):
            temp = grid[x + i][y + j]
            grid[x + i][y + j] = grid[x + size - 1 - j][y + i]
            grid[x + size - 1 - j][y + i] = grid[x + size - 1 - i][y + size - 1 - j]
            grid[x + size - 1 - i][y + size - 1 - j] = grid[x + j][y + size - 1 - i]
            grid[x + j][y + size - 1 - i] = temp

for L in L_list:
    subset_size = 2 ** L
    # 부분 격자 시작점
    for x in range(0, grid_size, subset_size):
        for y in range(0, grid_size, subset_size):
            rotate(grid, x, y, subset_size)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    melt = []
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] > 0:
                cnt = sum(1 for d in range(4) if 0 <= x + dx[d] < grid_size and 0 <= y + dy[d] < grid_size and grid[x + dx[d]][y + dy[d]] > 0)
                if cnt < 3:
                    melt.append((x, y))  # 얼음이 있는 칸이 3칸 미만이라면 해당 칸은 얼음의 양이 1 줄어들어야 함.
    
    # 조건에 해당하는 얼음들
    for x, y in melt:
        grid[x][y] -= 1


# 출력
# 남아있는 얼음 A[r][c]의 합
# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 
# 덩어리는 연결된 칸의 집합이다.

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx][ny] > 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt

# 남아있는 얼음
sum_ice = 0
# 가장 큰 덩어리 칸의 개수
cnt_ice = 0
visited = [[False] * grid_size for _ in range(grid_size)]
for x in range(grid_size):
    for y in range(grid_size):
        if grid[x][y] > 0:
            sum_ice += grid[x][y]
            if not visited[x][y]:
                cnt_ice = max(cnt_ice, bfs(x, y, visited))

print(sum_ice)
print(cnt_ice)