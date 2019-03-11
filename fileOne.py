def func():
    print("Function running in fileOne.py")
print("Top level print in fileOne.py")

if __name__ == "__main__":
    print("FileOne.py is being run directly")
else:
    print("FileOne.py is being imported")
    print("Name is "+ __name__)