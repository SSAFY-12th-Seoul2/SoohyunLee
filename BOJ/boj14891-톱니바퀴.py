def discriminant(cogwheels, wheel_num):
    sn_state = [True] * 3
    for idx in range(3):
        if cogwheels[idx][2] != cogwheels[idx+1][6]:
            sn_state[idx] = False

    sn_state.insert(wheel_num, False)
    return sn_state

def rotate(wheel_num, direction):
    global cogwheels
    temp = cogwheels[wheel_num]
    if direction == 1:
        cogwheels[wheel_num] = [temp[-1]] + temp[:-1]
    else:
        cogwheels[wheel_num] = temp[1:] + [temp[0]]


def score_func(cogwheels):
    score = 0
    for i in range(4):
        state = cogwheels[i][0]
        if state == 1:
            score += 2**i
    return score


cogwheels = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())
rotation_plan = [list(map(int, input().split())) for _ in range(K)]

for wheel_num, direction in rotation_plan:
    wheel_num -= 1
    sn_state = discriminant(cogwheels, wheel_num)
    rotate(wheel_num, direction)
    
    # 왼쪽
    left_direction = direction
    right_direction = direction
    for num in range(wheel_num-1, -1, -1):
        if 0 <= num < 4 and not sn_state[num]:
            rotate(num, -left_direction)
            left_direction = -left_direction
        else:
            break
    # 오른쪽
    for num in range(wheel_num+1, 4):
        if 0 <= num < 4 and not sn_state[num]:
            rotate(num, -right_direction)
            right_direction = -right_direction
        else:
            break
            
result = score_func(cogwheels)
print(result)

###############################

def rotate(wheel, direction):
    return wheel[-direction:] + wheel[:-direction]

def score_func(cogwheels):
    return sum(wheel[0] << i for i, wheel in enumerate(cogwheels))

cogwheels = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())

for _ in range(K):
    wheel_num, direction = map(int, input().split())
    wheel_num -= 1
    
    rotations = [0] * 4
    rotations[wheel_num] = direction
    
    # 왼쪽 확인
    for i in range(wheel_num - 1, -1, -1):
        if cogwheels[i][2] != cogwheels[i+1][6]:
            rotations[i] = -rotations[i+1]
        else:
            break
    
    # 오른쪽 확인
    for i in range(wheel_num + 1, 4):
        if cogwheels[i-1][2] != cogwheels[i][6]:
            rotations[i] = -rotations[i-1]
        else:
            break
    
    # 회전 적용
    cogwheels = [rotate(wheel, r) for wheel, r in zip(cogwheels, rotations)]

print(score_func(cogwheels))
