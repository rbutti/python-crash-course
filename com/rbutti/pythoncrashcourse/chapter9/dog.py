class Dog:

    name = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("nestam", 1)
print(my_dog.name)
my_dog.sit()
