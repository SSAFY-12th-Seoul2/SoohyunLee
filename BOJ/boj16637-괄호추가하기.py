# 괄호 추가하기 

# 계산
def calculate(a, b, op):
    # print('####### op:', a, b, op)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:  # op == '*'
        return a * b


def dfs(idx, result):
    global max_result
    
    # 연산이 끝났을 때
    if idx == len(operators):
        max_result = max(max_result, result)
        return
    
    # 괄호 없이 계산
    # 현재의 숫자(result)와 다음의 숫자(numbers[idx + 1])를 연산(operators[idx])
    next_result = calculate(result, numbers[idx + 1], operators[idx])
    dfs(idx + 1, next_result)
    
    # 괄호를 추가하면서 계산
    if idx + 1 < len(operators):
        # 괄호 계산
        temp_result = calculate(numbers[idx + 1], numbers[idx + 2], operators[idx + 1])
        # 괄호 계산 한 값(temp_result)과 기존 값(result) 연산 수행
        next_result = calculate(result, temp_result, operators[idx])
        dfs(idx + 2, next_result)

N = int(input())
expression = input()
# 팁: 계산식으로 되어있을 때 eval함수를 이용하여 바로 답을 도출할 수 있음
# print(eval(expression))

# 숫자와 연산자 분리
numbers = [int(expression[i]) for i in range(0, N , 2)]
operators = [expression[i] for i in range(1, N , 2)]

max_result = -1e9

# DFS 시작
dfs(0, numbers[0])

# 결과 출력
print(max_result)