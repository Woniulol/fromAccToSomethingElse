# 每一个类都会有很多重复的东西
# 可以使用继承特性减少代码的重复
# 把公共的东西写在父类里面
class Dog:
    def __init__(self, name: str, age: int = 1) -> None:
        self.age = age
        self.name = name

    def __str__(self) -> str:
        return f"dog {self.name} whose age is {self.age} is"

    def eat(self):
        print(f"{self} eating")

    def sleep(self):
        print(f"{self} sleeping")

    def play(self):
        print(f"{self} playing")

    def watch(self):
        print(f"{self} watching")


class Cat:
    def __init__(self, name: str, age: int = 1) -> None:
        self.age = age
        self.name = name

    def __str__(self) -> str:
        return f"cat {self.name} whose age is {self.age} is"

    def eat(self):
        print(f"{self} eating")

    def sleep(self):
        print(f"{self} sleeping")

    def play(self):
        print(f"{self} playing")

    def catch(self):
        print(f"{self} catching")


class Person:
    def __init__(
        self, name: str, pets: [Dog | Cat | None] = [None], age: int = 1
    ) -> None:
        self.pets = pets
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"person {self.name} whose age is {self.age} is"

    def eat(self):
        print(f"{self} eating")

    def sleep(self):
        print(f"{self} sleeping")

    def play(self):
        print(f"{self} playing")

    def pet_care(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()

    def pet_work(self):
        for pet in self.pets:
            if isinstance(pet, Dog):
                pet.watch()
            elif isinstance(pet, Cat):
                pet.catch()
            else:
                print("unidentified pet type")
            # 这么写程序的扩展是很恶心的
            # 需要对动物的work进行抽象


if __name__ == "__main__":
    d = Dog(name="dd", age=3)
    d.eat()
    d.sleep()
    d.play()
    d.watch()
    print(d.__dict__)

    c = Cat(name="cc", age=5)
    c.eat()
    c.sleep()
    c.play()
    c.catch()
    print(c.__dict__)

    p = Person(name="pp", pets=[d, c], age=18)
    p.pet_care()
    p.pet_work()
