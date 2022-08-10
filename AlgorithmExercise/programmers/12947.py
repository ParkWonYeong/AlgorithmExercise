## 12947

def solution(x):
    
    check_x = str(x)
    
    cnt_x = 0
    for i in range(len(check_x)):
        cnt_x += int(check_x[i])
    
    answer = False
    
    if x % cnt_x == 0:
        answer = True
    
    return answer