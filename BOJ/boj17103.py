
# 골드바흐 파티션

import math

array = [False, False] + [True]*(999999)

for i in range(2, int(math.sqrt(1000000))):
    if array[i] == True:
        j = 2
        while i*j <= 1000000:
            array[i*j] = False
            j+=1

T = int(input()) 
for _ in range(T):
    N = int(input()) 
    a = array[2:int(N/2)+1]
    b = array[int(N/2):N-1][::-1]
    cnt = sum([x*y for x, y in zip(a, b)]) 
    print(cnt)