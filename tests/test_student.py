from models.student import Student
from test_teacher import MockCourse


def make_student() -> Student:
    return Student("Jean", "Dupont", 42)


def test_student_init():
    assert isinstance(make_student(), Student)


# ATTENTION : le test ne passe pas individuellement
def test_student_str():
    student = make_student()
    assert str(student) == "Jean Dupont (42 ans), n° étudiant : 2"


def teststudent_post_init():
    student = make_student()
    assert student.student_nbr == 3


def teststudent_add_course():
    student = make_student()
    course = MockCourse()
    assert len(student.courses_taken) == 0
    student.add_course(course)
    assert len(student.courses_taken) == 1
    assert student.courses_taken[0] == course
