## 12932

def solution(n):
    n = str(n)
    answer = []
    for i in range(len(n)):
        num = int(n[-(i+1)])
        answer.append(num)
    return answer