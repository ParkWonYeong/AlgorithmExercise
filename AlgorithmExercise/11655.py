## 11655

# 아스키 코드를 이용해서 알파벳을 +13씩 밀어낸다.
# A는 65, Z는 90
# a는 97, z는 122

import sys
s = sys.stdin.readline()

ans = ''
for i in s:
    if 'A' <= i and i <= 'Z':   # 알파벳 대문자인 경우
        i = ord(i)+13
        if i>90:                # Z를 넘어설 경우
            i -= 26
        ans += chr(i)           # 아스키코드를 다시 영문으로 변환해준다
    elif 'a' <= i and i <= 'z': # 알파벳 소문자인 경우
        i = ord(i)+13
        if i>122:               # z를 넘어설 경우
            i -= 26
        ans += chr(i)           # 아스키코드를 다시 영문으로 변환해준다
    else:                       # 숫자나 공백일 경우
        ans += i                # 그대로 출력한다

print(ans)

# 30864KB, 68ms