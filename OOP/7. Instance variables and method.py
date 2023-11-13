class Car:
    def __init__(self, car_name, model_name):
        self.name = car_name                #instan variable
        self.model = model_name            #instan variable
        self.wheels = 4            #instan variable

    def view(self):    #instance method
        print('model_name:' , self.name, self.model) #use the name defined in the class, not your variable

car_1 = Car("bmw", 2016) #objec 1
car_2 = Car('audi', 2019)

car_2.wheels = 6 #will show 6 wheels not 4

car_1.view()
car_2.view()
