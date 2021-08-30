import os 

print(os.getcwd()) # This will get the current working directory

os.chdir("/users/allan/desktop")
print(os.getcwd())

os.makedirs("python test folder") # this creates "python test folder on the desktop"
