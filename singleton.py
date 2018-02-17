class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class SomeClass(metaclass=Singleton):
    pass

def main():
    sg1 = SomeClass()
    sg2 = SomeClass()
    print(f"sg1 : {id(sg1)} / sg2 : {id(sg2)}")

if __name__ == "__main__":
    main()
