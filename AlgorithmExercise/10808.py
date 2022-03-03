## 10808

s = input()
alpha = [0]*26  # 알파벳 개수 총 26개

for i in s:
    alpha[ord(i)-97] += 1
    # ord: 문자를 숫자(아스키코드)로 바꿔주는 함수.
    # 알파벳 a의 아스키코드인 97을 빼주어 배열의 index와 맞춰 배열에 값을 기입한다.

print(' '.join(map(str, alpha)))

# 30864KB, 72ms