## 배열합치기

# sol1. 배열 정렬 이용
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = sorted(a+b)

print(' '.join(str(i) for i in ans))    # 혹은 print(*ans)


# sol2. 투포인터 이용
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []

a_pointer, b_pointer = 0,0
a_length, b_length = len(a), len(b)

while a_pointer != a_length or b_pointer != b_length:
    if a_pointer == a_length:       # a의 원소는 다 담겼다면
        ans.append(b[b_pointer])
        b_pointer += 1
    elif b_pointer == b_length:     # b의 원소는 다 담겼다면
        ans.append(a[a_pointer])
        a_pointer += 1
    else:                           # a,b 원소 모두 아직 다 안 담겼다면
        if a[a_pointer] < b[b_pointer]:     # 크기에 맞게 정렬하며 append
            ans.append(a[a_pointer])
            a_pointer += 1
        else:
            ans.append(b[b_pointer])
            b_pointer += 1

print(*ans)