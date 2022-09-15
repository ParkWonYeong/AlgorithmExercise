## 문자열 압축

# def solution(s):
    
#     answer = len(s)
    
#     for num in range(1, len(s)//2 + 1):
#         stack = ''
#         cnt, cut = 1, s[:num]
        
#         # 1~문자열의 반의 개수까지 돌며 현재와 다음 num 값을 비교한다.
#         # 비교해서 값이 같으면 반복되는 단위로 취급
#         for i in range(num, len(s), num):
#             # 이전상태와 동일
#             if cut == s[i:i+num]:
#                 cnt += 1
                
#             # 반복되는 문자열 단위를 벗어나는 경우
#             else:
#                 # 반복되는 문자가 없어서 한 번만 나타난 경우
#                 if cnt < 2:
#                     stack += cut
#                 # 반복되는 문자가 있는데 그 반복이 끝난 경우
#                 else:
#                     stack += str(cnt) + cut    
                    
#                 # 이후 다음 num로 넘어가며 cut과 cnt 다시 초기화
#                 cnt, cut = 1, s[i:i+num]
#         # 남은 문자열 마저 처리
#         if cnt < 2:
#             stack += cut
#         else:
#             stack += str(cnt) + cut
        
#         # 가장 짧은 것의 길이를 요구했으므로 min값.
#         answer = min(answer, len(stack))

#     return answer



## 문자열 압축(2회독)

def solution(s):

    # 초기값 할당
    ans = len(s)   

    for num in range(1, len(s)//2+1):

        cnt, cut = 1, s[:num]           # cut: 반복되는 문자열 카운트, cut: 자를 문자열
        save = ''

        for i in range(num, len(s), num):
            if cut == s[i:i+num]:       # 반복되는 문자열인 경우
                cnt += 1

            else:                       # 반복되는 문자열이 끝났거나 없는 경우
                # 문자열 압축하기

                if cnt < 2:             # 맨 처음일 때
                    save += cut
                else:                   # 그 외(반복된 문자열이 끝났을 때)
                    save += str(cnt) + cut

                cnt, cut = 1, s[i:i+num]    # 새롭게 반복되는 문자열을 찾아 갱신

        # 나머지 문자열이 남은 경우, 위의 else 구문 내 과정과 동일하게 문자열을 압축하여 마저 처리함.
        if cnt < 2:
            save += cut
        else:
            save += str(cnt) + cut

        ans = min(len(save), ans)       # 더 짧은 압축 문자열 길이로 갱신

    return ans

print(solution('aabbaccc'))