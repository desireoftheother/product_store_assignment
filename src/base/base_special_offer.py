from abc import ABC, abstractmethod
from typing import List
from src.base.base_goods import BaseGood, BaseOfferGood


class BaseSpecialOffer(ABC):
    """Base class for applying different special offers"""

    @property
    @abstractmethod
    def goods_2_quantity_mapping(self) -> dict:
        """Mapping between specific goods and count which is needed to be present in order
        for special offer applying"""

    @property
    @abstractmethod
    def mock_good(self) -> BaseOfferGood:
        """Goods object which will substitute that goods that are used in offer"""

    def apply_an_offer(self, original_goods_list: List[BaseGood]) -> List[BaseGood]:
        """Method for applying the specific special offer to the list of ordered goods"""
        is_order_applied = False
        offer_occurences_times_list = []
        for good_obj, count in self.goods_2_quantity_mapping.items():
            obj_cnt = sum(
                [
                    1 if good.goods_name == good_obj.goods_name else 0
                    for good in original_goods_list
                ]
            )
            if (obj_cnt % count == 0) & (obj_cnt != 0):
                is_order_applied = True
                offer_occurences_times_list.append(obj_cnt / count)
            else:
                is_order_applied = False
        if not is_order_applied:
            final_goods_list = original_goods_list.copy()
        else:
            modified_goods_list = original_goods_list.copy()
            offer_applied_times = int(min(offer_occurences_times_list))
            removed_offered_goods = modified_goods_list.copy()
            for good_obj, count in self.goods_2_quantity_mapping.items():
                removed_offered_goods.sort(
                    key=lambda item: item.goods_name == good_obj.goods_name
                )
                times_slicing = int(offer_applied_times * count)
                for i in range(0, times_slicing):
                    removed_offered_goods.pop()
            removed_offered_goods = removed_offered_goods + (
                [self.mock_good] * offer_applied_times
            )
            final_goods_list = removed_offered_goods
        return final_goods_list
