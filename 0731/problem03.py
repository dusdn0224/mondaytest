############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_item_price(item_list):
    # pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    s = 0
    for item in item_list: # 각 아이템 마다
        s += item['count'] * item['price'] # 수량과 가격 곱해서 총합에 넣기
    return s
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    SSAFANG_ITEM_LIST = [
        {
          'name': 'Galaxi Buds',
          'count': 3,
          'price': 150000,
        },
        {
          'name': 'Galaxi Pro Book 3',
          'count': 2,
          'price': 1500000,
        },
        {
          'name': 'Galaxi Mouse Pro',
          'count': 3,
          'price': 21000,
        },
    ]
    print(calc_item_price(SSAFANG_ITEM_LIST))  # => 3513000
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    