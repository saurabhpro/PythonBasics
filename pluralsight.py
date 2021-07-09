class ClassA:
    def a(self):
        return 'A'


class ClassB(ClassA):
    def b(self):
        return 'B'


class B:
    def b(self):
        return 'B'


class C(ClassA, B):
    def c(self):
        return 'c'


def even_series():
    num = 0
    while True:
        yield num
        num += 2
