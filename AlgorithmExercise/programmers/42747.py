## 42747

def solution(citations):
    answer = 0
    citations.sort(reverse = True)  # 큰수부터 내림차순
    
    for i in range(len(citations)):
        if citations[i] >= i+1:     # h번 이상 인용이 h편 이상
            answer = i+1
    
    return answer