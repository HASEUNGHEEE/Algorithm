def solution(phone_book):
    # 1. Hash Map을 만든다.
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1 # key : value = phone_number : 1(1개 존재)
        
    # 2. 접두어가 Hash Map에 존재하는지 찾는다.
    for phone_number in phone_book:
        jubdoo = ""
        for digit in phone_number:
            jubdoo += digit
            # 3. 접두어를 찾는다. (기존번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True
    

    """
    # Sorting 후 1중 Loop을 통해 앞의 번호가 뒷 번호의 접두어인지 확인하는 방법
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

    """
    
