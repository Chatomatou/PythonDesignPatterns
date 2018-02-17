#coding:utf-8

class Facade:
    def __init__(self):
        self._subclass_1 = SubClass1()
        self._subclass_2 = SubClass2()
        self._subclass_3 = SubClass3()
        #other...
        
    def operation(self):
        self._subsystem_1.operation1()
        self._subsystem_1.operation2()
        self._subsystem_2.operation1()
        self._subsystem_2.operation2()
        self._subsystem_3.operation1()
        self._subsystem_3.operation2()
        #other...

class SubClass1:
    def operation1(self):
        pass

    def operation2(self):
        pass

class SubClass2:
    def operation1(self):
        pass

    def operation2(self):
        pass
        
class SubClass3:
    def operation1(self):
        pass

    def operation2(self):
        pass

def main():
    facade = Facade()
    facade.operation()

if __name__ == "__main__":
    main()
