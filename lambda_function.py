lambda parameters:expression
def double(x):
    return x * 2
print(double(6))
double = lambda x: x * 2
multiply = lambda x,y: x * y
add = lambda x,y,z: x + y + z
full_name = lambda first_name, last_name: first_name+" " +last_name
age_check = lambda age: True if age >= 18 else False
print(age_check(17))
print(full_name("Lisbeth", "Paulino"))
print(double(8))
print(multiply(4,9))
print(add(2,4,6))
