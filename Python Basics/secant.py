from math import sin, cos

x1 = float(input('Enter x(n-1) number'))
x2 = float(input('Enter x(n-2) number'))
perror = float(input('Enter permissible error'))

def func_calc(x):
    #return x ** 3 - 20
    return(cos(x) + 2 * sin(x) + x ** 2)

def calcx():
    ff = func_calc(x1) - func_calc(x2)
    dd = (x1 - x2)/ff
    return x1 - (func_calc(x1) * dd)  
  
x = calcx()
func_x = func_calc(x)

while abs(func_x) >= perror:
    
    x2, x1 = x1, x 
    x = calcx()
    func_x = func_calc(x)
    
print("ROOT:", x1, x2)    

