## 12916
# 문자열 내 p와 y 개수

def solution(s):
    
    answer = False
    s = s.lower()
    
    cnt_p, cnt_y = s.count('p'), s.count('y')
    
    if cnt_p == cnt_y:
        answer = True
    
    return answer