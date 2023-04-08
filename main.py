class Cat:
    def __init__(self, name):
        self.name = name

    def play(self, person):
        print('Im playing with', person.name)
        person.isHappy = True



class Person:
    isHappy = False

    def __init__(self, name, age):
        self.name = name
        self.age = age


my_cat = Cat("Barsik")
me = Person('Kyryl', 22)

print(me.isHappy)

my_cat.play(me)
print(me.isHappy)
