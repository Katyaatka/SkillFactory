import pytest

from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self,1, 1) == 3
