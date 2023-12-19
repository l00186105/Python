"""
Class template by JOR

Revision History
06OCT22: Alpha
11OCT23: Beta
"""

class MyTemplate():
   # Constructor, called whenever an instance of the class is created.
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        # Take in an argument and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2

# Instantiate the class
        
my_object = MyTemplate("John", True)

# Check the object and type
print(type(my_object))
