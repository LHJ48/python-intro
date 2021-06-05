import calendar


class Calculator(object): # object는 객체의미
    '''
    클래스 내부에 있는 함수를 메소드라고 정의한다.
    '''
    def __init__(self, first_num, second_num): # 생성자인데, 외부에서 입력받는 값을 설정하는 메소드
        self.first_num = first_num
        self.second_num = second_num

    def add(self):
        return self.first_num + self.second_num

    def sub(self):
        return self.first_num - self.second_num

    def mul(self):
        return self.first_num * self.second_num

    def div(self):
        return self.first_num / self.second_num

    '''
    클래스 내부에 있는 함수를 메소드라고 정의한다.
    일반메소드에서 정의한 기능을 호출해서 실제 값으로 연산하는 메소드를
    스태틱메소드라고 하며 @staticmethod 로 표시한다.
    '''

    @staticmethod
    def main():
        while 1:
            menu = input('0-종료 1-계산기 : ')
            if menu == '0':
                break
            elif menu == '1':
                calc = Calculator(int(input('첫번쨰 수: ')), int(input('두번째 수: ')))
                print('*' * 30)
                print(f'{calc.first_num} + {calc.second_num} = {calc.add()}')
                print(f'{calc.first_num} - {calc.second_num} = {calc.sub()}')
                print(f'{calc.first_num} * {calc.second_num} = {calc.mul()}')
                print(f'{calc.first_num} / {calc.second_num} = {calc.div()}')
                print('*' * 30)
            else:
                print('잘못된 메뉴선택입니다.')

if __name__ == '__main__':
    Calculator.main()
