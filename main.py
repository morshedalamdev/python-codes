""" READING A TEXT FILE """
filename = 'data/huck_finn.txt'
file = open(filename, mode='r') # 'r' stands for 'read'
text = file.read()
file.close() # Always close the file after you're done with it

""" WRITING TO A FILE """
filename = 'data/huck_finn.txt'
file = open(filename, mode='w') # 'w' stands for 'write'
file.write("Hello, World!")
file.close() # Always close the file after you're done with it

""" CONTEXT MANAGER WITH """
with open('data/huck_finn.txt', 'r') as file:
    text = file.read()
    print(text)