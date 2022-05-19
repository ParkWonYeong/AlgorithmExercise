## 42577

def solution(phone_book):

    phone_book.sort()
    # 한 번호가 다른 번호의 접두어로 존재하면 false
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False
    return True