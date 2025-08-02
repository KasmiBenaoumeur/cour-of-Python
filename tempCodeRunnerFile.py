import os # os module is used to interact with the operating system

print(os.getcwd()) # Get Current Working Directory

print(os.path.dirname(os.path.abspath(__file__))) # Get Current File Directory

print(os.path.abspath(__file__)) # Get Current File Full Path

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Change Current Working Directory To Current File Directory
print(os.getcwd())