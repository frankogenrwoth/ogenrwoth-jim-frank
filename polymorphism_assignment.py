# overloading
def get_sum(*numbers):
    return sum(numbers)


# overriding
class A:
    def say_hi(self):
        pass


class B(A):
    def say_hi(self):
        print("hello")


if __name__ == "__main__":
    print(get_sum(1, 4, 6), get_sum(3, 5))
    b = B()
    b.say_hi()
