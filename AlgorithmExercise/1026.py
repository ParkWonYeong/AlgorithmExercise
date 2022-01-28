## 1026

# 길이가 N인 정수 배열 A와 B가 있다.
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]이다.
# 단, B에 있는 수는 재배열하면 안된다.
# S의 최솟값을 출력.

from sys import stdin

N = int(stdin.readline())   # N이 주어진다.
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

# S의 최솟값을 만들기 위해
# A는 오름차순, B는 내림차순으로 정렬한 뒤 계산하도록 한다.
A.sort()
B.sort(reverse=True)

sum=0
for i in range(N):
    div = A[i]*B[i]
    sum += div

print(sum)


## 처음에 이렇게 풀고 정답이라고 인정되었다.
## 하지만 문제의 조건에서 B는 재배열을 하면 안 된다고 적혀있다.

# 다른 방법으로 A배열의 최소값과 B 배열의 최대값을 곱한다.
# 그리고 pop 함수를 이용해 이들을 배열에서 빼준다.

from sys import stdin

N = int(stdin.readline())   # N이 주어진다.
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

sum=0
for _ in range(N):
    div = min(A)*max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
    sum += div

print(sum)

# 이를 이용하면 두 배열을 재정렬 하지 않고 풀 수있다.

## 다른 풀이를 찾아보니 A배열만 재정렬하는 풀이도 있었다.

from sys import stdin

N = int(stdin.readline())   # N이 주어진다.
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
A.sort()
sum=0
for i in range(N):
    div = A[i]*B.pop(B.index(max(B)))
    sum += div

print(sum)

# 세 가지 풀이 모두 메모리 30864KB, 시간 68ms로 동일했다.