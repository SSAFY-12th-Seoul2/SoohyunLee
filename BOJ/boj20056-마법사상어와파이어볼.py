# 마법사 상어와 파이어볼

import sys

# N 격자크기 M개의 파이어볼 발사
N, M, K = map(int, sys.stdin.readline().split())

# 8개의 방향
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

# i번의 파이어볼의 위치는 r, c, 질량은 m, 방향은 d, 속력은 s
balls = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]


# K번의 이동
for _ in range(K):
    # 모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동
    # 이동하는 중에 같은 칸에 여러 개의 파이어볼이 있을 수 있다.

    # 격자판
    grid = [[[] for _ in range(N)] for _ in range(N)]
    for r, c, m, s, d in balls:
        # 이동
        r -= 1
        c -= 1
        nr = (r + directions[d][0] * s) % N
        nc = (c + directions[d][1] * s) % N
        grid[nr][nc].append([m, s, d])  # 질량, 속력, 방향 저장

    
    balls = []
    for r in range(N):
        for c in range(N):
            if len(grid[r][c]) == 1:  # 파이어볼이 한 개
                balls.append([r, c] + grid[r][c][0])
            elif len(grid[r][c]) >= 2:  # 파이어볼이 두개 이상인 경우
                sum_m = sum(info[0] for info in grid[r][c])  # 질량 합
                sum_s = sum(info[1] for info in grid[r][c])  # 속력 합
                cnt = len(grid[r][c])  # 개수

                new_m = sum_m // 5  # 질량 계산
                new_s = sum_s // cnt  # 속력 계산

                odd = all(info[2] % 2 == 1 for info in grid[r][c])  # 모두 홀수인가?
                even = all(info[2] % 2 == 0 for info in grid[r][c])  # 모두 짝수인가?

                if new_m > 0:   # 질량이 0인 건 소멸
                    if odd or even:  # 모두 홀수이거나 모두 짝수이면
                        new_d = [0, 2, 4, 6]  # 방향
                    else:
                        new_d = [1, 3, 5, 7]  # 그렇지 않으면의 방향
                    
                    for nd in new_d:
                        balls.append([r, c, new_m, new_s, nd])   # 위치, 질량, 속력, 방향 저장

result = sum(info[2] for info in balls)
print(result)
