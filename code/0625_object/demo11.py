class Animal:
    def shout(self):
        print("叫")



class Bird(Animal):
    def fly(self):
        print("飞")
    # def shout(self):
    #     print("叫")


class Dog(Animal):
    def run(self):
        print("跑")
    # def shout(self):
    #     print("叫")
animal = Animal()
bird = Bird()
dog = Dog()
print(isinstance(animal,Bird))
print(isinstance(dog,Animal))
print(issubclass(Animal,Bird))
print(issubclass(Dog,Animal))