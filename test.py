import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 10, 10) == 20
    def test_division(self):
        assert self.calc.division(self, 20, 2) == 10
    def test_multiply(self):
        assert self.calc.multiply(self, 5, 6) == 30
    def test_subtraction(self):
        assert self.calc.subtraction(self, 12, 4) == 8
    def teardown(self):
        print("Выполнение метода Teardown")

