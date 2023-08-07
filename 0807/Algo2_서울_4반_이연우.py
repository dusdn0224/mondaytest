T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 점수 구하기
    point = 0
    for i in range(1, N+1):  # N번의 챌린지 수행
        for j in range(N):  # 탁자
            if 0 <= i * j < N:  # 챌린지 동안 탁자 안에서 튀기는 조건으로
                point += arr[i * j]  # 점수에 더해주기

    # 획득 점수가 0점 이하인 경우네는 0점으로 출력하기
    if point <= 0:
        point = 0

    print(f'#{tc}', point)
