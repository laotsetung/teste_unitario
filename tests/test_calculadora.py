import pytest

from calculadora import somar, subtrair, multiplicar, dividir, potencia   

#Testando a função somar
def test_soma():
    assert somar(1,1) == 2
    assert somar(9,33) == 42
    assert somar(5,-10) == -5
    with pytest.raises(ValueError, match="A entrada precisa ser um número"):
        somar(1, "a")

#Testando a função subtrair
def test_subtracao():
    assert subtrair(5,3) == 2
    assert subtrair(42,9) == 33
    assert subtrair(-5,-10) == 5

#Testar varias multiplicações 
@pytest.mark.parametrize("a, b, resultado", [
    (2, 10, 20.0),
    (3, 3, 9.0),
    (5.1, 2, 10.2),
])
def test_multiplicar(a, b, resultado):
    assert multiplicar(a, b) == resultado

# Testar varias divisões
@pytest.mark.parametrize("a, b, resultado", [
    (10, 2, 5.0),
    (30, 3, 10.0),
    (-10, 5, -2.0),
    (13, 1, 13.0),
])
def test_divisao(a, b, resultado):
    assert dividir(a, b) == resultado

# teste de divisão por ZERO, que espera um erro
def test_divisao_erro():
    with pytest.raises(ValueError, match="Não é possível dividir por zero"):
        dividir(13,0)

# Teste da função de potência que está errada
def test_potencia_com_bug():
    # 2 elevado a terceira potencia = 8, mas o codigo esta errado então deve falhar
    assert potencia(2,3) == 8
