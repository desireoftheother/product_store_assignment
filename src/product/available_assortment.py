from src.product.goods.regular_goods import *

from src.product.offers.soup_bread_offer import SoupBreadOffer
from src.product.offers.apples_offer import ApplesOffer

AVAILABLE_OFFERS = [SoupBreadOffer(), ApplesOffer()]


class AvailableAssortment:
    """Class which stores available assortment for our shop
    in form of mapping between the goods name and actual object"""

    NAME2GOOD_MAPPING: dict = {
        "Apples": Apples(),
        "Bread": Bread(),
        "Milk": Milk(),
        "Soup": Soup(),
    }
