## 86051

def solution(numbers):
    all = [0,1,2,3,4,5,6,7,8,9]
    answer = 0
    for i in range(len(all)):
        if all[i] not in numbers:
            answer += all[i]
    return answer

## 별해 ##
def solution(numbers):
    return 45-sum(numbers)