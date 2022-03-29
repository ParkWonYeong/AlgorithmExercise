## 10162

# A=5분(=300초), B=1분(=60초), C=10초
# 전자레인지로 요리해야할 시간=T
# A,B,C 3개의 이용 횟수 합은 항상 최소가 되어야한다.(최소 버튼 조작)
# 제시된 3개의 버튼으로 T초를 맞출 수 없다면 -1 출력


T = int(input())

a,b,c,error = 0,0,0,0

while T >= 0:
    if T >= 300:        # 300초 이상인 경우
        T -= 300        # 버튼 A를 사용한다
        a += 1
        continue
    elif T >= 60:       # 60초 이상인 경우
        T -= 60         # 버튼 B를 사용한다
        b += 1
        continue
    elif T >= 10:       # 10초 이상인 경우
        T -= 10         # 버튼 C를 사용한다
        c += 1
        continue
    elif T==0:          # 0초가 된 경우
        break           # 반복문을 빠져나간다.
    else:
        error -= 1      # 그 외(10초 미만)의 경우 -1을 출력한다
        break
    
if error == -1:
    print(error)

else:
    print(a, b, c)

# 30864KB, 76ms (별해도 동일)


### 별해 ###

T = int(input())
cnt = [0]*3
abc = [300,60,10]

if(T%10 != 0):  # 1의 자리가 0이 아니면, 즉 버튼 사용으로 0만들기가 불가능하면
    print(-1)   # -1 출력

else:           # 그 외의 경우 5585번 동전 만들기처럼 나머지 이용해서 구하기
    for i in range(3):
        cnt[i] = T//abc[i]  # 큰값부터 나누어 몫은 카운트에 저장
        T -= cnt[i]*abc[i]  # 남은 T
    print(cnt[0], cnt[1], cnt[2])
