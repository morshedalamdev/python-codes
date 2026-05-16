"""Importing flat files from the web with urllib"""

# from urllib.request import urlretrieve
# import pandas as pd

# # assign url of file:
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
# urlretrieve(url, "data/winequality-white.csv")  # save file locally

# # read file into DataFrame & print its head
# df = pd.read_csv("data/winequality-white.csv", sep=";")
# print(df.head())


"""Importing flat files from the web with pandas"""
# import matplotlib.pyplot as plt
# import pandas as pd

# # assign url of file:
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"

# # read file into DataFrame & print its head
# df = pd.read_csv(url, sep=";")
# print(df.head())

# # Plot first column of df
# df.iloc[:, 0].plot.hist()
# plt.xlabel("fixed acidity")
# plt.ylabel("count")
# plt.show()


""" Importing non-flat files from the web with pandas"""
# import pandas as pd
# import xlrd

# # assign url of file:
# url = "https://assets.datacamp.com/course/importing_data_into_r/latitude.xls"

# # read in all sheets of Excel file
# xls = pd.read_excel(url, sheet_name=None)

# print(xls.keys())  # print the sheetnames to the shell
# print(xls["1700"].head())  # print the head of the sheet named "1700" to the shell


""" Performing HTTP requests in Python using urllib """
# from urllib.request import urlopen, Request

# # Specify the url
# url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# request = Request(url)  # This packages the request
# response = urlopen(request)  # Sends the request and catches the response

# html = response.read()  # Extract the response

# print(type(response))  # Print the datatype of response
# print(html)  # Print the html
# response.close()  # Be polite and close the response!


""" Performing HTTP requests in Python using requests """
# import requests

# # Specify the url
# url = "http://www.datacamp.com/teach/documentation"

# # Packages the request, send the request and catch the response
# r = requests.get(url)

# text = r.text  # Extract the response

# print(text)  # Print the html


""" Parsing HTML with BeautifulSoup """
# from bs4 import BeautifulSoup
# import requests

# url = "https://www.python.org/~guido/"  # Specify url

# # Package the request, send the request and catch the response
# r = requests.get(url)

# html_doc = r.text  # Extracts the response as html

# soup = BeautifulSoup(html_doc)  # Create a BeautifulSoup object from the HTML

# pretty_soup = soup.prettify()  # Prettify the BeautifulSoup object
# guido_title = soup.title  # Get the title of webpage
# guido_text = soup.text  # Get the text of webpage
# a_tags = soup.find_all("a")  # Get all the a tags of webpage

# print(pretty_soup)  # Print the response
# print(guido_title)  # Print the title of the webpage
# print(guido_text)  # Print the text of the webpage

# # Print the URLs to the shell
# for link in a_tags:
#     print(link.get("href"))


""" Loading and exploring a JSON """
# import json

# # Load JSON
# with open("a_movie.json") as json_file:
#     json_data = json.load(json_file)

# # Print each key-value pair in json_data
# for k in json_data.keys():
#     print(k + ": ", json_data[k])


""" JSON from the web to Python """
import requests

# Assign URL to variable
url = "http://www.omdbapi.com/?apikey=72bc447a&t=social+network"

# Package the request, send the request and catch the response
r = requests.get(url)

# Decode the JSON data into a dictionary
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ": ", json_data[k])
