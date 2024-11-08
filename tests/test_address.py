import pytest

from models.address import Address


@pytest.fixture
def make_address() -> Address:
    return Address("12 rue des Pinsons", "Castanet", 31320)


class TestAddress:

    def test_address_init(self, make_address):
        assert isinstance(make_address, Address)

    def test_address_attributes(self, make_address) -> None:
        assert isinstance(make_address.street, str)
        assert isinstance(make_address.city, str)
        assert isinstance(make_address.postal_code, int)

    def test_address_street(self, make_address) -> None:
        assert make_address.street == "12 rue des Pinsons"

    def test_address_city(self, make_address) -> None:
        assert make_address.city == "Castanet"

    def test_address_postal_code(self, make_address) -> None:
        assert make_address.postal_code == 31320

    def test_address_str(self, make_address) -> None:
        assert str(make_address) == "12 rue des Pinsons, 31320 Castanet"

    def test_address_str_all_none(self):
        assert str(Address(None, None, None)) == "None, None None"
