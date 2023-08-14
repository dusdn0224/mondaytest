T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 봉우리 수
    cnt = 0

    # i 행, j 열
    for i in range(N):
        for j in range(N):
            # 상하좌우
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                # 인접지역의 좌표가 2차원 배열 안에 있고
                if 0 <= ni < N and 0 <= nj < N:
                    # 해당 지역의 높이보다 크거나 같은 인접지역이 존재한다면
                    if arr[i][j] <= arr[ni][nj]:
                        # 탐색 종료
                        break
            # 탐색이 중간에 끝나지 않았다면 == 인접지역이 모두 해당 지역보다 낮다면
            # 봉우리에 추가
            else:
                cnt += 1

    print(f'#{tc}', cnt)
