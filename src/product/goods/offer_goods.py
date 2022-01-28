from src.base.base_goods import BaseOfferGood
from src.product.goods.regular_goods import Apples, Soup, Bread


class ApplesOfferGood(BaseOfferGood):
    """Placeholder class for invalid input cases"""

    @property
    def price(self) -> float:
        return Apples().price * (1 - self.discount)

    @property
    def measure_unit(self) -> str:
        return ""

    @property
    def goods_name(self) -> str:
        return "ApplesOffer"

    @property
    def discount(self) -> float:
        return Apples().price * 0.1

    @property
    def offer_description(self) -> str:
        return "Apples 10% off:"


class SoupBreadGood(BaseOfferGood):
    """Placeholder class for invalid input cases"""

    @property
    def price(self) -> float:
        return 2 * Soup().price + Bread().price * (1 - self.discount)

    @property
    def measure_unit(self) -> str:
        return ""

    @property
    def goods_name(self) -> str:
        return "SoupBreadOffer"

    @property
    def discount(self) -> float:
        return Bread().price * 0.5

    @property
    def offer_description(self) -> str:
        return "2 tins of soup and bread for half price:"
