#coding:utf-8
import abc

# L'Arbre (classe abstraite)
class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass

# Une branche
class Composite(Component):
    def __init__(self):
        self._children = set()

    def operation(self):
        for child in self._children:
            child.operation()

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)

# Une feuille
class Leaf(Component):
    def operation(self):
        pass

def main():
    item = Leaf()
    bag = Composite()
    bag.add(item)
    bag.operation()

if __name__ == "__main__":
    main()
