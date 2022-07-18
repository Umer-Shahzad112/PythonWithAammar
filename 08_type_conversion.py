
x = 2       #integer
y = 2.      #float
z = 'hello' #string

print(type(x))
print(type(y))
print(type(z))

#implicit type conversion
print(type(x*y))
print(type(y*x))

#explicit type conversion
age = input('What is your age')
print(age ,type(age))

age = int(age)
print(age,type(age))

