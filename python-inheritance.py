class SchoolMember:
    '''description'''

    def __init__(self, name):
        print("init SchoolMember %s" % name)


class Teacher(SchoolMember):
    '''teachers'''

    def __init__(self, name, salary):
        SchoolMember(name)
        print("init Teacher %s" % salary)


class Student(SchoolMember):
    '''student'''

    def __init__(self, name, mark):
        SchoolMember(name)
        print("init Student %s" % mark)


Teacher("linChen", 7700)
Student("chris", 100)
