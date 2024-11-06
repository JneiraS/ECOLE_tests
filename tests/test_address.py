from models.address import Address


def make_address() -> Address:
    """Factorielle pour cr er un objet Address."""
    return Address("12 rue des Pinsons", "Castanet", 31320)


class TestAddress:

    def test_address_init(self):
        assert isinstance(make_address(), Address)

    def test_address_attributes(self) -> None:
        address = make_address()
        assert isinstance(address.street, str)
        assert isinstance(address.city, str)
        assert isinstance(address.postal_code, int)

    def test_address_street(self) -> None:
        address = make_address()
        assert address.street == "12 rue des Pinsons"

    def test_address_city(self) -> None:
        address = make_address()
        assert address.city == "Castanet"

    def test_address_postal_code(self) -> None:
        address = make_address()
        assert address.postal_code == 31320

    def test_address_str(self) -> None:
        address = make_address()
        assert str(address) == "12 rue des Pinsons, 31320 Castanet"

    def test_address_str_all_none(self):
        assert str(Address(None, None, None)) == "None, None None"
