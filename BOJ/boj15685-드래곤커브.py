# 드래곤 커브
import sys

# 방향 함수
# 0
# 0 1
# 0 1 2 1
# 0 1 2 1 2 3 2 1

def rotate_direction(lst):
    result_direc_list = lst.copy()
    for d in reversed(lst):
        result_direc_list.append((d + 1) % 4)
    return result_direc_list

# 드래곤 커브의 개수
N = int(sys.stdin.readline())

grid = [[0 for _ in range(101)] for _ in range(101)]

# 방향
direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
direction_list = []


round = 0
while round < N:
    # x, y는 드래곤 커브의 시작점
    # d는 시작 방향, g는 세대
    x, y, d, g = map(int, sys.stdin.readline().split())

    # 시작 점
    grid[y][x] = 1
    
    # 방향 추출
    direction_list=[d]

    # g세대까지 경로 추출
    for _ in range(g):
        direction_list = rotate_direction(direction_list)

    # 경로에 따라 grid에 1로 방문 처리
    for dd in direction_list:
        di, dj = direction[dd]
        x += di
        y += dj
        grid[y][x] = 1

    round += 1

# 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구함
result = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1:
            count = 0
            for di, dj in [[0, 1], [1, 1], [1, 0]]:
                ni = i + di
                nj = j + dj
                if grid[ni][nj] == 1:
                    count += 1

            if count == 3:
                result += 1

print(result)
