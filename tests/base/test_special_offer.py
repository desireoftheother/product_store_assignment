from src.base.base_special_offer import BaseSpecialOffer
from mock_fixtures import mock_special_offer
from utils import MockGood


class TestSpecialOffers:
    def test_apply_special_offer(self, mock_special_offer: BaseSpecialOffer) -> None:
        original_goods_list = [MockGood()]
        assert [
            good.goods_name
            for good in mock_special_offer.apply_an_offer(original_goods_list)
        ] == ["MockOffer"]
