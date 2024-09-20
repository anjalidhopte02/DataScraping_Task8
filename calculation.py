# 4 extral function import and export 
##addtion, sub, div, mul

x=24
y=12

def calculation():

 if __name__== "__main__":
  def add(x, y):
    return x + y

  def subtract(x, y):
    

    return x - y

  def divide(x, y):
    

    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

  def multiply(x, y):
    
    return x * y 


print("Addition:", x+y)
print("Subtraction:", x-y)
print("Division:", x/y)
print("Multiplication:", x*y)
