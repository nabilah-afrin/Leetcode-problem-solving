"""
    def product(self, num1, num2):
        print(num1 + num2)
    def product(self, num1, num2,num3):
        print(num1 + num2 +num3)
        

c1 = mycalculator()
c1.product(2,3)
c1.product(9,10,11)

#it will show error.because there are two methods with sem name which is not allowed
#basically in this code the last method was saved , and the first call was with the first method, but the saved one is what python rembers.so it shows error"""

#to prevent method overloading 
class mycalculator:
  
    
    def product(self, num1, num2 = None,num3 =None):
        if num1 != None and num2 != None and num3   != None:
            print(num1+num2+num3)
        elif num1 != None and num2 != None:
            print((num2+num1))
        else:
            print(1*num1)

#if theres a lots of numbes
class mycalculator:
   
    def product(self, *num):
        sum = 1
        for x in num:
            sum = sum + x
        print(sum)


#another method: dispatch

class mycalculator:
    """def __init__(self, num1, num2):
        self.first_number = num1
        self.second_number = num2"""
    @dispatch(int, int)
    def product(self, num1, num2):
        print(num1 + num2)
    @dispatch(int, int, int)
    def product(self, num1, num2,num3):
        print(num1 + num2 +num3)   #when object is tsring use string in dispatch

