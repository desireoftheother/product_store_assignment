from src.base.base_goods import BaseGood


class Soup(BaseGood):
    @property
    def price(self) -> float:
        return 0.65

    @property
    def measure_unit(self) -> str:
        return "tin"

    @property
    def goods_name(self) -> str:
        return "Soup"

    @property
    def goods_type(self) -> str:
        return "product"


class Bread(BaseGood):
    @property
    def price(self) -> float:
        return 0.80

    @property
    def measure_unit(self) -> str:
        return "loaf"

    @property
    def goods_name(self) -> str:
        return "Bread"

    @property
    def goods_type(self) -> str:
        return "product"


class Milk(BaseGood):
    @property
    def price(self) -> float:
        return 1.30

    @property
    def measure_unit(self) -> str:
        return "bottle"

    @property
    def goods_name(self) -> str:
        return "Milk"

    @property
    def goods_type(self) -> str:
        return "product"


class Apples(BaseGood):
    @property
    def price(self) -> float:
        return 1.00

    @property
    def measure_unit(self) -> str:
        return "bag"

    @property
    def goods_name(self) -> str:
        return "Apples"

    @property
    def goods_type(self) -> str:
        return "product"
