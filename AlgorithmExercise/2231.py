## 2231

import sys

n = int(sys.stdin.readline())       # 자연수 N을 문자열로 받는다.

for i in range(1, n+1):             # 1부터 N까지 반복
    num = i
    num += sum((map(int, str(i))))   # i의 각 자릿수 합
    num_sum = i+num     # 분해합 = 생성자 + i의 각 자릿수 합


    ## 위 코드 한 줄을 다르게 표현 하는 방법 ##
    num,sum = i,i
    while (num != 0):
        sum += num % 10 # 각 자릿수 더하기(1의 자리 수부터)
        num /= 10
    ## 하지만 이 반복구문까지 쓰면 시간초과가 발생했다. ##


    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을 때
    # 가장 작은 생성자를 가진다.
    if num_sum == n:    # 분해합이 자연수 N이 될 경우
        print(i)        # 그 i를 출력하고
        break           # 반복문을 종료한다.
    if i==n:            # 생성자 i와 입력값이 같으면 생성자가 달리 없는 것
        print(0)        #  0을 출력한다.

# 30864KB, 1300ms