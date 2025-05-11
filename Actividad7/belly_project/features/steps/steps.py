from behave import given, when, then
# Importamos la función parse_time_to_hours(), lógica del programa
from src.time_parser import parse_time_to_hours
import re


@given('que he comido {cukes:d} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.belly.comer(cukes)

# Ejercicio 1 - Eliminación de lógica
@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    # Limpieza de puntuación innecesaria y conversión a minúsculas
    time_description = time_description.strip('"').lower()
    # Delegación de lógica a src/time_paser.py en la función parse_time_to_hours()
    total_time_in_hours = parse_time_to_hours(time_description)
    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."