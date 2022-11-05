#start of dog classifier

class Dog:
 def __init__(self, breed, gender, age, prego, activity):
  self.breed = breed #str for breed size
  self.age = age #str fo range
  self.gender= gender #male/female
  self.prego = prego #self explanitory
  self.activity = activity #self explanitory


 def puppies(self):
  if self.age == 'puppies':
   if self.breed== 'toy':
    if self.activity == 'not-active':
     return #food
    if self.activity == 'medium-activity':
     return #food
    if self.activity == 'active':
     return #food
   elif self.breed == 'small':
    if self.activity == 'not-active':
     return #food
    if self.activity == 'medium-activity':
     return #food
    if self.activity == 'active':
     return #food
   elif self.breed == 'medium':
    if self.activity == 'not-active':
     return #food
    if self.activity == 'medium-activity':
        return #food
    if self.activity == 'active':
        return #food
   elif self.breed == 'large':
    if self.activity == 'not-active':
        return #food
    if self.activity == 'medium-activity':
        return #food
    if self.activity == 'active':
        return #food
  else: return None  
     