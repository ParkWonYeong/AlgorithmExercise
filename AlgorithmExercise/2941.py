## 크로아티아 알파벳

s = input()     # 크로아티아 알파벳 문자열
cnt = 0
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

i = 0
while i < len(s):

    for j in range(len(croa)):
        if croa[j] in s[i:i+3]:  # 크로아티아 목록에 있는 알파벳이면
            
            if croa[j] == 'dz=':
                i += 3
            else:
                i += 2
            cnt += 1
            break

    else:
        i += 1
        cnt += 1
    
print(cnt)