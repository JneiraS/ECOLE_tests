from datetime import date

from models.teacher import Teacher


def make_teacher() -> Teacher:
    return Teacher("Jean", "Dupont", 42, date(2024, 1, 1))


class MockCourse:
    def __init__(self, students_taking_it=[]):
        self.name = "Test Course"
        self.start_date = date(2024, 1, 1)
        self.end_date = date(2024, 1, 1)
        self.teacher = {"first_name": "Jean", "last_name": "Dupont", "age": 42,
                        "hiring_date": date(2024, 1, 1)}
        self.students_taking_it = students_taking_it


class TestsTeacher:
    def test_teacher_attributes(self):
        teacher = make_teacher()

        assert isinstance(teacher.first_name, str)
        assert isinstance(teacher.last_name, str)
        assert isinstance(teacher.age, int)
        assert isinstance(teacher.hiring_date, date)

        assert teacher.address is None
        assert teacher.first_name == "Jean"
        assert teacher.last_name == "Dupont"
        assert teacher.age == 42
        assert teacher.hiring_date == date(2024, 1, 1)

    def test_add_course(self):
        teacher = make_teacher()
        course = MockCourse
        teacher.add_course(course)
        assert teacher.courses_teached == [course]

    def test_teacher_str(self):
        teacher = make_teacher()
        assert str(teacher) == "Jean Dupont (42 ans), arrivé(e) le 2024-01-01"
