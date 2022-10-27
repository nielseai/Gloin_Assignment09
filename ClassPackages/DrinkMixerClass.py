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

class DrinkMixer():
    #set variables and check against "inventory list"
    def setDrinks(self,inputOne,inputTwo):
        self.checkDrinks(inputOne,inputTwo)
    
    #check if the drinks are in a list of in stock options and provide feedback to the user
    def checkDrinks(self,drinkOne,drinkTwo):
        drinkList = ['Vodka','Whiskey','Rum','Coke','Sour','Soda','Cranberry','Lime']
        if drinkOne in drinkList and drinkTwo in drinkList:
            self.drinkOne = drinkOne
            self.drinkTwo = drinkTwo
        elif drinkOne in drinkList and drinkTwo not in drinkList:
            self.drinkOne = drinkOne
            print(drinkTwo + " is not a drink that is offered.")
        elif drinkOne not in drinkList and drinkTwo in drinkList:
            self.drinkTwo = drinkTwo
            print(drinkOne + " is not a drink that is offered.")
        else:
            print(drinkOne + " and " + drinkTwo + " are not drinks that are available.")
    
    #initializing variables
    def __init__(self, drinkOne, drinkTwo):
        self.drinkOne = drinkOne
        self.drinkTwo = drinkTwo
    
    #Return a string of drinks to be mixed
    def __repr__(self):
        return 'Drinks to mix: ' + self.drinkOne + " and " + self.drinkTwo
    
    #Return a "fancy" string of the drinks to be mixed   
    def __str__(self):
        return 'Drinks to mix: ' + self.drinkOne + " and " + self.drinkTwo
    
    # "mix the drinks" and output the resulting combination
    def mixDrinks(self,drinkOne,drinkTwo):
        return "Mixing your drinks made a " + drinkOne + " " + drinkTwo + "!"
    