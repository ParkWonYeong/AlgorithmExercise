## 1417

n = int(input())

# 득표수 중 최댓값에서 한장씩 매수해주어야 한다.
vote = [0]*n
cnt = 0

## 예외처리(후보자가 없을때)
if n == 1:
    pass

else:
    for i in range(n):
        vote[i] = int(input())
    
    dasom = vote.pop(0)

    while dasom <= max(vote):
        # 다솜이 득표수 1 추가
        dasom += 1
        # 득표수 가장 많던 후보 득표수 1 감소
        vote[vote.index(max(vote))] -= 1
        # 다솜이가 매수한 사람의 수 갱신
        cnt += 1
print(cnt)

# 30840KB, 68ms