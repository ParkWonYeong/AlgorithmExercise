## 82612

def solution(price, money, count):
    cnt = 0
    for i in range(count):
        cnt += i+1
        
    answer = cnt*price - money
    
    if answer <= 0:
        return 0

    return answer```