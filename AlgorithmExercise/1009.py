## 분산처리

import sys
input = sys.stdin.readline

for i in range(int(input())):
    a,b = map(int, input().split())
    aa = a%10

    if aa == 0:
        print(10)
    elif aa in [1,5,6]:
        print(aa)
    elif aa in [4,9]:
        if b%10 == 0:
            print(aa*aa%10)
        else:
            print(aa)
    else:
        if b%10==0:
            print(a)
        else:
            print(a**(b%10)%10)


# 1부터 10까지 각각을 거듭제곱 했을 때 1의 자리 패턴 확인
# 1: 1
# 2: 2,4,6,8
# 3: 3,9,7,1
# 4: 4,6
# 5: 5
# 6: 6
# 7: 7,9,3,1
# 8: 8,4,2,6
# 9: 9,1
# 10: 10

# => 1,5,6은 자기자신, 10일때는 0이므로 10 출력.
# =>=> 4,9는 b도 10으로 나눈 나머지를 구하고 나머지 0이면 a 그대로 출력, 아니면 a*a%10 출력
# =>=>=>=> b를 10으로 나눈 나머지를 구하고 나머지 0이면 a 그대로 출력, 아니면 a를 나머지만큼 거듭제곱 한 것의 나머지 출력