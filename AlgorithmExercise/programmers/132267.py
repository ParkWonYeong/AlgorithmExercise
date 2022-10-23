def solution(a, b, n):
    answer = 0
    # 마트에 주는 빈병 a, a병당 마트가 주는 b, 가지고 있는 수 n
    while n >= a:
        # print('have: ', n)
        give = n - n%a
        get = (give//a)*b
        answer += get      # 얻는 병의 수
        n = n%a + get
        # print('give: ', give)
        # print('get: ', get)

    return answer