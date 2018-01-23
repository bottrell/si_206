'''
add a ‘speak’ method to Animal—make up something that a generic Animal would say
add ‘speak’ methods to Dog and Bird (but not Spider) that are like the one we added to Dog earlier. Have them say what you think Dogs and Birds would say.
Make all the animals speak
Add a Snake class, with appropriate choices for number of legs, greeting, and speak. Test your Snake.
To turn in: get as far as you can. At a minimum, you should implement Animal.speak(self) and speak(self) for at least one subclass, and write code that accesses each method. Turn in your modified version of animals.py 


'''
class Animal:
  legs = 4

  def __init__(self, nm):
    self.name = nm

  def get_num_legs(self):
    return self.legs

  def greeting(self):
    return "cowers"

  def speak(self):
    return "boo"


class Dog(Animal):

  def __init__(self, nm, br):
    super().__init__(nm)
    self.breed = br

  def speak(self):
    return "Bark"

  def greeting(self):
    return "wags"

class Cow(Animal):
  pass

class Bird(Animal):
  legs = 2

  def speak(self):
    return "chirp"


class Spider(Animal):
  legs = 8

class Snake(Animal):
  legs = 0

  def greeting(self):
    return "slithers"

  def speak(self):
    return "Hisssss"


class Labrador(Dog):
  def __init__(self, nm):
    super().__init__(nm, 'Labrador')

  def greeting(self):
    return super().greeting() + " enthusiastically"


d1 = Dog('Fido', 'Australian Shepherd')
c1 = Cow('Bessie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')
l1 = Labrador('Air Bud')
snake1 = Snake('Wormy')

animals = [d1, c1, b1, s1, l1]
for a in animals:
  print (a.name, 'has', a.get_num_legs(), 'legs and', a.greeting())

if isinstance(d1, Animal):
  print("A dog is an animal")
else:
  print("A dog is not an animal")

print(d1.speak())
print(c1.speak())
print(b1.speak())
print(s1.speak())
print(l1.speak())
print(snake1.speak())
