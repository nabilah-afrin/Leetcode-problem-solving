class dog:   #define the blueprint for object       
    def __init__(self, name, color):
        self.dog_name = name
        self.color = color
    def update_color(self, color): #we have to pass the argument here, because we will have to change the variable, self.color will cerate the space
        self.color = color
    def view(self):   # no need to pass the variables that have been already declared, because we already declared it in _init_
        print( self.dog_name, "is", self.color) #always self.variable_name hbe

d1 = dog("pocol","white")
d1.view()
d1.update_color("blue")
d1.view()
#suppose i want to see the attribute and their values of the object. dictionary using will automatically shpw the attibuutes that i have created with their values
print(d1.__dict__)
print(dir(d1)) #shows the varibales and methods