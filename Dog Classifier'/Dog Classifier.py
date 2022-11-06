#start of dog classifier

class Dog:
 def __init__(self, size, gender, age, pregnant, activity):
  self.size = size #str for breed size
  self.age = age #str fo range
  self.gender= gender #male/female
  self.activity = activity #amount of physical activity
  self.pregnant = 1 if pregnant == "Yes" else 0 #if pregnant
  self.age_imp = 1 ###int
  self.size_imp = 1 ###int
  self.activity_imp = 1 ###int
  self.pregnant_imp = 1 ###int


 def food(self):
  self.age_imp * self.age_c() + self.size_imp * self.size_c() + self.activity_imp * self.activity_c() + self.pregnant_imp * self.pregnant
 
 def age_c(self):
  match self.age:
   case 'puppy': return ###int
   case 'adult': return ###int
   case 'senior': return ##int
 
 def size_c(self):
  match self.size:
   case 'toy': return ###int
   case 'small': return ###int
   case 'medium': return ##int
   case 'large': return ##int

 def activity_c(self):
  match self.activity:
   case 'low': return ###int
   case 'medium': return ###int
   case 'active': return ##int
