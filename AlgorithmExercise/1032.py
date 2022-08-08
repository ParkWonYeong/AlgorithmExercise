## 1032
# 명령 프롬프트

# 검색 결과가 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지 출력한다.
# 패턴에는 알파벳, '.', '?'만 넣을 수 있다. '?'는 가능한 적게 써야한다.
# 파일 이름의 길이는 모두 같다.

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