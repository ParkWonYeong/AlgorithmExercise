## 86491

def solution(sizes):
    # 비교해서 width에 큰 값 몰빵, height에 작은 값 몰빵
    for i in range(len(sizes)):
        if (sizes[i][0] < sizes[i][1]) :
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
            
    answer = max(sizes, key=lambda x:x[0])[0]*max(sizes, key=lambda y:y[1])[1]
    return answer