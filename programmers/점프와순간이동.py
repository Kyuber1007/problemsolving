def solution(n):
    ans = 0

    # n이 0이 되면 전체 다 이동한 것을 의미함.
    while n:
        # n이 2의 배수일 경우 그냥 2배씩 이동하도록 함.
        if n % 2 == 0:
            n /= 2
        # 아닐 경우, 1 칸씩 움직이도록 함.
        else:
            n -= 1
            ans += 1
    return ans


solution(5000)
