from abc import ABC, abstractmethod


class BaseGood(ABC):
    """Base class for common goods property description"""

    @property
    @abstractmethod
    def price(self) -> float:
        """Price of this particular good per measure unit"""

    @property
    @abstractmethod
    def measure_unit(self) -> str:
        """Measure unit specified for this type of goods"""

    @property
    @abstractmethod
    def goods_name(self) -> str:
        """Name which is used to identify the good"""

    @property
    @abstractmethod
    def goods_type(self) -> str:
        """Type of good. Should be either product or invalid or offer"""


class BaseOfferGood(BaseGood):
    """Base class for offer goods property description"""

    @property
    @abstractmethod
    def discount(self) -> float:
        """Discount which will you get for the single applying of order"""

    @property
    @abstractmethod
    def offer_description(self) -> str:
        """Special offer description which will be printed on screen"""

    @property
    def goods_type(self) -> str:
        return "offer"
