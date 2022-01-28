import pytest
import mock
import builtins

from src.io.io import WelcomeTextGenerator, InputHandler, OutputHandler
from tests.utils import (
    MockGood,
    MockOfferGood,
    MockSpecialOffer,
    MockAvailableAssortment,
)


class TestWelcomeTextGenerator:
    def test_assert_stdout(self, capsys):
        generator = WelcomeTextGenerator(MockAvailableAssortment())
        generator.print_a_welcome_text()
        captured = capsys.readouterr()
        assert (
            captured.out
            == """Hello and welcome to our fellow shop!
Today we are having the following goods available:
Bar pricing 666 british pounds per foo
Please, enter your order in following format:
PriceBasket item1 item2 ... item 2
"""
        )


class TestInputHandler:
    @pytest.fixture()
    def handler(self) -> InputHandler:
        return InputHandler(MockAvailableAssortment())

    def test_handle_input(self, handler) -> str:
        with mock.patch.object(builtins, "input", lambda: "PriceBasket Bar Bar"):
            assert [item.goods_name for item in handler.handle_input()] == [
                "Bar",
                "Bar",
            ]


class TestOutputHandler:
    @pytest.fixture()
    def handler(self) -> OutputHandler:
        return OutputHandler()

    def test_handle_input(self, handler, capsys) -> str:
        orders_list = [MockGood(), MockGood()]
        final_list = [MockOfferGood()]
        available_offers = [MockSpecialOffer()]
        handler.generate_formatted_output(
            final_list=final_list,
            orders_list=orders_list,
            available_offers=available_offers,
        )
        captured = capsys.readouterr()
        reference_string = """Subtotal: 1332.00 British pounds
MockGood 999% off: 42.00 British pounds
Total: 333 British pounds
"""
        assert captured.out == reference_string
