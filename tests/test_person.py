from models.person import Person


def make_person() -> Person:
    return Person("Jean", "Dupont", 42)


def test_person_init():
    assert isinstance(make_person(), Person)


def test_person_attributes():
    person = make_person()

    assert isinstance(person.first_name, str)
    assert isinstance(person.last_name, str)
    assert isinstance(person.age, int)

    assert person.address is None
    assert person.first_name == "Jean"
    assert person.last_name == "Dupont"
    assert person.age == 42


def test_person_str():
    person = make_person()
    assert str(person) == "Jean Dupont (42 ans)"

