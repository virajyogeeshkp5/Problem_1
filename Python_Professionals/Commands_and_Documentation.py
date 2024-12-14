# commands and documentation
# single line command
print("Hello World")

# programmatically accesing docstring
def func():
    """This is a function that does not nothing at all"""
    return
print(func.__doc__)

help(func)

