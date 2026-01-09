import pytest
from unittest.mock import Mock
import requests
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

from praktikum.burger import Burger
import data

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture(params= data.bun)
def mock_bun(request):
    mock_bun = Mock()
    mock_bun.get_name.return_value = request.param[0]
    mock_bun.get_price.return_value = request.param[1]
    #bun = Bun(mock_bun)
    return mock_bun


@pytest.fixture(params= data.sauce)
def mock_sauce(request):
    mock_sauce = Mock()
    mock_sauce.get_type.return_value = request.param[0]
    mock_sauce.get_name.return_value = request.param[1]
    mock_sauce.get_price.return_value = request.param[2]
    return mock_sauce

@pytest.fixture(params= data.filling)
def mock_filling(request):
    mock_filling = Mock()
    mock_filling.type = request.param[0]
    mock_filling.name = request.param[1]
    mock_filling.price = request.param[2]
    return mock_filling




