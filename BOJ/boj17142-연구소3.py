# 연구소 3
from itertools import combinations
from collections import deque

# 가장 처음에 모든 바이러스는 비활성 상태
# 활성 상태인 바이러스는 상하좌우로 인접한 모든 칸을 동시에 복제, 1초

def dfs(virus_set):
    visited = [[-1]*N for _ in range(N)]
    queue = deque(virus_set)
    
    for virus in virus_set:
        visited[virus[0]][virus[1]] = 0

    time = 0
    while queue:
        virus = queue.popleft()
        vi = virus[0]
        vj = virus[1]
        # 상하좌우
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = vi + di
            nj = vj + dj
            # 범위 안에 있고
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1:
                
                # 빈칸이거나, 비활성 바이러스인 경우
                if grid[ni][nj] == 0 or grid[ni][nj] == 2:
                    # 방문 처리
                    visited[ni][nj] = visited[vi][vj] + 1
                    # 인큐
                    queue.append((ni, nj))
                    # 빈칸인 경우에만 바이러스가 확산되어서
                    if grid[ni][nj] == 0:
                        # 최대 시간 만들기
                        time = max(visited[ni][nj], time)

    # 빈칸인 곳중에 하나라도 방문 안한 곳이 있다면 -> -1 출력
    if any(grid[i][j] == 0 and visited[i][j] == -1 for i in range(N) for j in range(N)):
        return -1
    else:
        return time

    # flag = False
    # for i in range(N):
    #     for j in range(N):
    #         if grid[i][j] == 0:
    #             if visited[i][j] == -1:
    #                 flag = True
    # if flag:
    #     return -1
    # else:
    #     return time


### 입력 ###
# 연구소의 크기, 놓을 수 있는 바이러스의 개수
N, M = map(int, input().split())

virus_position = list()
grid = list()
# 연구소의 상태
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        # 비활성 바이러스의 위치
        if temp[j] == 2:
            virus_position.append((i,j))
    grid.append(temp)


min_time = 1e9
for virus_set in combinations(virus_position, M):
    # 바이러스 부분집합 구하여 조마다 시간을 구함
    time = dfs(virus_set)
    # 시간이 구해진다면
    if time != -1:
        # 가장 작은 시간을 구함
        min_time = min(time, min_time)

# 모든 집합에서 시간이 구해지지 않은 경우엔
if min_time == 1e9:
    # -1을 출력하도록 함
    print(-1)
else:
    print(min_time)