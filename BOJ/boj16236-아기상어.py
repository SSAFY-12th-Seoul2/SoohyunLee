# 아기상어
import sys
from collections import deque
sys.stdin = open('boj/input.txt', 'r')

## 문제 ## 
# N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다.
# 한 칸에는 물고기가 최대 1마리 존재한다.

# 가장 처음에 아기 상어의 ""크기""는 2이고
# 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 ""이동""한다.

# 제약 : 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
# 제약2 : 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
# 제약3 : 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

## 제약 정리 ## 
# 이동 제약 : 아기 상어의 크기보다 큰 칸은 못지나감 (같음 이동 허용)
# 먹이 제약 : 아기 상어의 크기보다 작은 물고기만 먹을 수 있음 (같은 크기 먹지 못함)

## 이동 결정 ##
# 더 먹을 곳 없으면 엄마에게 도움 요청
# 먹을 수 있는 물고기가 1마리 => 먹으러 감
# 먹을 수 있는 물고기가 1마리 초과 => 거리가 가장 가까운 물고기 먹으러감
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나가야 하는 칸의 개수의 "최솟값" => 최단 경로 BFS
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러 마리라면, 가장 왼쪽에 있는 물고기.

# 결과 : 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아 먹을 수 있는지.

# BFS를 이용해서 아기 상어의 이동과 물고기 탐색 구현
def bfs(si, sj):
    ## 준비 ##
    # visited 생성(거리와 함께 체크)
    # -1은 방문을 안 한 것으로 함
    dist = [[-1] * n for _ in range(n)]
    # 큐 생성, 시작점 인큐
    q = deque([(si, sj)])
    # 시작점 방문표시(거리)
    # 시작점이니깐 거리 = 0
    dist[si][sj] = 0
    fish = []

    ## 탐색 ## 
    while q:
        i, j = q.popleft()  # 큐의 첫 번째 원소 반환
        # print('현재 위치:', i, j)
        # 상, 우, 하, 좌
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]: 
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] == -1:  # 아직 방문되지 않은 곳이라면
                # 이동 제약 : 아기 상어의 크기보다 큰 칸은 못지나감 (나머지는 이동 가능)
                if grid[ni][nj] <= baby_size : 
                    dist[ni][nj] = dist[i][j] + 1  # 방문 처리
                    q.append((ni, nj))
                    # 먹이 제약 : 아기 상어의 크기보다 작은 물고기만 먹을 수 있음 (같은 크기 먹지 못함)
                    # 0은 빈칸
                    if 0 < grid[ni][nj] < baby_size:
                        fish.append((dist[ni][nj], ni, nj))  # 먹을 수 있는 물고기 리스트 

    if not fish:
        return None
    # fish.sort(key = lambda x : (x[0], x[1], x[2]))  # 먹을 수 있는 물고기가 1마리 이상인 경우, 거리의 최솟값
    # print(fish)
    # return fish[0]
    return min(fish)


# 공간의 크기
n = int(input())
# 공간의 상태
grid = [0] * n
si = sj = -1
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 9:
           # 아기상어의 위치
           si, sj = i, j
           temp[j] = 0 # 아기 상어가 있는 자리를 빈칸으로 초기화
    grid[i] = temp


baby_size = 2
eat = 0  
move_cnt = 0  # time 
while True:
    result = bfs(si, sj) # 현재 아기상어의 위치에서 가장 가까운 곳에 있는 먹이 위치를 찾아줌
    if result is None:
        break

    dist, ni, nj = result
    # print(dist, ni, nj)
    move_cnt += dist
    eat += 1
    grid[ni][nj] = 0  # 물고기를 먹으면, 그 칸은 빈칸이 됨
    si, sj = ni, nj   # 해당 자리에서 다시 먹이 탐색

    if eat == baby_size: # 크기가 2인 아기상어는 물고기 2마리를 먹으면 크기가 3이 됨
        baby_size += 1
        eat = 0

print(move_cnt)
