#start of dog classifier

class Dog:
 def init(self, size, age, prego):
  self.size = size
  self.age = age
  self.prego = prego

 def food(self):
  if self.age <= 8 and self.size == "toy":
   ####
   pass
  elif self.age <= 11 and self.size == "small":
   ####
   pass
  elif self.size in ['medium','large']:
   ####
   pass