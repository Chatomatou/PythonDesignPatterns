#coding:utf-8
import copy

class Prototype:
    pass

#---------------------------------------------
def main():
    original = Prototype()
    prototype = copy.deepcopy(original)

if __name__ == "__main__":
    main()
