from collections import deque

# 섬 구분하기
def labeling(x, y, label):
    q = deque([(x, y)])
    map_grid[x][y] = label
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < N and map_grid[nx][ny] == 1:
                map_grid[nx][ny] = label
                q.append((nx, ny))

def clustering(map_grid):
    label = 2
    for i in range(N):
        for j in range(N):
            if map_grid[i][j] == 1:
                labeling(i, j, label)
                label += 1

# 최단 거리 찾기
def find(start_points, label):
    min_distance = 1e9
    q = deque(start_points)
    distance = [[-1]*N for _ in range(N)]
    for sx, sy in start_points:
        distance[sx][sy] = 0

    while q:
        cx, cy = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < N:
                # 바다이면서, 아직 방문하지 않은 곳(다리를 짓지 않은 곳)
                if map_grid[nx][ny] == 0 and distance[nx][ny] == -1:
                    # 다리를 만들고, 거리 + 1
                    distance[nx][ny] = distance[cx][cy] + 1
                    q.append((nx, ny))
                # 그 섬이 내 섬과 다를 경우
                elif map_grid[nx][ny] > 1 and map_grid[nx][ny] != label:
                    min_distance = min(min_distance, distance[cx][cy])          
    
    return min_distance

# 입력
N = int(input())
map_grid = [list(map(int, input().split()))for _ in range(N)]

# 섬 클러스터링
clustering(map_grid)

# 초기값 설정
result = 1e9

# 섬 
for label in range(2, max(map(max, map_grid)) + 1):
    start_points = [(i, j) for i in range(N) for j in range(N) if map_grid[i][j] == label]
    result = min(result, find(start_points, label))

print(result)