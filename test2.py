data = [0,1,2]
print data
print data
print data

class TheClass(object):
    def __init__(self, name, sex, age):
        """
        In initiation, basic data are stored in the instance.
        name: Str. First name only.
        sex: Int.
        age: Int.
        """
        self.name = name
        self.sex = sex
        self.age = age
