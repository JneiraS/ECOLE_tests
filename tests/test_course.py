from datetime import date

from models.course import Course


def make_course() -> Course:
    return Course("Test Course",
                  date(2024, 1, 1),
                  date(2024, 1, 31))


class MockTeacher:
    @staticmethod
    def get_instance():
        return {"first_name": "Jean",
                "last_name": "Dupont", "age": 42,
                "hiring_date": date(2024, 1, 1)}

    def return_full_name(self) -> str:
        return f"{self.get_instance()['first_name']} {self.get_instance()['last_name']}"


def test_course_init():
    course = make_course()
    assert isinstance(course, Course)


def test_attributes():
    course = make_course()
    assert course.name == 'Test Course'
    assert course.start_date == date(2024, 1, 1)
    assert course.end_date == date(2024, 1, 31)


def test_str_no_teacher():
    course = make_course()
    assert str(course) == "Test Course (2024-01-01 – 2024-01-31),\npas d'enseignant affecté"


def test_str_with_teacher():
    course = make_course()
    teacher = MockTeacher().return_full_name()

    course.teacher = teacher
    expected_str = "Test Course (2024-01-01 – 2024-01-31),\nenseigné par Jean Dupont"
    assert str(course) == expected_str
