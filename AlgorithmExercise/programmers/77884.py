## 77884

def solution(left, right):
    
    num = 0
    l = right-left+1
    
    for i in range(l):
        
        target = left + i
        cnt = 0
        
        for j in range(1,target+1):
            if target % j == 0:
                cnt += 1
                
        if cnt % 2 == 0:
            num += target
        else:
            num -= target
    answer = num
    return answer