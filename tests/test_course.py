from datetime import date

from models.course import Course


def make_course() -> Course:
    return Course("Test Course",
                  date(2024, 1, 1),
                  date(2024, 1, 31))


class MockTeacher:
    def __init__(self):
        self.first_name = "Jean"
        self.last_name = "Dupont"
        self.hiring_date = date(2024, 1, 1)
        self.courses_teached = []

    def return_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class MockStudent:
    def __init__(self, courses_taken=[]):
        self.courses_taken = courses_taken


class TestsCourse:
    def test_course_init(self):
        course = make_course()
        assert isinstance(course, Course)

    def test_attributes(self):
        course = make_course()
        assert course.name == 'Test Course'
        assert course.start_date == date(2024, 1, 1)
        assert course.end_date == date(2024, 1, 31)

    def test_str_no_teacher(self):
        course = make_course()
        assert str(course) == "Test Course (2024-01-01 – 2024-01-31),\npas d'enseignant affecté"

    def test_str_with_teacher(self):
        course = make_course()
        teacher = MockTeacher().return_full_name()

        course.teacher = teacher
        expected_str = "Test Course (2024-01-01 – 2024-01-31),\nenseigné par Jean Dupont"
        assert str(course) == expected_str

    def test_set_teacher(self):
        course = make_course()
        teacher = MockTeacher()
        assert course.teacher is None
        course.set_teacher(teacher)
        assert course.teacher == teacher

    def test_add_student(self):
        course = make_course()
        student = MockStudent()
        course.add_student(student)
        assert course.students_taking_it == [student]
