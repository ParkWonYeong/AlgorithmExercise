# 최댓값과 최솟값

def solution(s):
    num = list(map(int, s.split()))
    return str(min(num)) + " " + str(max(num))