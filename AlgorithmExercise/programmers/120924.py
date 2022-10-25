def solution(common):
    if common[0]-common[1] == common[1]-common[2]:  # 등차수열일 때
        answer = common[-1] + (common[1]-common[0])
    else:
        answer = common[-1]*(common[1]//common[0])
        
    return answer