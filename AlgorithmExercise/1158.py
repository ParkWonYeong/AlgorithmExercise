## 1158

# 1번부터 N번까지 N명의 사람이 원을 이뤄 앉아있다고 양의 정수가 주어짐
# 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로
# 이루어진 원을 따라 이 과정을 계속 해나간다.
# 이 과정은 N명의 사람들이 모두제거될 때까지 게속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 예를들어 (7,3)-요세푸스 순열은 <3,6,2.7,5,1,4>이다.

import sys
input = sys.stdin.readline

n,k = map(int, input().split())

circle = []
for i in range(n):
    circle.append(i+1)
# circle 안에는 1부터 N까지의 번호가 부여된다.

num = k
result = []
index = 0

while len(circle) != 0:
    index += num-1
    if index >= len(circle):    # 인덱스 값이 부여된 최댓값보다 커질 경우
        index = index % len(circle) # 기존의 부여받은 수로 나눠 그 나머지값으로 계산해주면 된다.
    result.append(circle.pop(index))

print("<", ', '.join(str(i) for i in result[:]), ">", sep="")

# 참고
# ".join(리스트)": 매개변수 ['a','b','c'] => 'abc'로 합쳐서 반환
# '구분자'.join(리스트): 요소들 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐 변환
# ex) '_'.join(['a','b','c'])라 하면 "a_b_c"로 반환