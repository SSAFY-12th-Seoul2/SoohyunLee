# 나무 재태크
import sys

def spring(grid):
    total_death_trees = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(grid[i][j][1]) > 0:
                # 나이가 어린 순으로
                grid[i][j][1].sort()
                amount = grid[i][j][0]
                trees = list()
                death_trees = list()
                for tree_age in grid[i][j][1]:
                    if grid[i][j][0] >= tree_age:
                        grid[i][j][0] -= tree_age
                        trees.append(tree_age + 1)
                    else:
                        death_trees.append(tree_age)


                    # 틀린 조건
                    # if (amount - tree_age) < 0:
                    #     death_trees.append(tree_age)
                    # else:
                    #     grid[i][j][0] -= tree_age
                    #     new_tree_age = tree_age + 1
                    #     trees.append(new_tree_age)

                    # 둘의 차이
                    # 비교 방식 : 양분과 나무 나이를 직접 비교 / 양분에서 나무 나이를 뺀 결과가 음수인지
                    # 여기서 amount가 갱신되지 않고 있음
                    
                grid[i][j][1] = trees
                total_death_trees[i][j] = death_trees

    return grid, total_death_trees

def summer(grid, total_death_trees):
    for i in range(N):
        for j in range(N):
            if len(total_death_trees[i][j]) > 0:
                for death_tree in total_death_trees[i][j]:
                    new_amount = death_tree // 2
                    grid[i][j][0] += new_amount

    return grid

def fall(grid):
    for i in range(N):
        for j in range(N):
            if len(grid[i][j][1]) > 0:
                for tree in grid[i][j][1]:
                    if tree % 5 == 0 :
                        for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1],
                                       [-1, -1], [-1, 0], [-1, 1]]:
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < N and 0 <= nj < N:
                                grid[ni][nj][1].append(1)
    return grid

def winter(grid):
    for i in range(N):
        for j in range(N):
            new_amount = A_grid[i][j]
            grid[i][j][0] += new_amount

    return grid


def simulate(grid):
    spring_grid, death_trees = spring(grid)
    summer_grid = summer(grid, death_trees)
    fall_grid = fall(summer_grid)
    winter_grid = winter(fall_grid)

    return winter_grid


N, M, K = map(int, sys.stdin.readline().split())

grid = [[[5, []] for _ in range(N)] for _ in range(N)]

# N개의 줄에 A 배열의 값
A_grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# M개 줄에 상도가 심은 나무의 정보 (위치 x, 위치 y, 나이)
for _ in range(M):
    x, y, age = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    grid[x][y][1].append(age)


for _ in range(K):
    grid = simulate(grid)

print(sum(len(grid[i][j][1]) for i in range(N) for j in range(N) if len(grid[i][j][1]) > 0))
