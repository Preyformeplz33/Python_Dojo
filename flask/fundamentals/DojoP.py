class Ninja:
     def __init__(first_name ,last_name,treats,pet_food,pet):
          self.first_name = first_name#Recca
          self.last_name= last_name#Hanabishi
          self.treats = Candy #Ramune
          self.pet_food = pet_food #Chips
          self.pet = Pet(name="",type="",tricks="")

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
     def __init__(name,type,triks):
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

userone = Ninja("Recca","Hanabishi","Ramune","Chips")
Nine=pet("Nine","em","hide")

Recca.walk()









