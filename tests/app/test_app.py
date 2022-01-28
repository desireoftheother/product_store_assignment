import builtins

import mock

from app.app import MainApplication

from tests.mock_fixtures import *


class TestMainApplication:
    @pytest.fixture
    def main_app(
        self, mock_available_assortment, mock_special_offer
    ) -> MainApplication:
        return MainApplication(
            available_assortment=mock_available_assortment,
            available_offers=[mock_special_offer],
        )

    def test_apply_offers(
        self, main_app: MainApplication, mock_good_fx, mock_offer_good
    ) -> None:
        applied_offers_list = main_app.apply_offers(
            [mock_good_fx, mock_good_fx, mock_good_fx]
        )
        assert [good.goods_name for good in applied_offers_list] == [
            good.goods_name for good in [mock_offer_good] * 3
        ]

    def test_execute_application(
        self,
        capsys,
        main_app: MainApplication,
    ) -> None:
        with mock.patch.object(builtins, "input", lambda: "PriceBasket Bar Bar"):
            main_app.execute_application()
            captured = capsys.readouterr().out
            reference_string = """Hello and welcome to our fellow shop!
Today we are having the following goods available:
Bar pricing 666 british pounds per foo
Please, enter your order in following format:
PriceBasket item1 item2 ... item 2
Subtotal: 1332.00 British pounds
MockGood 999% off: 84.00 British pounds
Total: 666 British pounds
"""
            assert captured == reference_string
