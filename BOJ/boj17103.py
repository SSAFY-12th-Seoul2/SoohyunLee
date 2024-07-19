import math
# N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.
array = [False, False] + [True]*(1000001)

# 소수 array 생성(소수면 True)
for i in range(2, int(math.sqrt(1000001))):
    if array[i] == True:
        j = 2
        while i*j <= 1000000:
            array[i*j] = False
            j+=1

T = int(input()) # 테스트 케이스
for _ in range(T):
    N = int(input()) # 짝수
    a = array[2:int(N/2)+1]
    b = array[int(N/2):N-1][::-1]
    cnt = sum([x*y for x, y in zip(a, b)]) # 둘 다 소수이면 True, List만들어서 Sum
    print(cnt)