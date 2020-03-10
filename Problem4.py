# Fernando Valadez-Nunez
# 03/09/2020

# Write a function that takes a year as a parameter and returns True if the
# year is a leap year, False if it is otherwise

# Requirements: The year is evenly divisible by 4
#               The year can be evenly divided by 100 it is not a leap year,
#               umless: The year is also evenly divisible by 400. Then it is
#               a leap year


def isLeapYear(year):
  
    if year % 4 == 0 and year % 100 != 0:
           
          return(True)
      
    elif year % 100 == 0 and year % 400 == 0:
    
          return (True)
          
    else:
          return (False)
        
print (isLeapYear(1996))
