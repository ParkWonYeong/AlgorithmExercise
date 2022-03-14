## 2745

import sys
n,b = sys.stdin.readline().rstrip().split()
n = ''.join(reversed(n))    # 높은 자릿수부터 계산하기 위해 뒤집는다.
b = int(b)

# 36진법에 해당하는 숫자와 알파벳을 담은 문자열
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = 0
# range(시작, 마지막, -1(거꾸로))
for i in range(len(n)-1,-1,-1): # 반복문을 뒤에서부터 거꾸로 실행
    # number에서 해당 문자열에 해당하는 인덱스 값을 구하고 진수에 i에 해당하는 제곱 곱하기
    ans += number.index(n[i])*(b**i)
    
print(ans)



## 별해 ##
# B진법으로 된 수 N을 곧바로 출력시킨다.
n,b = map(str, sys.stdin.readline().rstrip().split())
# int(변환할 string, n진법). n진법은 정수 형태로 입력해야한다.
print(int(n,int(b)))