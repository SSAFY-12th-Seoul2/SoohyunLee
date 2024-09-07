# 인구 이동

# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.


# bfs
from queue import deque

# 입력 받기
N, L, R = map(int, input().split())
nation = [list(map(int, input().split())) for _ in range(N)]

# 인접한 두 나라를 탐색하기 위한 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, visited):
    # bfs를 위한 준비 단계
    queue = deque()
    queue.append((x, y))  # 노드 방문(인큐)
    visited[x][y] = True  # 방문 처리

    # 문제에서 필요한 변수
    association = [(x, y)]  # 연합의 초기 노드
    pop_sum = nation[x][y]  # 해당 노드의 인구 값
    
    # 구현
    while queue:
        x, y = queue.popleft() # 디큐

        for i in range(4):
            # 인접 노드 확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 인접한 나라 중에, 인큐 된 적이 없다면!
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 조건 판단
                if L <= abs(nation[x][y] - nation[nx][ny]) <= R:
                    # bfs를 위한 처리
                    queue.append((nx, ny))  # 인큐
                    visited[nx][ny] = True  # 방문 처리

                    # 문제에서 필요한 변수
                    association.append((nx, ny))  # 연합 노드에 추가
                    pop_sum += nation[nx][ny]  # 인구수 누적합
    
    # 연합 인구 재분배(문제에서 요구하는 처리)
    if len(association) > 1:
        new_pop = pop_sum//len(association)
        for i, j in association:
            nation[i][j] = new_pop  # 인구 이동
        return True
    return False


days = 0
while True:
    visited = [[False] * N for _ in range(N)]  # visited 생성

    flag = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:  # 아직 방문하지 않은 노드라면
                if bfs(i, j, visited): 
                    flag = True 
    
    # i, j를 모두 다 돌았는데 인구 이동이 발생하지 않았으면 종료
    if not flag:
        break

    # i, j를 모두 다 돌고 한번이라도 인구 이동이 생겼다면 day += 1
    days += 1

print(days)

    