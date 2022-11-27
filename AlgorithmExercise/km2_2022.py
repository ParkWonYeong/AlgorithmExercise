def solution(id_list, k):

    check_list = {}
    answer = 0      # 고객에게 지급된 쿠폰 총 수량

    for i in range(len(id_list)):
        p = list(map(str, id_list[i].split()))
        p = list(set(p))                # 물품 구매 고객은 하루 최대 1장씩 할인 쿠폰 수령

        for j in p:
            if j not in check_list:
                check_list[j] = 1
                answer += 1
            elif j in check_list:
                if check_list[j] < k:   # 고객 한 명당 최대 k장까지 할인 쿠폰 수령 가능
                    check_list[j] += 1
                    answer += 1
    
    return answer