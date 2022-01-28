from src.base.base_special_offer import BaseSpecialOffer
from src.base.base_goods import BaseGood
from src.product.goods.regular_goods import Apples
from src.product.goods.offer_goods import ApplesOfferGood


class ApplesOffer(BaseSpecialOffer):
    @property
    def goods_2_quantity_mapping(self) -> dict:
        """Mapping between specific goods and count which is needed to be present in order
        for special offer applying"""
        return {
            Apples(): 1
        }

    @property
    def mock_good(self) -> BaseGood:
        """Goods object which will substitute that goods that are used in offer"""
        return ApplesOfferGood()
