from typing import List
from decimal import Decimal

from src.product.available_assortment import AvailableAssortment
from src.base.base_special_offer import BaseSpecialOffer
from src.base.base_goods import BaseGood
from src.product.goods.service_goods import InvalidGood


class WelcomeTextGenerator:
    """Class which is responsible for welcome text generation"""

    def __init__(self, available_assortment: AvailableAssortment):
        self.available_assortment: dict = available_assortment.NAME2GOOD_MAPPING

    def print_a_welcome_text(self):
        print(
            """Hello and welcome to our fellow shop!
Today we are having the following goods available:"""
        )
        for item in self.available_assortment.values():
            print(
                f"{item.goods_name} pricing {item.price} british pounds per {item.measure_unit}"
            )
        print(
            """Please, enter your order in following format:
PriceBasket item1 item2 ... item 2"""
        )


class InputHandler:
    """Class which is responsible to receive the valid input"""

    def __init__(self, available_assortment: AvailableAssortment):
        self.available_assortment: dict = available_assortment.NAME2GOOD_MAPPING

    def handle_input(self) -> List[BaseGood]:
        """Method for receiving the validated input for goods basket"""
        goods_list_obj = self.__map_goods_name_to_obj(
            (self.__receive_validated_input_string())
        )
        invalidity_check = sum(
            [isinstance(item, InvalidGood) for item in goods_list_obj]
        )
        if invalidity_check > 0:
            print("""Please, check the spelling and try again""")
            goods_list_obj = self.handle_input()
        return goods_list_obj

    def __receive_validated_input_string(self) -> str:
        """Method for receiving and validating input strings"""
        input_basket = input()
        if not input_basket.startswith("PriceBasket"):
            print("Please, enter your order starting with PriceBasket")
            input_basket = self.handle_input()
        return input_basket

    def __map_goods_name_to_obj(self, input_string: str) -> List[BaseGood]:
        """Method which maps input string to the list of actual goods"""
        goods_list_obj: List[BaseGood] = list(
            map(self.__safely_map_name_to_good_obj, input_string.split(" ")[1:])
        )
        return goods_list_obj

    def __safely_map_name_to_good_obj(self, item_name: str) -> BaseGood:
        """Method which maps good name to the goods object with a bit of validation process"""
        try:
            good_obj = self.available_assortment[item_name]
        except KeyError:
            print(f"""Unfortunately, we don't have a good with name {item_name}.""")
            good_obj = InvalidGood()
        return good_obj


class OutputHandler:
    def generate_formatted_output(
        self,
        final_list: List[BaseGood],
        orders_list: List[BaseGood],
        available_offers: List[BaseSpecialOffer],
    ) -> None:
        """Method for generating the formatted output of application"""
        applied_offers_list = []
        goods_name_list = [item.goods_name for item in final_list]
        for offer in available_offers:
            if offer.mock_good.goods_name in goods_name_list:
                applied_offers_list.append(offer.mock_good)
        subtotal = sum([item.price for item in orders_list])
        total = sum([item.price for item in final_list])
        print(f"""Subtotal: {round(Decimal(subtotal), 2)} British pounds""")
        if len(applied_offers_list) == 0:
            print("No special offer applied")
        else:
            for offer in applied_offers_list:
                actual_disctount = round(
                    Decimal(
                        offer.discount
                        * sum(
                            [
                                1 if offer.goods_name == item.goods_name else 0
                                for item in final_list
                            ]
                        )
                    ),
                    2,
                )
                print(f"{offer.offer_description} {actual_disctount} British pounds")
        print(f"Total: {round(Decimal(total))} British pounds")
