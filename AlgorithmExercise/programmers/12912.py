## 12912

def solution(a, b):
    if b>a:
        answer = b*(b+1)//2-a*(a-1)//2
    else:
        answer = a*(a+1)//2-b*(b-1)//2
    return answer