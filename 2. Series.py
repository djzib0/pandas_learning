import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[1])

b = [1, 7, 2]

myvar = pd.Series(b, index= ['x', 'y', 'z'])
print(myvar)
print(myvar['y'])

# Create panda Series from a dictionary
calories = {'day1': 420, 'day2': 380, 'day3': 390}
myvar = pd.Series(calories)
print(myvar)
print(myvar[2])
print(myvar['day3'])

# Creates a Series using only data from 'day1' and 'day2'
calories = {'day1': 420, 'day2': 380, 'day3': 390}
myvar = pd.Series(calories, index=['day2', 'day1'])
print(myvar)