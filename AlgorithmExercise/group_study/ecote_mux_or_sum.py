## 곱하기 혹은 더하기

s = input()     # 주어지는 숫자(문자열)

# 모든 문자 하나 사이에 곱하기 혹은 더하기를 넣어야한다.
# 모든 연산은 곱셈,덧셈 관계없이 왼쪽에서부터 이루어진다.

calculate,answer = int(s[0]), int(s[0])

for i in range(1, len(s)):
    calculate = max(int(s[i])*answer, int(s[i])+answer)
    answer = calculate

print(answer)