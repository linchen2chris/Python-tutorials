from inheritance import SchoolMember, Teacher, Student


def test_SchoolMember():
    chen = SchoolMember('chen')
    assert chen.getName() == 'chen'


def test_Teacher():
    chen = Teacher('chen', 5000)
    #    assert chen.getName() == 'chen'
    assert chen.getSalary() == 5000


def test_Student():
    chen = Student('chen', 60)
    #   assert chen.getName() == 'chen'
    assert chen.getMark() == 60
