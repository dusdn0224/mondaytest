T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = input()
    key = input()
    # Key를 16진수로 변환
    try:
        k = int(key)
    except:
        if key == 'A':
            k = 0xA
        elif key == 'B':
            k = 0xB
        elif key == 'C':
            k = 0xC
        elif key == 'D':
            k = 0xD
        elif key == 'E':
            k = 0xE
        else:
            k = 0xF
    print(f'#{tc}', end=' ')
    # 연산 수행 및 출력
    for i in range(N):
        try:
            print(hex(int(P[i]) ^ k)[2].capitalize(), end='')
        except:
            if P[i] == 'A':
                p = 0xA
            elif P[i] == 'B':
                p = 0xB
            elif P[i] == 'C':
                p = 0xC
            elif P[i] == 'D':
                p = 0xD
            elif P[i] == 'E':
                p = 0xE
            else:
                p = 0xF
            print(hex(p ^ k)[2].capitalize(), end='')
    print()
