import pytest
from utils import *


@pytest.fixture
def mock_offer_good() -> MockOfferGood:
    return MockOfferGood()


@pytest.fixture
def mock_special_offer() -> MockSpecialOffer:
    return MockSpecialOffer()


@pytest.fixture
def mock_available_assortment() -> MockAvailableAssortment:
    return MockAvailableAssortment()


@pytest.fixture
def mock_good_fx() -> MockGood:
    return MockGood()
