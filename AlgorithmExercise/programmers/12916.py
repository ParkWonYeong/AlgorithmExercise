## 12916
# 문자열 내 p와 y 개수

def solution(s):
    
    s = s.lower()
    
    cnt_p = s.count('p')
    cnt_y = s.count('y')
    
    answer = False
    
    if cnt_p == cnt_y:
        answer = True
    

    return answer