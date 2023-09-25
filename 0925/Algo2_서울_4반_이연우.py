def f(cnt, point, lst):
    global max_point
    # 모든 행을 다 돌았을 때 최대값 갱신
    if cnt == N:
        max_point = max(max_point, point)
        return
    # 0 ~ N-1 열 중 사격하지 않은 열만 방문
    # 방문할 때 방문한 리스트에 넣어주고 함수가 끝나면 다시 없애줌
    for i in range(N):
        if i not in lst:
            lst.append(i)
            f(cnt + 1, point + arr[cnt][i], lst)
            lst.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_point = 0
    f(0, 0, [])
    print(f'#{tc}', max_point)