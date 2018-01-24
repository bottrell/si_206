'''
SI 206 W18 Homework03: Classes and Inheritance

Your discussion section:
People you worked with:

######### DO NOT CHANGE PROVIDED CODE ############
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

'''
Task A
'''
from random import randrange
class Explore_pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

coco = Explore_pet()

#your code begins here . . .
coco.boredom = 10
print(coco)
brian = Explore_pet("Brian")
brian.hunger = 20
print(brian)

'''
Task B
'''
#For task B, add your code inside the Pet class
class Pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10
    words = ["Hello"]

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

    def clock_tick(self):
        self.hunger += 2
        self.boredom += 2

    def say(self):
        print("I know how to say: ")
        for word in self.words:
            print(word)

    def teach(self, word):
        self.words.append(word)
        self.boredom += self.boredom_decrement
        if self.boredom < 0:
            self.boredom = 0

    def feed(self):
        self.hunger += self.hunger_decrement
        if self.hunger < 0:
            self.boredom = 0

    def hi(self):
        index = randrange(len(self.words))
        print(self.words[index])
'''
Task C
'''


def teaching_session(my_pet,new_words):
    for word in new_words:
        my_pet.teach(word)
        my_pet.hi()
        print(my_pet)
        if my_pet.mood() == "hungry":
            my_pet.feed()
        my_pet.clock_tick()

  #your code goes here. Replace pass with your code . . .

mark = Pet("Mark")
my_words = ["that's", "a", "bold", "move", "general", "cotton", "we'll", "see", "how", "that", "one", "plays", "out"]
teaching_session(mark, my_words)


#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################
'''
Task A: Dog and Cat
'''
#your code begins here . . .
class Dog(Pet):
    def __str__(self):
        state = "I'm " + self.name + 'arrrf! '
        state += 'I feel ' + self.mood() + 'arrrf! '
        if self.mood() == 'hungry':
            state += 'Feed me, arrrf!'
        if self.mood() == 'bored':
            state += 'You can teach me new words, arrrf!'
        return state

class Cat(Pet):
    meow_count = 0
   
    def __init__(self, name = "Coco", meow_count = 3):
        super().__init__(name)
        self.meow_count = meow_count

    def hi(self):
        index = randrange(len(self.words))
        print(self.words[index] * self.meow_count)

#cat = Cat("Jordan", 10)
#teaching_session(cat, words)

'''
Task B: Poodle
'''
#your code begins here . . .
class Poodle(Dog):
    def dance(self):
        print("Dancing in circles like poodles do!")

    def say(self):
        self.dance()
        super().say()

doodle = Poodle("Doodle")
doodle.say()

cat = Cat("Lebron", 3)
cat.hi()


