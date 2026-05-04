""" READING A TEXT FILE """
# filename = 'data/huck_finn.txt'
# file = open(filename, mode='r') # 'r' stands for 'read'
# text = file.read()
# file.close() # Always close the file after you're done with it

""" WRITING TO A FILE """
# filename = 'data/huck_finn.txt'
# file = open(filename, mode='w') # 'w' stands for 'write'
# file.write("Hello, World!")
# file.close() # Always close the file after you're done with it

""" CONTEXT MANAGER WITH """
# with open('data/huck_finn.txt', 'r') as file:
#     text = file.read()
#     print(text)

""" NumPy IMPORT """
import numpy as np

filename = 'data/huck_finn.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0, 1]) 
# Load data from a text file, skipping the first row (header)
# default delimiter is whitespace, but here we specify a comma for CSV files
# usecols specifies which columns to read (0 and 1 in this case)
print(data)