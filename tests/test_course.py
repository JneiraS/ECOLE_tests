from datetime import date

import pytest

from models.course import Course


@pytest.fixture
def course() -> Course:
    return Course("Test Course", date(2024, 1, 1), date(2024, 1, 31))


@pytest.fixture
def mock_teacher():
    class MockTeacher:
        def __init__(self):
            self.first_name = "Jean"
            self.last_name = "Dupont"
            self.hiring_date = date(2024, 1, 1)
            self.courses_teached = []

        def return_full_name(self) -> str:
            return f"{self.first_name} {self.last_name}"

    return MockTeacher()


@pytest.fixture
def mock_student():
    class MockStudent:
        def __init__(self, courses_taken=[]):
            self.courses_taken = courses_taken

    return MockStudent()


class TestsCourse:
    def test_course_init(self, course):
        assert isinstance(course, Course)

    def test_attributes(self, course):
        assert course.name == "Test Course"
        assert course.start_date == date(2024, 1, 1)
        assert course.end_date == date(2024, 1, 31)

    def test_str_no_teacher(self, course):
        assert str(course) == (
            "Test Course (2024-01-01 – 2024-01-31)," "\npas d'enseignant affecté"
        )

    def test_str_with_teacher(self, course, mock_teacher):
        course.teacher = mock_teacher.return_full_name()
        expected_str = (
            "Test Course (2024-01-01 – 2024-01-31)," "\nenseigné par Jean Dupont"
        )
        assert str(course) == expected_str

    def test_set_teacher(self, course, mock_teacher):
        assert course.teacher is None
        course.set_teacher(mock_teacher)
        assert course.teacher == mock_teacher

    def test_add_student(self, course, mock_student):
        course.add_student(mock_student)
        assert course.students_taking_it == [mock_student]
