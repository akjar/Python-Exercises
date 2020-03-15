# Exercise Two (User Inputs)

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input('What is your name?')
km = input('What is your distance in km?')

km_to_miles = round(float(km) / 1.609, 1)

print(f'Hello {name.capitalize()}! Your {km}km distance is {km_to_miles} miles.')