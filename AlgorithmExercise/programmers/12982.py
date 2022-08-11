def solution(d, budget):
    
    answer = 0
    d.sort()    # 오름차순 정렬
    print(d)
    
    i = 0
    while i < len(d):
        if (budget >= d[i]):
            budget -= d[i]
            answer += 1
            
            print(budget)
            print('i= ', i)
            i += 1
        else:
            break
    
    return answer