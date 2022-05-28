## 42586

def solution(progresses, speeds):
    
    # 입력받은 원본 배열 보존
    progress = progresses
    speed = speeds
    
    answer = []
    time,cnt = 0,0
    
    while len(progress) > 0:    # 기능당 걸리는 날 수 계산
        if (progress[0]+speed[0]*time >= 100):  # 맨 앞의 기능 완성시
            progress.pop(0)     # 맨 앞의 항목 pop
            speed.pop(0)
            cnt += 1            # cnt 증가
            
        else:                   # 맨 앞의 기능 미완성시
            if cnt > 0:         # 이미 앞에 완성된 기능 있으면
                answer.append(cnt)  # 완성기능 내보내기
                cnt = 0         # answer 넣어주고 cnt 초기화
            time += 1           # time 증가
            
    answer.append(cnt)
    
    return answer