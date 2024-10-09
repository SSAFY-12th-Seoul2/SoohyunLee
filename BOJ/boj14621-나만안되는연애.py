# 찾기 : 원소가 속한 집합의 대표 원소(또는 루트)를 찾음
def find(parent, i):
    if parent[i] == i:  # i 자기 자신이 i를 바라본다 = 해당 집합의 대표자를 찾았다.
        return i
    parent[i] = find(parent, parent[i])  # 경로 압축
    return parent[i]  # i의 부모가 가리키고 있는 정점부터 다시 대표자를 탐색

# 합집합 : 두 개의 집합을 합쳐서 하나의 집합으로 만듦
def union(parent, rank, x, y):
    # x 와 y 의 대표자를 찾자.
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:  # 이미 같은 집합이면 끝
        return

    # rank를 비교하여 더 작은 트리를 큰 트리 밑에 병합
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        # rank가 같으면 한쪽을 다른 쪽 아래로 병합하고 rank를 증가시킴
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # 가중치(거리) 기준으로 정렬
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    mst_weight = 0
    cnt = 0

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v): # 싸이클이 없다면
            cnt += 1
            union(parent, rank, u, v)
            mst_weight += weight
            if cnt == n - 1:  # n-1개의 엣지를 가진 최소 신장 트리를 완성했을 때
                return mst_weight

    return -1

# 학교의 수, 학교를 연결하는 도로의 개수
N, M = map(int, input().split())
# 남초 대학교면 M, 여초 대학교면 W
gender = [""] + input().split()
# u학교와 v학교가 연결되어 있으며 이 거리는 d
edges = []
for _ in range(M):
    u, v, d = map(int, input().split())
    # gender[u]와 gender[v]가 같으면 두 학교는 같은 성별이므로 continue
    if gender[u] == gender[v]:
        continue
    edges.append((u, v, d))
    
print(kruskal(N, edges))

