import pytest
from src.time_parser import parse_time_to_hours

@pytest.mark.parametrize("texto, esperado", [
    ("1 hora y 30 minutos",   1.5),
    ("90 minutos",            1.5),
    ("3600 segundos",         1.0),
    ("1 hora, 30 minutos y 45 segundos", pytest.approx(1 + 30/60 + 45/3600)),
    ("45 segundos",           pytest.approx(45/3600)),
    ("2 horas",               2.0),
])
def test_parse_time_to_hours(texto, esperado):
    assert parse_time_to_hours(texto) == esperado

def test_parse_time_invalid():
    with pytest.raises(ValueError):
        parse_time_to_hours("tiempo indefinido")