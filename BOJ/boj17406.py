import sys
import copy
from itertools import permutations
N, M, K = map(int, input().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rotate_info = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

# 회전
def rotate_f(grid, rotate):
    r, c, s = rotate
    r -= 1
    c -= 1
    new_grid = copy.deepcopy(grid)

    for i in range(1, s + 1):
        # 위쪽 줄 회전
        for j in range(c - i, c + i):
            new_grid[r - i][j + 1] = grid[r - i][j]
        # 오른쪽 줄 회전
        for j in range(r - i, r + i):
            new_grid[j + 1][c + i] = grid[j][c + i]
        # 아래쪽 줄 회전
        for j in range(c + i, c - i, -1):
            new_grid[r + i][j - 1] = grid[r + i][j]
        # 왼쪽 줄 회전
        for j in range(r + i, r - i, -1):
            new_grid[j - 1][c - i] = grid[j][c - i]

    return new_grid


# 회전 연산의 순서를 이용하여
# 각 행의 합 중 최솟값을 찾아보기
def find_min(n, m, k, grid, rotate_info):
    min_v = float('inf')

    for perm in permutations(rotate_info):
        new_grid = copy.deepcopy(grid)
        for rotate in perm:
            new_grid = rotate_f(new_grid, rotate)
        min_v = min(min_v, min(sum(row) for row in new_grid))

    return min_v

result = find_min(N, M, K, grid, rotate_info)
print(result)