##importing math
"""import math

print("Square root of 36:", math.sqrt(36))
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print("Power of 2^3:", math.pow(2, 3))"""

##importing random
"""import random

print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))
"""

##datetime library
"""import datetime

today = datetime.date.today()
print("Today's date is:", today)

now = datetime.datetime.now()
print("Current time:", now.strftime("%H:%M:%S")) """

#numpy library

"""import numpy as np

# Create a simple array
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)

# Perform operations
print("Array * 2:", my_array * 2)         # Multiply each element by 2
print("Mean:", np.mean(my_array))        # Average of the array
print("Square Roots:", np.sqrt(my_array))

# array from 10 to 50
my_array = np.array([range(10,50)])
#print("Array: ", my_array)

max_value = np.max(my_array)
min_value = np.min(my_array)
print("Max Value: ", max_value)
print("Min value: ", min_value)
print("Array * 3: ", my_array * 3)"""

import pandas as pd

# Create a DataFrame (table-like structure)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)

print(df)

# Access column
print("Names:", df['Name'])

# Filter rows
print("Scores above 90:")
print(df[df['Score'] > 90])