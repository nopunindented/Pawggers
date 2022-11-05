#start of dog classifier

class Dog:
 def __init__(self, breed, gender, age, pregnant, activity):
  self.breed = breed #str for breed size
  self.age = age #str fo range
  self.gender= gender #male/female
  self.pregnant = pregnant #if pregnant
  self.activity = activity #amount of physical activity
  food_amount= ''
  self.food_amount= food_amount

 def food(self):
    match self.food_amount:
        ####do shit
        case None: return



 ####----####                          
 def activity_check(self):             
  match self.activity:
   case 'not-activity': return 
   case 'medium-activity': return
   case 'active': return
 ####----####                          

 def adult(self):
  match 'breed':
   case 'toy':
            if self.activity == 'not-active':
                return #food
            if self.activity == 'medium-activity':
                return #food
            if self.activity == 'active':
                return #food
        if self.breed == 'small':
            if self.activity == 'not-active':
                return #food
            if self.activity == 'medium-activity':
                return #food
            if self.activity == 'active':
                return #food
        if self.breed == 'medium':
            if self.activity == 'not-active':
                return #food
            if self.activity == 'medium-activity':
                return #food
            if self.activity == 'active':
                return #food
        if self.breed == 'large':
            if self.activity == 'not-active':
                return #food
            if self.activity == 'medium-activity':
                return #food
            if self.activity == 'active':
                return #food

 def senior(self):
    if self.age == 'senior' and self.gender== 'male':
        if self.breed== 'toy':
            if self.activity == 'not-active':
                return #food
            if self.activity == 'medium-activity':
                return #food
            if self.activity == 'active':
                return #food
        if self.breed == 'small':
            if self.activity == 'not-active':
                return #food
            if self.activity == 'medium-activity':
                return #food
            if self.activity == 'active':
                return #food
        if self.breed == 'medium':
            if self.activity == 'not-active':
                return #food
            if self.activity == 'medium-activity':
                return #food
            if self.activity == 'active':
                return #food
        if self.breed == 'large':
            if self.activity == 'not-active':
                return #food
            if self.activity == 'medium-activity':
                return #food
            if self.activity == 'active':
                return #food

    elif self.age == 'senior' and self.gender== 'female':
        if self.pregnant== 'pregnant':
            if self.breed== 'toy':
                if self.activity == 'not-active':
                    return #food
                if self.activity == 'medium-activity':
                    return #food
                if self.activity == 'active':
                    return #food
            if self.breed == 'small':
                if self.activity == 'not-active':
                    return #food
                if self.activity == 'medium-activity':
                    return #food
                if self.activity == 'active':
                    return #food
            if self.breed == 'medium':
                if self.activity == 'not-active':
                    return #food
                if self.activity == 'medium-activity':
                    return #food
                if self.activity == 'active':
                    return #food
            if self.breed == 'large':
                if self.activity == 'not-active':
                    return #food
                if self.activity == 'medium-activity':
                    return #food
                if self.activity == 'active':
                    return #food
        if self.pregnant== 'not-pregnant':
            if self.breed== 'toy':
                if self.activity == 'not-active':
                    return #food
                if self.activity == 'medium-activity':
                    return #food
                if self.activity == 'active':
                    return #food
            if self.breed == 'small':
                if self.activity == 'not-active':
                    return #food
                if self.activity == 'medium-activity':
                    return #food
                if self.activity == 'active':
                    return #food
            if self.breed == 'medium':
                if self.activity == 'not-active':
                    return #food
                if self.activity == 'medium-activity':
                    return #food
                if self.activity == 'active':
                    return #food
            if self.breed == 'large':
                if self.activity == 'not-active':
                    return #food
                if self.activity == 'medium-activity':
                    return #food
                if self.activity == 'active':
                    return #food
                
 def food(self):
  match self.age:
   case 'puppy': 
    self.puppies() 
   case 'adult':
    self.adult()
   case 'senior':
    self.senior()
 

 def puppies(self):
  match self.breed:
   case 'toy':
    match self.activity:
     case 'not-activity':
      return #food
     case 'medium-activity':
      return #food
     case 'active':
      return #food
   case 'small':
    match self.activity:
     case 'not-activity':
      return #food
     case 'medium-activity':
      return #food
     case 'active':
      return #food
   case 'medium':
    match self.activity:
     case 'not-activity':
      return #food
     case 'medium-activity':
      return #food
     case 'active':
      return #food
   case 'large':
    match self.activity:
     case 'not-activity':
      return #food
     case 'medium-activity':
      return #food
     case 'active':
      return #food