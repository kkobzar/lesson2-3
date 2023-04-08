class Cat:
    isHungry = True

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

    def feed(self, cat):
        if cat.isHungry:
            print(self.name, "is feeding cat named", cat.name)
            cat.isHungry = False
        else:
            print(cat.name, 'is not hungry')




my_cat = Cat("Barsik")
me = Person('Kyryl', 22)

# print(me.isHappy)
#
# my_cat.play(me)
# print(me.isHappy)

me.feed(my_cat)
