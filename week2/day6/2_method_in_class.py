'''Define a class called Cohort.
Use the __init__() method to create a division attribute that is passed to the constructor when an instance is instantiated.
Also create an attribute students: an empty list to hold students that may be added.
Define a method add_student that adds a student's name to the students list.
Implement __len__ so that it returns the number of students in the cohort.
Instantiate an instance of Cohort, pass the constructor "DAI", and store it in the variable dai_cohort_003. Add three students to the cohort.
Feel free to print the attributes to the console to demonstrate that each instance has it's own, independent attributes.'''


class Cohort():

    def __init__(self, division):
        self.division = division
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def __len__(self):
        return len(self.students)


# instantiate an instance
dai_cohort_003 = Cohort("DAI")


# add three students to the cohort
dai_cohort_003.add_student("Jaime")
dai_cohort_003.add_student("Matt")
dai_cohort_003.add_student("Mike")
