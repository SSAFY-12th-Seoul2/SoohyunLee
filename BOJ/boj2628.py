width, height = map(int, input().split())

cut_number = int(input())
row_list = []
col_list = []

for _ in range(cut_number):
    a, b = map(int, input().split())
    if a == 0:
        row_list.append(b)
    else:
        col_list.append(b)

row_list.append(0)
row_list.append(height)
col_list.append(0)
col_list.append(width)

row_list.sort()
col_list.sort()

def split_cut(cr_list):
    return [cr_list[i] - cr_list[i-1] for i in range(1, len(cr_list))]


row_list = split_cut(row_list)
col_list = split_cut(col_list)

max_area = max(r*c for r in row_list for c in col_list)

print(max_area)
