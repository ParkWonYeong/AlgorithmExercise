## 1181

# 시간 단축을 위해 input 자리에 sys.stdin.readline()을 사용하니 출력 형식이 잘못되었다는 오답이 나타났다.
# sys.stdin.readline()이 \n\을 포함하는 입력이기 때문에 연속으로 값을 입력받는 for문에서 에러가 발생한다고 한다.
# 따라서 문자열을 append할 때 .strip()을 추가로 입력해준다.

import sys

N = int(sys.stdin.readline())   # 단어의 개수 N
en = []

for _ in range(N):
    en.append(sys.stdin.readline().strip())

en = list(set(en))          # 집합의 성질을 이용해 중복을 삭제한다.
en.sort(key=lambda x: (len(x),x))   # 우선순위: 1) 길이 2) 사전순

print("\n".join(en))

# sys 라이브러리를 사용했을 때는 104ms로,
# 단순히 input을 썼을 때 870~890ms가 나온 것과 비교해보면
# 매우 빨라졌음을 알 수 있다.