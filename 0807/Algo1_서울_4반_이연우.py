T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 좌표: (y1, x1, y2, x2)
    y1, x1, y2, x2 = map(int, input().split())
    # 마당
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 평균값 구하기
    h = 0
    cnt = 0
    for i in range(y1, y2 + 1):  # 녹색영역
        for j in range(x1, x2 + 1):
            h += arr[i][j]  # 높이 값의 합
            cnt += 1  # 영역의 칸 수
    avr = h // cnt  # 평균값

    # 평탄화 작업의 횟수
    flatten = 0
    for i in range(y1, y2 + 1):  # 녹색 영역
        for j in range(x1, x2 + 1):
            if arr[i][j] > avr:  # 평균값보다 높을 경우
                flatten += arr[i][j] - avr
            elif arr[i][j] < avr:  # 평균값보다 낮을 경우
                flatten += -(arr[i][j] - avr)
            # 평균값과 높이가 같은 경우엔 평탄화 작업 X

    print(f'#{tc}', flatten)
