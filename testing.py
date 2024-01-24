# Здесь пишем код для тестирования функции
from code import calculate

def test(a,b,c):
    d = calculate(a,b,c)

    test_d = -(a * b * c)

    assert d==test_d


test(1,2,3)
test(2,4,6)
test(11,12,2)
