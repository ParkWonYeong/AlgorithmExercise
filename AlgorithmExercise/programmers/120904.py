def solution(num, k):
    answer = 0
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) == k and answer == 0:
            answer = i+1

    return -1 if answer==0 else answer