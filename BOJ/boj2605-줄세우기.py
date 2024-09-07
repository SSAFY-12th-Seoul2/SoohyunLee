
# 줄 세우기

T = int(input())
lst = list(map(int, input().split()))
new_lst = []
for ind, value in enumerate(lst):
    new_ind = ind-value
    new_lst.insert(new_ind, ind+1)

for num in new_lst:
    print(num, end=" ")