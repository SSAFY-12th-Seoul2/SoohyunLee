# 마법사 상어와 비바라기

import sys
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
d_info = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]  # 이동의 정보

# 8방향
direction = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
# 4방향 - 대각선 탐색 용
dx4 = [-1, -1, 1, 1]
dy4 = [-1, 1, 1, -1]

# 첫 구름의 위치
clouds = set([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

for d, s in d_info:
    d -= 1
    dx, dy = direction[d]

    # 이동 후의 새로운 구름 위치를 저장
    new_clouds = set()

    # 모든 구름의 위치를 이동시킴
    for ci, cj in clouds:
        ni = (ci + dx * s) % N
        nj = (cj + dy * s) % N
        new_clouds.add((ni, nj))
        arr[ni][nj] += 1  # 이동한 구름의 위치에서 물의 양 1씩 증가
    
    for ci, cj in new_clouds:
        # 구름 하나 선정해서 대각선 탐색
        cnt = 0
        for j in range(4):
            ni = ci + dx4[j]
            nj = cj + dy4[j]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                cnt += 1
        arr[ci][cj] += cnt  # 양수인 값을 가진 대각선 개수를 더해줌
    
    # 이제 구름이 있었던 칸을 제외한 나머지 칸 중에서 물의 양이 2이상인 칸을 탐색
    clouds = set()  # 다음 구름 위치를 위해 빈 세트 생성
    for i in range(N):
        for j in range(N):
            if (i, j) not in new_clouds and arr[i][j] >= 2:
                arr[i][j] -= 2
                clouds.add((i, j))

print(sum([a for ar in arr for a in ar]))
