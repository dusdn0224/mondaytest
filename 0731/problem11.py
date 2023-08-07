############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def get_row_col_maxsum(matrix):
    # pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    row_counts = []
    rs = 0
    for r in matrix: # 행마다
        row_count = 0
        cs = 0
        for c in r:
            row_count += c # 행 합 구해서
            cs += 1 # 열 개수
        row_counts.append(row_count) # 행 합 리스트에 넣기
        rs += 1 # 행 개수
    column_counts = []
    for i in range(cs):
        column_count = 0
        for j in range(rs):
            column_count += matrix[j][i] # 열 합 구해서
        column_counts.append(column_count) # 열 합 리스트에 넣기
    row_counts.sort(reverse=True) # 정렬
    column_counts.sort(reverse=True) # 정렬
    if row_counts[0] > column_counts[0]: # 행 합이 더 클 경우
        return ('row', row_counts[0])
    elif row_counts[0] < column_counts[0]: # 열 합이 더 클 경우
        return ('col', column_counts[0])
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    