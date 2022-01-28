from functools import reduce
from typing import List

from src.base.base_goods import BaseGood
from src.base.base_special_offer import BaseSpecialOffer
from src.product.available_assortment import AvailableAssortment
from src.io.io import WelcomeTextGenerator, InputHandler, OutputHandler


class MainApplication:
    """Class for handling main application functionality"""

    def __init__(
        self,
        available_assortment: AvailableAssortment,
        available_offers: List[BaseSpecialOffer],
    ):
        self.welcome_text_generator = WelcomeTextGenerator(available_assortment)
        self.input_validator = InputHandler(available_assortment)
        self.output_handler = OutputHandler()
        self.available_offers = available_offers

    def apply_offers(self, orders_list: List[BaseGood]):
        """Simple method for applying the all offers to the order list"""
        final_list = reduce(
            lambda goods_list, offer: offer.apply_an_offer(goods_list),
            self.available_offers,
            orders_list,
        )
        return final_list

    def execute_application(self) -> None:
        """Main method for executing the application"""
        self.welcome_text_generator.print_a_welcome_text()
        orders_list = self.input_validator.handle_input()
        final_list = self.apply_offers(orders_list)
        self.output_handler.generate_formatted_output(
            final_list, orders_list, self.available_offers
        )
