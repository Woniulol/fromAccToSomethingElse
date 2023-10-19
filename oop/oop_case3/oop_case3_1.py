class Dog:
    def __init__(self, name: str, age: int = 1) -> None:
        self.age = age
        self.name = name

    def eat(self):
        print(f"dog {self.name} is eating")

    def sleep(self):
        print(f"dog {self.name} is sleeping")

    def play(self):
        print(f"dog {self.name} is playing")

    def watch(self):
        print(f"dog {self.name} is watching")


class Cat:
    pass


class Person:
    pass


if __name__ == "__main__":
    d = Dog(name="dd", age=3)
    d.eat()
    d.sleep()
    d.play()
    d.watch()
    print(d.__dict__)
