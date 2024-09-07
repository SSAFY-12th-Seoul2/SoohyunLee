import sys
from itertools import permutations

N = int(input())
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order_case = tuple(order for order in permutations(range(9), 9) if order[3] == 0)


max_score = 0
for order in order_case:
    total_score = 0
    idx = 0

    for inning in innings:
        score = 0
        out_cnt = 0
        base1, base2, base3 = 0, 0, 0
        
        while out_cnt < 3:
            hitter = order[idx % 9]
            hit_result = inning[hitter]

            if hit_result == 0:  # 아웃
                out_cnt += 1
            elif hit_result == 1:  # 1루타
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif hit_result == 2:  # 2루타
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif hit_result == 3:  # 3루타
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            elif hit_result == 4:  # 홈런
                score += 1 + base1 + base2 + base3
                base1 = base2 = base3 = 0

            idx += 1  # 다음 타자로 이동

        total_score += score
    
    max_score = max(max_score, total_score)
print(max_score)
