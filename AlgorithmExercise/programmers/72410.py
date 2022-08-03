## 72410

## 신규 아이디 추천

def solution(new_id):
    # id 길이는 3자 이상 15자 이하
    # 알파벳 소문자, 숫자, -, _, . 문자만 사용
    # 이때 마침표(.)는 처음과 끝, 연속 사용이 불가
    
    # 1) 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()
    ans = ''
    check_com = 0
    
    # 2) 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    for idx in new_id:
        if (idx.isalnum() == True) or (idx == '-') or (idx == '_') or (idx == '.'):
            # 3) 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표로 치환
            if check_com == '.' and idx == '.':
                pass
            else:
                ans += idx
                check_com = idx

    # 4) 마침표(.)가 양끝에 위치하면 제거
    if len(ans) >= 2:
        if ans[0] == '.':
            ans = ans[1:]
        if ans[-1] == '.':
            ans = ans[:-1]
    else:
        if ans[0] == '.':
            ans = ''
    
    # 5) 빈 문자열이면 'a' 추가
    if len(ans) == 0:
        ans += 'a'
        
    # 6) 길이가 16자 이상이면 뒤에 삭제
    if len(ans) >= 16:
        ans = ans[:15]
        
    # 만약 삭제 후 끝부분이 마침표면 제거
    if ans[-1] == '.':
        ans = ans[:-1]
        
    # 7) 길이가 2자 이하면 마지막 문자를 추가
    if len(ans) <= 2:
        add_str = ans[-1]
        while len(ans) < 3:
            ans += add_str
    return ans