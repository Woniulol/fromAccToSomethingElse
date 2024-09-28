import typing


@typing.runtime_checkable
class MyProtocol(typing.Protocol):
    attribute_b: int

    def my_interface(self):
        ...

    def my_interface_signature(self, int_a: int, *, int_: int):
        ...

    # @property
    # def attribute_a(self):
    #     ...

class Concrete():
    def __init__(self, num: int) -> None:
        self.attribute_a = num
        self.attribute_b = num

    def my_interface(self):
        print("Hello World!")

    def my_interface_signature(self, float_a: float, *, int_: float):
        print("no signature is provided")

def type_check_func(p: MyProtocol):
    p.my_interface()

if __name__ == "__main__":
    print(isinstance(Concrete(1), MyProtocol))
    c = Concrete(1)
    print(c.attribute_a)
    c.my_interface()

    # Mypy does not check the type of the protocol signature.
    type_check_func(c)
