import os 

print(os.getcwd()) # This will get the current working directory

os.chdir("/users/allan/desktop")
print(os.getcwd())

os.makedirs("python test folder") # this creates "python test folder on the desktop"

os.path.isfile("test.docx") # Checks to see if the file test.docx exists

os.path.isdir("python test folder") # Checks to see if the directory exists

os.remove("test.docx") # Removes file called test.docx doesn't remove folders

os.removedirs("python test folder") # removes folder