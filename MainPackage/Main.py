'''
Name: Alex Bridge, Jon Buck, Grace Hertzfeld, Aria Nielsen
email:  bridgeax@mail.uc.edu, buckjn@mail.uc.edu, hertzfgc@mail.uc.edu, nielseai@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This assignment demonstrates that we can develop a project with classes to model something 
in the real world using github and eclipse
Anything else that's relevant:
'''

from ClassPackages.PopClass import *
from ClassPackages.CoffeeClass import *
from ClassPackages.DrinkMixerClass import *

drink1 = Pop('PepsiCo', 'Diet Pepsi')
drink3 = Pop('Nestle', 'Pure Life')
drink2 = Coffee(200, 195)
drink4 = Coffee(201, 197)
drink5 = DrinkMixer('Vodka','Soda')
drink6 = DrinkMixer('Whiskey','Lemon')

drink2.enforceTemperature(drink2.degree)
print(drink2.__str__())
drink3.validateBrand(drink3.brand)
print(drink1.__str__())
drink5.checkDrinks(drink5.drinkOne, drink5.drinkTwo)
print(drink5.__str__())