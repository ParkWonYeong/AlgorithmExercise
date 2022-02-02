# 9012

# 괄호문자열(Parenthesis String, PS): (와 ) 만으로 구성된 문자열.
# 한 쌍의 괄호 기호로 된 () 문자열은 기분 VPS(Valid PS).
# x가 VPS라면 이것을 하나의 괄호에 넣은 새로운 문자열(x)도 VPS.
# 두 VPS x와 y를 접합시킨 새로운 문자열 xy도 VPS

# VPS가 되기 위한 조건은 (부터 시작된 (와 )의 개수가 같아야 한다는것.
# 따라서 (를 +, )를 -라고 생각했을 때 최종 합산이 0이 되면 YES를 출력하는 알고리즘을 만든다.

import sys
input = sys.stdin.readline

T = int(input())    # 입력 데이터의 수

for _ in range(T):
    strings = input()   # 한 줄씩 입력된 PS 값을 받아주고,
    s = list(strings)   # 리스트로 만든다.
    sum = 0
    for j in s:         # 만든 리스트에서
        if j == '(':    # ( 가 나오면 +1, 
            sum += 1
        elif j == ')':  # ) 가 나오면 -1을 해준다.
            sum -= 1
        if sum < 0:     # ) 가 더 많이 나오면 VPS 생성을 할 수 없으므로
            print("NO")
            break       # 바로 break한다.

    if sum > 0:         # 한편, 빠져나와서 ( 가 더 많으면
        print("NO")     # VPS 만들기 실패
    elif sum == 0:      # 빠져나와서 (와 )의 수가 같으면
        print("YES")    # VPS 만들기 성공

# 메모리 30864KB, 시간 76ms로 성공했다.