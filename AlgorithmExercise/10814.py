## 10814
# stable 정렬과 unstable 정렬
# stable 정렬: 입력 받은 값들 중에 같은 값이 있을 경우 해당 값의 순서를 그대로 유지한다.
# unstable 정렬에서는 이를 장담할 수 없다. 파이썬은 기본적으로 stable 정렬을 한다.

import sys

n = int(sys.stdin.readline())   # 온라인 저지 회원 수 N
member = []
for _ in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)          # 나이는 정수형으로 type을 바꿔준다.(비교해야하기 때문)
    member.append((age,name))

member.sort(key=lambda x:x[0])     # (age, name) 중 x[0]요소인 age만을 비교한다.

# 이러한 방식으로 나이순(오름차순)으로 정렬해주면 나머지 요소인 가입 순서는 남아있으므로 알맞게 출력된다.
for i in member:
    print(i[0], i[1])

# 45488KB, 300ms