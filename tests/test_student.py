from datetime import date

import pytest

from models.course import Course
from models.student import Student


@pytest.fixture
def mock_course():
    return Course("Mathématiques", date(2024, 1, 31), date(2025, 1, 31))


def make_student() -> Student:
    return Student("Jean", "Dupont", 42)


class TestStudent:

    def test_student_init(self):
        assert isinstance(make_student(), Student)

    # ATTENTION : ce test ne passe pas individuellement
    def test_student_str(self):
        student = make_student()
        assert str(student) == "Jean Dupont (42 ans), n° étudiant : 2"

    def teststudent_post_init(self):
        student = make_student()
        assert student.student_nbr == 3

    def teststudent_add_course(self, mock_course):
        student = make_student()
        assert len(student.courses_taken) == 0
        student.add_course(mock_course)
        assert len(student.courses_taken) == 1
        assert student.courses_taken[0] == mock_course
