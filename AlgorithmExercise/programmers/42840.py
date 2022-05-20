## 42840

def solution(answers):

    num_1 = [1,2,3,4,5]
    num_2 = [2,1,2,3,2,4,2,5]
    num_3 = [3,3,1,1,2,2,4,4,5,5]

    count1, count2, count3 = 0,0,0
    for i in range(len(answers)):
        if answers[i] == num_1[i%5]:
            count1 += 1
        if answers[i] == num_2[i%8]:
            count2 += 1
        if answers[i] == num_3[i%10]:
            count3 += 1

    ans = max(count1, count2, count3)
    answer = []
    for i, cnt in enumerate([count1, count2, count3]):
        if cnt == ans:
            answer.append(i+1)

    return answer