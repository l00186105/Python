# Define a class object attribute, it will be the same for any instance of the class
    class_object_attribute1 = 6378137
    class_object_attribute2 = 6356752 

# Instantiate the class
my_object = MyTemplate("John", True)
# Check the object
print(my_object.semi_major_axis, my_object.semi_minor_axis)