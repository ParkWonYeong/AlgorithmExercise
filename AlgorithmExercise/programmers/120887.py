def solution(i, j, k):
    answer = 0
    k = str(k)
    for m in range(i,j+1):
        answer += str(m).count(k)
    return answer