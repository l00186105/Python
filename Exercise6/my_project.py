"""
project.py
"""
import reusable
print("Running code from the project")
print(reusable.my_square(4))

"""
reusable.py
"""
def my_square(a: int)->int:
    print("Running code from the module")
    return a*a

project.py
