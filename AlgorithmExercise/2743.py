## 2743

import sys
# sys.argv는 배열이다.
# sys.argv[0]에 기본적으로 파이썬 실행파일의 경로가 담겨있다.
# 그래서 sys.argv의 길이는 기본적으로 1이다.
# 우리가 알고싶은 값은 문자 알파벳 개수 자체 뿐이므로 여기서 1을 빼줘야한다.
print(len(sys.stdin.readline())-1)

# 30864KB, 76ms

## 별해 ##
# 단순 input을 사용하는 경우에는 1을 빼주지 않아도 된다.
print(len(input()))

# 30864KB, 84ms