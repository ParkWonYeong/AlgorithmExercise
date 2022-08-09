## 1032
# 명령 프롬프트

import sys
input = sys.stdin.readline

# input : 파일 이름의 개수 N (N<=50)
n = int(input())
ans = ''

# 반례: n=1인 경우
if n == 1:
    print(input())

else:
    file_list = []

    # n개의 줄에 주어지는 파일 이름(길이는 모두 같고 최대 50)
    for i in range(n):
        file_list.append(input())

    for j in range(len(file_list[0])-1):
        check_same = False

        for k in range(n-1):
            if file_list[k][j] == file_list[k+1][j]:
                check_same = True
            else:
                check_same = False
                break
        
        if check_same == True:
            ans += file_list[k][j]
        else:
            ans += '?'

    print(ans)