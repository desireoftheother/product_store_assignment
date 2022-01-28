from base.base_goods import BaseGood, BaseOfferGood
from base.base_special_offer import BaseSpecialOffer


class MockGood(BaseGood):
    @property
    def price(self) -> float:
        return 666

    @property
    def measure_unit(self) -> str:
        return "foo"

    @property
    def goods_name(self) -> str:
        return "Bar"

    @property
    def goods_type(self) -> str:
        return "product"


class MockOfferGood(BaseOfferGood):
    @property
    def price(self) -> float:
        return 333

    @property
    def measure_unit(self) -> str:
        return "Kilometers"

    @property
    def goods_name(self) -> str:
        return "MockOffer"

    @property
    def discount(self) -> float:
        return 42

    @property
    def offer_description(self) -> str:
        return "MockGood 999% off:"


class MockSpecialOffer(BaseSpecialOffer):
    @property
    def goods_2_quantity_mapping(self) -> dict:
        """Mapping between specific goods and count which is needed to be present in order
        for special offer applying"""
        return {MockGood(): 1}

    @property
    def mock_good(self) -> BaseGood:
        """Goods object which will substitute that goods that are used in offer"""
        return MockOfferGood()


class MockAvailableAssortment:
    """Class which stores available assortment for our shop
    in form of mapping between the goods name and actual object"""

    NAME2GOOD_MAPPING: dict = {
        "Bar": MockGood(),
    }
