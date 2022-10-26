'''
Name: Alex Bridge, Jon Buck, Grace Hertzfeld, Aria Nielsen
email: nielseai@mail.uc.edu, ____, hertzfgc@mail.uc.edu, _____# everyone put their email
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This assignment demonstrates that we can develop a project with classes to model something 
in the real world using github and eclipse
Anything else that's relevant:
'''

class Coffee:
    
    def setTemperature(self, degree):
        self.enforceTemperature(degree)
        
    def enforceTemperature(self, degree):
        if degree > 200:
            print('Coffee is too hot. Temperature needs to be between 196 and 200 degrees.')
        else:
            self.degree = degree
            
        if degree < 196:
            print('Coffee is not hot enough. Temperature needs to be between 196 and 200 degrees.')
        else:
            self.degree = degree
            
    # We are enforcing temperature of hot coffee
    
    def __init__(self, orderNumber, degree):
        self.orderNumber = orderNumber
        self.degree = degree
        
    def __repr__(self):
        'Return a string repr of coffee'
        return 'Order Number: ' + self.orderNumber

    def __str__(self):
        
        'Return an improved string of coffee'
        return 'OrderNumber: ' + str(self.orderNumber) + ', ' + 'Coffee Temperature: ' + str(self.degree)
    