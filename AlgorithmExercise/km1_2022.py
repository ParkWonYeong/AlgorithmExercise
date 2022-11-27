def solution(flowers):

    flowers.sort()
    start = flowers[0][0]
    answer = flowers[0][1] - flowers[0][0]
    
    for i in range(1, len(flowers)):
        if flowers[i][0] < flowers[i-1][1]: # 앞의 꽃이 지는 날짜 전에 피는 꽃이 있을 때
            if flowers[i][1] > flowers[i-1][1]: # 앞의 꽃이 지고 난 후에 지는 꽃일 때
                answer += flowers[i][1]-flowers[i-1][1]
        
        else:                               # 앞의 꽃이 지는 날짜 후 피는 꽃이 있을 때
            answer += flowers[i][1] - flowers[i][0]
    
    return answer