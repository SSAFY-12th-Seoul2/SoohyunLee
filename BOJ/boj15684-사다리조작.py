import sys
from itertools import combinations

# 사다리 타기 게임
def ghost_leg(grid):
    for start in range(N):
        cp = start  # cp = current position 현재 위치
        for i in range(H):
            # 오른쪽에 가로선이 있으면 이동
            if cp < N - 1 and grid[i][cp] == 1:
                cp += 1
            # 왼쪽에 가로선이 있으면 이동
            elif cp > 0 and grid[i][cp - 1] == 1:
                cp -= 1
        # 시작위치랑 최종 위치가 다르면 False
        if cp != start:
            return False
    return True


# 시뮬레이션 함수 = 사다리를 추가하고 사다리 타기 게임을 수행
def simulate(grid, subset):
    # grid 복사
    grid_copy = [row[:] for row in grid]
    # 사다리를 추가함
    for i, j in subset:
        grid_copy[i][j] = 1
    return ghost_leg(grid_copy)


# 입력
N, M, H = map(int, sys.stdin.readline().split())
# H * (N-1) 그리드 만들기
grid = [[0] * (N - 1) for _ in range(H)]


for _ in range(M):
    # a = 1, b = 2
    # 1번과 2번 세로선 사이에 2번째 줄에 사다리를 둠
    # -> grid[0][1]에 사다리가 있음을 1로 표현
    a, b = map(int, sys.stdin.readline().split())
    grid[a - 1][b - 1] = 1

min_value = float('inf')

# 사다리를 둘 수 있는 후보
candidates = []
for i in range(H):
    for j in range(N - 1):
        if grid[i][j] == 0:
            if (j == 0 or grid[i][j - 1] == 0) and (j == N - 2 or grid[i][j + 1] == 0):
                candidates.append((i, j))

# 다리를 추가로 놓지 않은 경우 확인
# FALSE면 ELSE로
if ghost_leg(grid):
    min_value = 0
else:
    # 1개~3개까지 둘 수 있음
    for h in range(1, 4):
        for subset in combinations(candidates, h):
            # 사다리를 추가하고 사다리 타기게임 수행
            # True 찾으면 break (1,2,3)중 최소값 찾기 때문
            if simulate(grid, subset):
                min_value = min(min_value, h)
                break

if min_value == float('inf'):
    print('-1')
else:
    print(min_value)