T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cards = list(input().split())
    B = []
    C = []
    bonus = 0

    for card in cards:
        if card.isdigit():  # 카드가 숫자라면
            card = int(card)
            if (card + bonus) % 2:  # 카드가 홀수라면
                B.append(card + bonus)
            else:  # 카드가 짝수라면
                C.append(card + bonus)
        elif card == '+':  # 더하기 카드라면
            bonus += 1

    point = [0] * 11  # 게임의 참가자는 최대 10명
    for i in range(1, 11):  # 1부터 10까지
        temp = 0
        if B:  # 빈 스택이 아니라면
            temp += B.pop(0)
        if C:  # 빈 스택이 아니라면
            temp += C.pop()
        point[i] = temp  # 포인트는 B덱과 C덱에서 가져온 카드의 합

    print(f'#{tc}', point[M])
