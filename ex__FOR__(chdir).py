

import os
# simulate running from another location:
os.chdir("C:\\Users\\HP\\Desktop")

print("Before changing directory:", os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
# then we switch to script folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("After changing directory:", os.getcwd())