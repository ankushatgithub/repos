class A():
    def func(self):
        print("In A Func")

    def func2(self):
        print("In A Func2")


class B():
    def func(self):
        print("B In Func")

    def func2(self):
        print("B In Func2")


class C(B,A):
    def func(self):
        print("C In Func2")


a = C()
a.func2()
