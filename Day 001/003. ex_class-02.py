#------------------------------------------------
# 상속(Inheritance)
# - 다중 상속 허용
# - class 자식클래스명(부모클래스1, ... )
#-----------------------------------------------

class A :
    @classmethod
    def printinfo(cls):
        print('A')

class B:
    @classmethod
    def printinfo(cls):
        print('B')

class AB(A,B):
    pass

class CC(B,A):
    pass

ab1 = AB()
ab1.printinfo()