def solution(m, n, board):
    answer = 0
    board_rotated = [[0] * m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            board_rotated[n - j - 1][m - i - 1] = board[i][j] 
    
    while True:
        check = [[0] * m for _ in range(n)]
        
        for i in range(n-1):
            for j in range(m-1):
                tem_char = board_rotated[i][j]
                if tem_char.isalpha():
                    if tem_char == board_rotated[i][j+1] and tem_char == board_rotated[i+1][j] and tem_char == board_rotated[i+1][j+1]:
                        check[i][j] = 1
                        check[i][j+1] = 1
                        check[i+1][j] = 1
                        check[i+1][j+1] = 1
        tem = 0
        for i in range(n):
            tem += sum(check[i])

        if tem == 0:
            break
        answer += tem
        new_board = []
        
        for i in range(n):
            new_line = []
            for j in range(m):
                if check[i][j] == 0:
                    new_line.append(board_rotated[i][j])
            while len(new_line) < m:
                new_line.append('_')
            new_board.append(new_line)
        board_rotated = new_board
    
    return answer