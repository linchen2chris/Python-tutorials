class SchoolMember:
    '''description'''

    name = ''

    def __init__(self, name):
        self.name = name
        print("init SchoolMember %s" % name)

    def getName(self):
        return self.name


class Teacher(SchoolMember):
    '''teachers'''

    salary = 0

    def __init__(self, name, salary):
        SchoolMember(name)
        self.salary = salary
        print("init Teacher %s" % salary)

    def getSalary(self):
        return self.salary


class Student(SchoolMember):
    '''student'''

    mark = 0

    def __init__(self, name, mark):
        SchoolMember(name)
        self.mark = mark
        print("init Student %s" % mark)

    def getMark(self):
        return self.mark
