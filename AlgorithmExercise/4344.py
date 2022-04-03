## 4344

testcase = int(input())
for i in range(testcase):

    student = []
    student = list(map(int, input().split()))
    num = student[0]
    sum, cnt = 0, 0
    
    for j in range(num):
        sum += student[j+1]
    
    average = sum / num
    
    for k in range(num):
        if student[k+1] > average:
            cnt += 1
        else:
            continue
    ans = '%.3f'%(cnt/num * 100)
    print(ans+'%')

## 30860KB, 76ms