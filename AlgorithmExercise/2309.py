## 2309

# 일곱 난쟁이의 키 합이 100
# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다.
# 가능한 정답이 여러가지인 경우에는 아무거나 출력한다.

# 일곱난쟁이의 키를 오름차순으로 출력한다.

import sys
input = sys.stdin.readline

nan = []
for _ in range(9):
    nan.append(int(input()))

# 전체 난쟁이들의 키 - 가짜 난쟁이들의 키 = 100
total = sum(nan)  # 여기선 전부 더하고나면 100 이상의 수가 될 것이다.
n1,n2 = 0,0
for i in range(9):
    for j in range(i+1,9):
        if (total - (nan[i]+nan[j]) == 100):
            n1, n2 = nan[i], nan[j]
nan.remove(n1)
nan.remove(n2)
nan.sort()

# join 할때 리스트 값들이 정수형이면 런타임 에러가 난다.
print('\n'.join(map(str, nan)))

# 30864KB, 68ms