## 실패율
# 실패율 = (해당 스테이지 도전중(클리어X)) / (해당 스테이지 도달)

def solution(N, stages):
    
    fault = []              # 배열 생성(스테이지, 실패율)
    b = len(stages)         # 나눌 인원수(stages에 담긴 인원수로 시작)
    for i in range(1, N+1):
        # 실패율 = a / b
        if b <= 0:          # 런타임에러 예외처리: 나눌 인원수가 0 이하면 무조건 0
            fault.append((i, 0))
        else:
            a = stages.count(i)     # 해당 스테이지 도전중인 인원
            fault.append((i, a/b))  # 배열에 (스테이지, 실패율) append
            b -= a                  # 다음 스테이지에서 해당 인원 제외
    
    fault.sort(key = lambda x: (-x[1], x[0]))   # 1순위: 실패율, 2순위: 스테이지
    answer = list(zip(*fault))[0]               # 0번째에 위치한 스테이지만 추출
    
    return answer