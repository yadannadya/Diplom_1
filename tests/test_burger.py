import pytest


class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        i = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert (i-1) == len(burger.ingredients)

    def test_move_ingredient(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_filling

    def test_get_price(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert burger.get_price() == (mock_bun.get_price.return_value * 2 + mock_sauce.get_price.return_value)

    def test_get_receipt(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert burger.get_receipt() == (f'(==== {mock_bun.get_name.return_value} ====)\n'
                                        f'= {mock_sauce.get_type.return_value.lower()} {mock_sauce.get_name.return_value} =\n'
                                        f'(==== {mock_bun.get_name.return_value} ====)\n'
                                        f'\n'
                                        f'Price: {burger.get_price()}')