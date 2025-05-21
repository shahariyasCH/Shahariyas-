
class Calculator:

    def __init__(self, a:float, b:float, operation:str):

        self.a=a
        self.b=b
        self.operation=operation.lower()

    def calculate(self):

       if self.operation=="add"or'+':
            return self.a + self.b
       elif self.operation=="sub"or'-':
            return self.a - self.b
       elif self.operation=="mul"or'*':
            return self.a * self.b
       elif self.operation=="div"or'/':
            if self.b!=0:
                return self.a / self.b
            else:
                return "error div by zero"
            
       else:
           return "invalid opreation"

a=float(input("Enter the number (a):"))
b=float(input("Enter the number (b):"))
operation=input("Enter the operation like add,sub...")

cal=Calculator(a, b, operation)
result=cal.calculate()
print('Result:',result)
