from src.base.base_goods import BaseGood


class InvalidGood(BaseGood):
    """Placeholder class for invalid input cases"""

    @property
    def price(self) -> float:
        return 0

    @property
    def measure_unit(self) -> str:
        return ""

    @property
    def goods_name(self) -> str:
        return "Invalid"

    @property
    def goods_type(self) -> str:
        return "invalid"
