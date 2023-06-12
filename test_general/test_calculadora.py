import pytest

from negocio.calculadora_neg import Calculadora

class TestLaboratorio:
    calculadora = Calculadora()

    @pytest.mark.wilo
    def test_sumar(self):
        print("[Funcion sumar]")
        assert self.calculadora.suma(3, 2) == 5
        assert self.calculadora.suma(8, 2) == 10

    @pytest.mark.wilo
    def test_restar(self):
        print("[Funcion restar]")
        assert self.calculadora.resta(5, 3) == 5
        assert self.calculadora.resta(14, 4) == 10

    @pytest.mark.regression
    def test_multiplicar(self):
        print("[Funcion multiplicar]")
        assert self.calculadora.multiplicar(5, 3) == 15
        assert self.calculadora.multiplicar(10, 2) == 20