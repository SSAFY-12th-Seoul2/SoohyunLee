# 택배
import sys

# 입력값 처리
n, m = map(int, sys.stdin.readline().split())
# 거리값을 담을 2차원 리스트
dist = [[1e9] * (n+1) for _ in range(n+1)]
# 결과값을 담을 2차원 리스트
result = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    # 입력값 처리
    start, to, weight = map(int, sys.stdin.readline().split())
    # start - to, to - start 각 가중치 값 입력
    dist[start][to] = weight
    dist[to][start] = weight  # 무방향
    result[start][to] = to  # start -> to : start 집하장에서 to 집하장으로 최단 경로를 통해 가기 위햇거는 제일 먼저 to를 지나가야 함
    result[to][start] = start # 무방향
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                print(f'{i}-{k}-{j}')
                dist[i][j] = dist[i][k] + dist[k][j]
                result[i][j] = result[i][k]
             
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print("-", end=" ")
        else:
            print(result[i][j], end=" ")
    print()

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             print("-", end=" ")
#         else:
#             print(dist[i][j], end=" ")
#     print()