## 68644

def solution(numbers):
    
    answer = set()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            ans = numbers[i]+numbers[j]
            answer.add(ans)
    answer = list(answer)
    answer.sort()
    return answer