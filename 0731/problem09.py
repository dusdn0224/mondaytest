############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_digits(number):
    # pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    i = 0
    for n in str(number): # 자릿수 구하기
        i += 1
    if i == 1: # 한자릿수일 때
        return number
    return (number // (10 ** (i - 1))) + sum_digits(number % (10 ** (i - 1))) # 재귀함수(더하기)
    
    
# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_digits(123))  # => 6
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    