## 12903

def solution(s):
    if len(s)%2 != 0:    # 홀수인 경우
        i = (len(s)+1)//2 - 1
        answer = s[i]
    else:
        i = len(s)//2 - 1
        answer = s[i:i+2]
    return answer