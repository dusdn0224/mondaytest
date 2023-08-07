############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):
    # pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    cipher = ''
    for char in word:
        if char.islower(): # 소문자일 경우
            # if ord(char) <= 122 - num: # a로 안 넘어갈 경우
            #     new_char = chr(ord(char) + num)
            #     cipher += new_char
            # else: # a로 넘어갈 경우
            #     new_char = chr(ord(char) + num - 26)
            #     cipher += new_char
            new_char = chr(((ord(char) - 97 + num) % 26) + 97)
            cipher += new_char
        elif char.isupper(): # 대문자일 경우
            # if ord(char) <= 90 - num: # A로 안 넘어갈 경우
            #     new_char = chr(ord(char) + num)
            #     cipher += new_char
            # else: # A로 넘어갈 경우
            #     new_char = chr(ord(char) + num - 26)
            #     cipher += new_char
            new_char = chr(((ord(char) - 65 + num) % 26) + 65)
            cipher += new_char
    return cipher


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    