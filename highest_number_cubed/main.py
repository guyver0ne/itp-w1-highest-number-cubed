"""This is the entry point of the program."""


def highest_number_cubed(limit):
     initial = 1
     
     while True:
      if initial ** 3 > limit:
         return initial - 1 
        
      initial += 1
     
    
    
    
    