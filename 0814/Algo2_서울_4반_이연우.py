T = int(input())
for tc in range(1, T+1):
    susik = input()
    # 괄호 스택
    bracket = []
    # 각 괄호에 들어있는 숫자를 넣을 리스트
    number = [[] for _ in range(len(susik) + 1)]
    # 스택 위치
    top = -1
    # -1을 출력하는 경우 체크용
    ans = True

    for i in range(len(susik)):
        # 여는 괄호의 경우 위치 정보 +1 후 스택에 추가
        if susik[i] == '(':
            top += 1
            bracket.append(susik[i])
        elif susik[i] == '{':
            top += 1
            bracket.append(susik[i])
        # 닫는 괄호의 경우, 짝이 맞는 경우에만
        # 스택에 들어있는 괄호는 없애줍니다.
        # 숫자 리스트도 초기화해줍니다.
        # 해당 괄호에 있는 숫자의 연산 후, 이전 괄호의 숫자 리스트에 추가해줍니다.
        # 만약 마지막 괄호라서 top이 -1이 되면 number[-1]에 연산이 저장될 것입니다.
        elif susik[i] == ')' and top != -1 and bracket[top] == '(':
            n = 0
            for num in number[top]:
                n += num
            number[top].clear()
            bracket.pop()
            top -= 1
            number[top].append(n)
        elif susik[i] == '}' and top != -1 and bracket[top] == '{':
            n = 1
            for num in number[top]:
                n *= num
            number[top].clear()
            bracket.pop()
            top -= 1
            number[top].append(n)
        # 숫자라면
        # top이 -1이 아닌 경우 == 괄호가 열린 상태인 경우에만
        # 해당 위치에 추가해줍니다.
        elif susik[i].isnumeric():
            if top == -1:
                ans = False
                break
            else:
                number[top].append(int(susik[i]))
        # 위의 조건에 해당하지 않는 경우는
        # 괄호의 짝이 맞지 않는 경우이므로 -1을 출력해야합니다.
        else:
            ans = False
            break

    # 괄호 스택에 괄호가 들어있거나 ans가 False라면 -1을 출력
    if bracket or not ans:
        print(f'#{tc}', -1)
    # 그렇지 않다면 number[-1]에 입력된 연산 결과를 출력
    else:
        print(f'#{tc}', *number[-1])
