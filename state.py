#coding:utf-8
import abc

class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self):
        pass

class ConcreteState1(State):
    def handle(self):
        pass

class ConcreteState2(State):
    def handle(self):
        pass

#-------------------------------------
def main():
    cs1 = ConcreteState1()
    context = Context(cs1)
    context.request()

if __name__ == "__main__":
    main()
