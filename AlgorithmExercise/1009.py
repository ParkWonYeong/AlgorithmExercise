## 분산처리

# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     a,b = map(int, input().split())
#     aa = a%10

#     if aa == 0:
#         print(10)
#     elif aa in [1,5,6]:
#         print(aa)
#     elif aa in [4,9]:
#         if b%10 == 0:
#             print(aa*aa%10)
#         else:
#             print(aa)
#     else:
#         if b%10==0:
#             print(a)
#         else:
#             print(a**(b%10)%10)


# 1부터 10까지 각각을 거듭제곱 했을 때 1의 자리 패턴 확인
# 1: 1
# 2: 2,4,6,8
# 3: 3,9,7,1
# 4: 4,6
# 5: 5
# 6: 6
# 7: 7,9,3,1
# 8: 8,4,2,6
# 9: 9,1
# 10: 10

# => 1,5,6은 자기자신, 10일때는 0이므로 10 출력.
# =>=> 4,9는 b도 10으로 나눈 나머지를 구하고 나머지 0이면 a 그대로 출력, 아니면 a*a%10 출력
# =>=>=>=> b를 10으로 나눈 나머지를 구하고 나머지 0이면 a 그대로 출력, 아니면 a를 나머지만큼 거듭제곱 한 것의 나머지 출력


# 1 -> 1
# 2 -> 2, 4, 8, 6
# 3 -> 3, 9, 7, 1
# 4 -> 4, 6
# 5 -> 5
# 6 -> 6
# 7 -> 7, 9, 3, 1
# 8 -> 8, 4, 2, 6
# 9 -> 9, 1
# 10 -> 0

# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     a,b = map(int, input().split())
#     a %= 10

#     if a == 0 or a == 1 or a == 5 or a == 6:
#         ans = a

#     elif a == 4 or a == 9:
#         if b%2 == 0:
#             ans = (a**2)%10
#         else:
#             ans = (a%10)
    
#     else:
#         ans = a**(b%4)%10

#     print(ans)

# 반례 : 3 11
# answer 7
# output 3


## 221029
import sys
input = sys.stdin.readline

for i in range(int(input())):
    a,b = map(int, input().split())
    aa = int(str(a)[-1])

    if aa in [1,5,6]:
        ans = aa
    elif aa in [4,9]:
        bb = b%2
        if aa == 4:
            list_4 = [6,4]
            ans = list_4[bb]
        else:
            list_9 = [1,9]
            ans = list_9[bb]
    elif aa in [2,3,7,8]:
        bb = b%4
        if aa == 2:
            list_2 = [6,2,4,8]
            ans = list_2[bb]
        elif aa == 3:
            list_3 = [1,3,9,7]
            ans = list_3[bb]
        elif aa == 7:
            list_7 = [1,7,9,3]
            ans = list_7[bb]
        else:
            list_8 = [6,8,4,2]
            ans = list_8[bb]
    else:
        ans = 10
    
    print(ans)