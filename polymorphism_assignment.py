# overloading
def get_sum(*numbers):
    return sum(numbers)


# overriding
class A:
    def say_hi(self):
        print("hello from A")


class B(A):
    def say_hi(self):
        print("hello from B")


# MRO
class C(A):
    def say_hi(self):
        print("hello from C")


class D(B, C):
    pass


if __name__ == "__main__":
    print(get_sum(1, 4, 6), get_sum(3, 5))
    b = B()
    b.say_hi()

    d = D()
    d.say_hi()
