import sys
from itertools import combinations 

# 치킨 집과 집 사이의 거리 구하기
def chicken_to_house(chicken_location, house_location):
    result = 0
    for hx, hy in house_location:
        min_v = float('inf')
        for cx, cy in chicken_location:
            value = abs(hx - cx) + abs(hy - cy)
            if min_v > value:
                min_v = value  # 치킨 집과 집 사이의 거리가 가장 짧은 경우를 저장
        result += min_v 
    return result
     
# 백트래킹 - 조합
def backtracking(chicken_location, house_location, M):
    min_v = float('inf')
    for cc in combinations(chicken_location, M):  # 최대 M개의 치킨집만 남기고 삭제할 것이기 때문에..
        value = chicken_to_house(cc, house_location)  # M개의 치킨집에 대하여 집과 치킨집 사이의 거리를 구함
        if value < min_v:
            min_v = value  
    
    return min_v


N, M = map(int, input().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken_location = list() # 치킨 집 정보
house_location = list() # 집 정보

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:  # 1은 집, 2는 치킨집
            chicken_location.append((i, j))
        elif city[i][j] == 1:
            house_location.append((i, j))

result = backtracking(chicken_location, house_location, M)
print(result)