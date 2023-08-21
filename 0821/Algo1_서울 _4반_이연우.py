T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_b = 0  # 최대 점수 변수
    min_b = 20*20  # 최소 점수 변수

    for i in range(N):
        for j in range(N):
            temp = arr[i][j]  # 점수를 입력받을 변수(초기값은 해당 풍선의 점수)

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우
                for k in range(1, arr[i][j] + 1):  # 해당 풍선의 점수만큼의 거리
                    ni, nj = i + di * k, j + dj * k  # 거리만큼 간다
                    if 0 <= ni < N and 0 <= nj < N:  # 게임판 안에 있다면
                        temp += arr[ni][nj]  # 점수 변수에 더해준다

            if max_b < temp:  # 최대 점수보다 크다면
                max_b = temp  # 그것이 최대 점수
            if min_b > temp:  # 최소 점수보다 작다면
                min_b = temp  # 그것이 최소 변수

    print(f'#{tc}', max_b - min_b)  # 최대 최소 차를 출력
