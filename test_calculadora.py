# test_calculadora.py

from calculadora import soma, subtrai, multiplica, divide

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_subtrai():
    assert subtrai(5, 2) == 3
    assert subtrai(10, 5) == 5
    assert subtrai(0, 0) == 0

def test_multiplica():
    assert multiplica(2, 3) == 6
    assert multiplica(5, 0) == 0
    assert multiplica(-1, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 5) == 2
    assert divide(5, 0) == "Erro: Divisão por zero!"
