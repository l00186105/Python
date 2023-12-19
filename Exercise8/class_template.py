def my_method1(self):
    if self.attr2:
        print(f"Good morning {self.attr1}")
    else:
        print(f"No greeting {self.attr1}")

my_object.my_method1()        
def my_method2(self, my_name:str):
    if self.attr2:
        print(f"Good morning {my_name}")
    else:
        print(f"No greeting {my_name}")
        my_object.my_method2(“Slartibartfast”)
                             
                          