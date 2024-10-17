# 최소 스패닝 트리

### 정답 ###
import sys
import heapq

def prim(start):
    # 1. 초기화 : 임의의 정점에서 시작하여 MST 구축을 위한 초기 트리 설정
    mst = set()
    edges = [(0, start)] 
    total_weight = 0

    # 2. 간선 선택, 모든 정점이 MST에 포함될 때까지
    while edges and len(mst) < V:
        weight, node = heapq.heappop(edges)  # 우선순위 큐에서 가장 낮은 가중치를 가진 간선을 꺼냄
        # 해당 간선이 연결하는 정점이 이미 MST에 포함되어 있다면 무시하고 다음 간선을 선택합니다.
        if node not in mst:
            # 그렇지 않다면, 해당 간선과 정점을 MST에 추가합니다.
            mst.add(node)
            total_weight += weight
            # 현재 MST와 연결된 간선 중에서 가중치가 가장 작은 간선을 선택
            for next_node, next_weight in graph[node]:
                if next_node not in mst:
                    # 새로 추가된 정점과 인접한 모든 간선을 우선순위 큐에 삽입합니다.
                    heapq.heappush(edges, (next_weight, next_node))

    return total_weight


V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, to, weight = map(int, sys.stdin.readline().split())
    # 가중치가 있는 무방향 그래프
    graph[start].append((to, weight))
    graph[to].append((start, weight))

print(prim(1))


### 오답 ###
print('------------------------------------------')
# import sys
# import heapq

def prim(start, V):
    heap = []
    MST = set()
    sum_weight = 0
    heapq.heappush(heap, (0, start))

    while heap and len(MST) < V:
        w, s = heapq.heappop(heap)

        if s in MST:
            continue

        MST.add(s)
        sum_weight += w

        # print(graph[s].items())
        for t, ww in graph[s].items():
            if t not in MST:
                heapq.heappush(heap, (ww, t))
    
    # MST의 크기가 V와 다르면 연결되지 않은 그래프
    if len(MST) != V:
        return -1
    
    return sum_weight

# 입력 처리
V, E = map(int, sys.stdin.readline().split())
graph = {i: {} for i in range(1, V+1)}

for _ in range(E):
    start, to, weight = map(int, sys.stdin.readline().split())
    graph[start][to] = weight
    graph[to][start] = weight

# print(graph)
# 결과 출력
result = prim(1, V)
if result == -1:
    print("그래프가 연결되지 않았습니다.")
else:
    print(result)


# 바뀐 점 : dictionary로 바꿈