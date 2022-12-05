'''
Defining and calling classes
'''


class OurClass():

    def __init__(self, name):
        self.name = name


our_python_class = OurClass('Intro Python')

our_ds_class = OurClass('Data Science')

print(our_python_class.name)

print(our_ds_class.name)
