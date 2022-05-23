## 43165

answer = 0

# dfs function
def dfs(numbers, target, idx, total):
    global answer
    if idx == len(numbers):
        if target == total:
            answer += 1
        return
    dfs(numbers, target, idx+1, total+numbers[idx])
    dfs(numbers, target, idx+1, total-numbers[idx])
    
# main
def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer