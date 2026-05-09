"""READING A TEXT FILE"""
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
# import numpy as np
# filename = 'data/huck_finn.txt'
# data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0, 1])
# # Load data from a text file, skipping the first row (header)
# # default delimiter is whitespace, but here we specify a comma for CSV files
# # usecols specifies which columns to read (0 and 1 in this case)
# print(data)


""" PANDAS IMPORT """
# import pandas as pd
# filename = 'data/huck_finn.txt'
# data = pd.read_csv(filename, delimiter=',') # Read a CSV file into a DataFrame
# data = pd.read_csv(filename, nrows=10, header=None) # nrows specifies how many rows to read, header=None indicates that the file does not have a header row
# print(data.head()) # Print the first few rows of the DataFrame

# data_array = data.to_numpy() # Convert the DataFrame to a NumPy array
# print(data_array)


""" PICKLED FILES """
# import pickle
# with open("pickled_data.pkl", "rb") as file:  # 'rb' stands for 'read binary'
#     data = pickle.load(file)  # Load the pickled data
# print(data)


""" Excel spreadsheet """
# import pandas as pd
# file = 'urbanpop.xlsx'
# data = pd.ExcelFile(file)  # Load the Excel file
# print(data.sheet_names)  # Print the names of the sheets in the Excel file

# df1 = data.parse('1960-1965')  # Parse the sheet named '1960-1965' into a DataFrame
# df2 = data.parse(0) # Parse the first sheet (index 0) into a DataFrame


""" IMPORTING SAS FILES """
# import pandas as pd
# from sas7BDAT import SAS7BDAT
# with SAS7BDAT('urbanpop.sas7bdat') as file:
#     df_sas = file.to_data_frame() # Convert the SAS file to a DataFrame


""" IMPORTING STATA FILES """
# import pandas as pd
# data = pd.read_stata('urbanpop.dta') # Read a Stata file into a DataFrame
# print(data.head()) # Print the first few rows of the DataFrame


""" IMPORTING HDF5 FILES """
# import h5py
# filename = 'data/urbanpop.hdf5'
# data = h5py.File(filename, 'r') # 'r' stands for 'read'

# Structure of HDF5 files is hierarchical, similar to a file system, with groups and datasets
for key in data.keys():
    print(key) # Print each key (dataset) in the HDF5 file

for key in data['meta'].keys():
    print(key) # Print each key in the 'meta' group of the HDF5 file

print(np.array(data['meta']['description']), np.array(data['meta']['source'])) # Print the 'description' and 'source' datasets from the 'meta' group