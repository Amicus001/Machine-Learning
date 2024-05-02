# Create Class
# - elements : attributes + method: 모두 없음
# - 기본 상속: object= __속성명__, __메서드명__()

class A():
    pass
#-----------------------------------------------------------
# Create Class 2
# - elements : attributes + method: 모두 없음
# - 기본 상속: object= __속성명__, __메서드명__()
#-----------------------------------------------------------
class B:

    #인스턴스 객체 생성 및 속성 초기화 메서드
    def __init__(self, num, name):
        #self로 지정된 힙 메모리 주소에서부터 속성 저장
        self.num = num
        self.name = name

    #인스턴스 메서드
    def printinfo(self):
        print(f'numL{self.num}')
        print(f' {self.name}')

    # 연산자 맵핑 메서드 구현
    # 연산자 + 과 맵핑된 메서드
    def __add__(self, other):
        print('__add__')
        return self.num + other.num
    def __sub__(self, other):
        return self.__sub__(self, other)
#===========================================================
#object / instance
# ->생성 함수: 클래스이름(init 메서드 매개변수)=
#
#===========================================================


a1 = A()
b1 = B(100, 'bb')
b2 = B(30, 'B2')
#객체, 인스턴스의 연산--------------------------------------
print(('ABC'+"123"))
print([1,2,3] + [10.20,3])
print('====>',b1 + b2)
print('====>',b1 - b2)


#===========================================================
#object / instance
# ->생성 함수: 클래스이름(init 메서드 매개변수)=
#
#===========================================================

print('B instance b1 속성과 메서드:',b1.__dict__ )
print('B 인스턴스 b1의 속성과 메서드:', b1.__dir__())
print('B 클래스의 속성과 메서드:', B.__dict__)

#객체/인스턴스의 속성/메서드 사용: 방법
#객체/인스턴스 변수명.속성
#객체/인스턴스 변수명/메서드
#------------------------------------
# print('a1의 속성과 메서드', a1.__dict__) #A의 인스턴스 a1
# print(A.__dict__) #클래스 A
#
# print(f'A의 인스턴스 a1의 속성과 메서드: ', a1.__dir__()) #메서드에 self가 붙으면 instance.
# print('A 클래스의 속성과 메서드:', A.__dict__)

#-----------------------------------------------------------
# Create Class 2
# - elements : attributes + method: 모두 없음
# - 기본 상속: object= __속성명__, __메서드명__()
#-----------------------------------------------------------
class C:
    #클래스 변수: c 클래스로 생성된 모든 인스턴스에서 공유
    #             인스턴스 생성 없이 사용 가능
    loc = 'Daegu'

    #인스턴스 객체 생성 및 속성 초기화 메서드
    def __init__(self, num, name):
        #self로 지정된 힙 메모리 주소에서부터 속성 저장
        self.num = num
        self.name = name

    #인스턴스 메서드
    def printinfo(self):
        print(f'num:{self.num}')
        print(f'name: {self.name}')

c1=C(100, 'ccc')

#인스턴스 메서드 사용
c1.printinfo()

#인스턴스 속성 사용:
print(c1.name)

#클래스 속성 사용
print("loc: ", C.loc, c1.loc)

#인스턴스 메서드는 클래스명으로 사용 불가: self(인스턴스) 주소 및 정보 없음
#C.printinfo()<-self 값 없으므로 오류 발생


#-----------------------------------------------------------
# Create Class 4
# - elements : attributes + method: 모두 없음
# - 기본 상속: object= __속성명__, __메서드명__()
#-----------------------------------------------------------
class DCalc:
    #클래스 변수: c 클래스로 생성된 모든 인스턴스에서 공유
    #             인스턴스 생성 없이 사용 가능
    name = 'CASIO'

    #클래스 메서드
    @classmethod
    def addnum(cls, a, b):
        print(cls.name)
        print(cls.addnum(a,b))
        return a + b
    @classmethod
    def minusnum(cls, a,b):
        return a - b


#클래스 속성 및 메서드 사용
print(f'DCalc.name():{DCalc.name}')
print(f'DCalc.addnum():{DCalc.addnum()}')
print(f'DCalc.minusnum():{DCalc.minusnum()}')