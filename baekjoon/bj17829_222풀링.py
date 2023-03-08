import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def find_second_max(x, y, answer):
    import heapq
    heap_ = []
    for i in range(x, x + 2):
        for j in range(y, y + 2):
            heapq.heappush(heap_, answer[i][j])
    heap_.sort()
    return heap_[-2]


def solution(N, input_matrix):
    answer = [[0 for _ in range(N//2)] for _ in range(N//2)]
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            answer[i//2][j//2] = find_second_max(i, j, input_matrix)
    return answer


while N > 1:
    matrix = solution(N, input_matrix=matrix)
    N = N//2
print(matrix[0][0])
