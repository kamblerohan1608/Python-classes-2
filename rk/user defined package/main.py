
# Main file to access created packages

from package import simple_calc ,pattern,complex_calc

print(simple_calc.add(10,20))

print(simple_calc.sub(10,20))

print(simple_calc.mul(10,20))

print(simple_calc.div(10,20))

pattern.right_angle(5)

a = complex_calc.factorial(5)
print(a)