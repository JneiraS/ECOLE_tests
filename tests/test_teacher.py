from datetime import date

from models.teacher import Teacher


def make_teacher() -> Teacher:
    return Teacher("Jean", "Dupont", 42, date(2024, 1, 1))


# MOOK
class MookCourse:
    @staticmethod
    def get_instance():
        return {"name": "Test Course",
                "start_date": date(2024, 1, 1),
                "end_date": date(2024, 1, 1),
                "teacher": {"first_name": "Jean", "last_name": "Dupont", "age": 42, "hiring_date": date(
                    2024, 1, 1)},
                "students_taking_it": []}


def test_teacher_attributes():
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


def test_add_course():
    teacher = make_teacher()
    course = MookCourse.get_instance()
    teacher.add_course(course)
    assert teacher.courses_teached == [course]


def test_teacher_str():
    teacher = make_teacher()
    assert str(teacher) == "Jean Dupont (42 ans), arrivé(e) le 2024-01-01"


if __name__ == "__main__":
    test_teacher_attributes()
    test_add_course()
    test_teacher_str()
