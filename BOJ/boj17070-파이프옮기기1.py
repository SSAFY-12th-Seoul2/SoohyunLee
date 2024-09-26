# 파이프 옮기기 1

# 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽이다.

# 파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 
# 파이프는 밀면서 회전시킬 수 있다.
# 회전은 45도만 회전시킬 수 있으며, 
# 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.

# 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 
# 방향은 가로이다. 
# 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.

import sys
sys.stdin = open('boj/input.txt', 'r')



def func(N, house):
    # i, j, 방향을 담을 수 있는 dp 생성
    dp = [[[0 for _ in range(3)] for _ in range(N+1)] for _ in range(N+1)]
    
    # 끝의 위치만 파악하면 됨
    # 기본 시작 조건
    dp[1][2][0] = 1
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if house[i][j] == 1:  # 벽인 경우 건너뛰기
                continue
            
            # 가로 방향으로 올 수 있는 경우의 수
            if j > 1 and house[i][j-1] == 0:
                # 이전 칸의 가로, 대각선의 경우의 수를 합한 값
                dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
            
            # 세로 방향으로 올 수 있는 경우의 수
            if i > 1 and house[i-1][j] == 0:
                # 이전 칸의 세로, 대각선의 경우의 수를 합한 값
                dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
            
            # 대각선 방향으로 올 수 있는 경우의 수
            if i > 1 and j > 1 and house[i-1][j] == 0 and house[i][j-1] == 0 and house[i-1][j-1] == 0:
                # 가로, 세로, 대각선의 경우의 수를 합한 값
                dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
    
    return sum(dp[N][N])

# 입력 처리
N = int(input())
house = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(func(N, house))
