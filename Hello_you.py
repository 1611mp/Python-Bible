# Ask User for name

name = input("What's your name?: ")

# Ask User for age

age = input("What's your age?: ")

# Ask User for city

city = input("In which city do you live?: ")

# Ask User what they enjoy

love = input("What you enjoy doing?: ")

# Create Output text

string = "Your name is {}, you are {} years old. You live in {} and you love {}."
output = string.format(name.title(),age,city.title(),love.title())

# Print output to screen

print(output)