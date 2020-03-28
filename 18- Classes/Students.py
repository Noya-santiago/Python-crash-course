""" a class is basically a bunch of code that acumullate a bunch of data. Its hard to explain , is like if you wanted to describe an object
with measurements or values """


class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        