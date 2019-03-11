import fileOne
print("Top level print in fileTwo.py")
fileOne.func()

if __name__ == "__main__":
    print("fileTwo.py is being run directly")
else:
    print("fileTwo.py is being imported")
    print("Name is "+ __name__)