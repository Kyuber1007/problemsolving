def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book) - 1):
        length = len(phone_book[i])
        if phone_book[i + 1][:length] == phone_book[i]:
            return False
    return True


# solution(["119", "97674223", "1195524421"])
# solution(["12", "321", "123", "1235", "567", "88"])
solution(["123", "456", "789"])
