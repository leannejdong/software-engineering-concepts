'''
Software engineering concepts

* Modularity

* Documentation

* Testing

* Version Control & Git

'''

# Modularity in Python

# Import the pandas PACKAGE
import pandas as pd
# Create some example data
data = {'x': [1,2,3,4], 'y':[20.1,62.5,34.8,42.7]}

# Create a dataframe CLASS object
df = pd.DataFrame(data)

# Use the plot METHOD
df.plot('x','y')