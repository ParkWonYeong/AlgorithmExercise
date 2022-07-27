## 42889
## 실패율

# 실패율 = (해당 스테이지 도전중(클리어X)) / (해당 스테이지 도달)

def solution(N, stages):
    
    fault = []
    b = len(stages)
    for i in range(1, N+1):
        # 실패율 = a / b
        if b <= 0:
            fault.append((i, 0))
        else:
            a = stages.count(i)
            fault.append((i, a/b))
            b -= a
    
    fault.sort(key = lambda x: (-x[1], x[0]))
    answer = list(zip(*fault))[0]
    
    return answer