## 15649

n,m = map(int, input().split())

def backtracking(s):
    if len(s) == m:                     # 선택을 반복했을 때 그 경우의 수가 m이면 끝.
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if i in s:      # i값이 s에 있는 경우(이미 선택한 숫자)
            continue    # 넘어가서 진행한다.(가지치기한다)
        # backtracking(s+[i])
        s.append(i)     # 해당 경우의 수 스택에 추가(Push)
        backtracking()
        s.pop()         # 함수 동작 후 스택에서 빼내기(pop)
        # 함수가 종료되면 해당요소들이 제거(pop)되어 호출 전의 상태로 돌아가므로
        # 주석의 형태를 이용해도 동일하게 동작한다.

# backtracking([])
backtracking()      # s = []