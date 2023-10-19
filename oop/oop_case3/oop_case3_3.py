class Animal:
    def __init__(self, name: str, age: int = 1) -> None:
        self.age = age
        self.name = name

    # 但这里不能给person对象添加pet
    # 所以在下面会给Person重新写一个__init__
    # 但是使用super调用父类的__init__

    def eat(self):
        print(f"{self} eating")

    def sleep(self):
        print(f"{self} sleeping")

    def play(self):
        print(f"{self} playing")


class Dog(Animal):
    def __str__(self) -> str:
        return f"dog {self.name} whose age is {self.age} is"

    def work(self):
        print(f"{self} watching")


class Cat(Animal):
    def __str__(self) -> str:
        return f"cat {self.name} whose age is {self.age} is"

    def work(self):
        print(f"{self} catching")


class Person(Animal):
    # Person 应该也要有自己的 __init__ 但是会覆盖
    # 所以使用super

    # ohhhhhhh vscode will automatically create the super when identifying one
    # class is inheriting from another one
    def __init__(self, name: str, pets: [Dog | Cat] = None, age: int = 1) -> None:
        super(Person, self).__init__(name, age)
        # 找self的下一个class的MRO链条，调用Person里的init方法
        self.pets = pets

    def __str__(self) -> str:
        return f"person {self.name} whose age is {self.age} is"

    def pet_care(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()

    def pet_work(self):
        for pet in self.pets:
            pet.work()
        # 现在的问题是pet里面可能没有work方法


if __name__ == "__main__":
    d = Dog(name="dd", age=3)
    d.eat()
    d.sleep()
    d.play()
    d.work()
    print(d.__dict__)
    print("---end---")

    c = Cat(name="cc", age=5)
    c.eat()
    c.sleep()
    c.play()
    c.work()
    print(c.__dict__)
    print("---end---")

    p = Person(name="pp", pets=[d, c], age=18)
    p.eat()
    p.sleep()
    p.play()
    print(p.__dict__)
    print("---end---")
