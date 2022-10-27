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

class Pop():
    def validateBrand(self, brand):
        brands = ["Coca-Cola", "PepsiCo"]
        if brand in brands:
            self.brand = brand
        else:
            print("This is not a pop brand: " + brand)
    def __init__(self, brand, name):    
        self.brand = brand
        self.name = name              
    def __repr__(self):
        return "brand = " + self.brand + "; name = " + self.name
    def __str__(self):
        return "brand = " + self.brand + "; name = " + self.name
    def get_name(self):
        return self.get_name
    def set_name(self, x):
        self._name = x