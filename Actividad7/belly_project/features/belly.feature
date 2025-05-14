# language: es

Característica: Comportamiento del Estómago

  Escenario: Comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

# Ejercicio 1: Nuevos escenarios Gherkin - Tiempos nuevos
  Escenario: Comer pepinos y esperar en minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar solo segundos
    Dado que he comido 5 pepinos
    Cuando espero "3600 segundos"
    Entonces mi estómago no debería gruñir
  
# Ejercicio 2: Nuevos escenarios Gherkin - Pepinos flotantes
  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 0.5 pepinos
    Cuando espero "2 horas"
    Entonces mi estómago no debería gruñir

# Ejercicio 2: Nuevos escenarios Gherkin - Pepinos Negativos
  Escenario: Error al comer cantidad negativa
    Dado que intento comer -2 pepinos
    Entonces se produce un error de cantidad negativa
