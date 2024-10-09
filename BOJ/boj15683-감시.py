# 감시

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

cctv = [(grid[i][j], i, j) for i in range(N) for j in range(M) if 1 <= grid[i][j] <= 5]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# CCTV 종류별 감시 방향
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

def watch(x, y, direction, temp):
    # print('감시', direction, x, y)
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or temp[nx][ny] == 6:
                break
            if temp[nx][ny] == 0:
                temp[nx][ny] = '#'

    # for i in range(len(temp)):
    #     print(temp[i])

    # print()

# cctv_idx
def dfs(cctv_idx, grid):
    global blind_spot
    # print('### Dfs', cctv_idx)
    if cctv_idx == len(cctv):
        # print('끝')
        count = sum(row.count(0) for row in grid)
        blind_spot = min(blind_spot, count)
        return

    temp = [row[:] for row in grid]
    cctv_type, x, y = cctv[cctv_idx]
    for direction in directions[cctv_type]:
        # print('----', cctv_type, direction)
        watch(x, y, direction, temp)
        dfs(cctv_idx + 1, temp)
        temp = [row[:] for row in grid] 
        # print(f'백트래킹 {cctv_idx}') 

blind_spot = float('inf')
dfs(0, grid)
print(blind_spot)
