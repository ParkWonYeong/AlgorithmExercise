## 문자열 재정렬

# 알파벳 대문자와 숫자로만 구성된 문자열.
# 알파벳을 모두 오름차순 한 뒤에 숫자 정렬.

s = input()
alpha=''
num=0

for i in range(len(s)):
    if s[i].isalpha() == True:  #  알파벳이면 alpha string에 추가
        alpha += s[i]
    else:
        num += int(s[i])        # 숫자면 num에 더하기

alpha = sorted(alpha)           # 오름차순 정렬
alpha += str(num)               # 모든 숫자를 더한 값 num 추가

for i in range(len(alpha)):
    print(alpha[i], end='')