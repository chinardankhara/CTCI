#the problem is trivial and I am going to use the inbuilt queue
#I can write a new queue class and import but why?

from queue import PriorityQueue

class animalShelter:
  def __init__(self):
    self.dogs = PriorityQueue()
    self.cats = PriorityQueue()

  def enqueue(self, animal):
    if isinstance(animal, Dog):
      self.dogs.put(animal)
    else:
      self.cats.put(animal)

  def dequeueAny(self):
    temp_animal = self.dogs[self.front]
    if self.cats[self.front].get_age() > temp_animal.get_age():
      temp_animal = self.cats[self.front]

    if isinstance(temp_animal, Dog):
      return self.dogs.get()
    return self.cats.get()
      
  def dequeueDog(self):
    return self.dogs.get()

  def dequeueCat(self):
    return self.cats.get()

#note: since python sorts priority queue by lowest first, one would need to negate the age value to make it sort right
#in general, atrocious OOP support compared to java :(

  