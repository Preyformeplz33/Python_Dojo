class Ninja:
     def __init__(self,first_name ,last_name,pet_food,pet):
          self.first_name = first_name#Recca
          self.last_name= last_name#Hanabishi
          self.treats = Ramune #Ramune
          self.pet_food = pet_food #Chips
          self.pet = Pet

# walk() - walks the ninja's pet involing the pet play() method
     def walk(self):
          self.pet.play()
          return(self)
# feed () - feeds the ninjas pet invking the pet eat () method
     def feed(self):
          self.pet.eat()
          return(self)
# bathe()-cleans the ninjas pet invoking the pet noise()method
def bathe(self):
     self.pet.noise()
     return(self)





class pet:
     def __init__(self,name,type,triks):
          self.name= name
          self.type = type
          self.triks = 333
          self.health = 333

#implemet the following methods:
     def sleep(self):
          self.energy += 25
     def eat(self):
          self.health += 10
          self.energy = 5
     def play(self):
          self.health+=5
     def sound(self):
          print('Ya!Ya!Ya')

userone = Ninja("Recca","Hanabishi","Chips")
Nine=pet("Nine","em","hide")

Recca.walk()









