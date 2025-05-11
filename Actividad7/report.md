# Actividad 7

## Instalación

### Paso 1 y 2: Clonar repositorio - Crear entorno virtual

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad7(main)$ tree
.
├── act9
...
├── belly_project
│   ├── features
│   │   ├── belly.feature
│   │   ├── environment.py
│   │   └── steps
│   │       └── steps.py
│   ├── README.md
│   ├── requirements.txt
│   └── src
│       └── belly.py
├── Instrucciones.md
└── report.md

116 directories, 870 files

```

### Paso 3: **Instala las dependencias necesarias**:

El contenido actual de `requirements.txt` es el siguiente, según se necesite, se van a ir instalando más dependencias:

```bash
(act9) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad7/belly_project(main)$ cat requirements.txt 
behave>=1.2.6
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-html>=3.2.0
flake8>=6.0.0

```

La instalación satisfactoria

```bash
(act9) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad7/belly_project(main)$ pip install -r requirements.txt 
Collecting behave>=1.2.6 (from -r requirements.txt (line 1))
  Using cached behave-1.2.6-py2.py3-none-any.whl.metadata (6.4 kB)
Collecting pytest>=7.0.0 (from -r requirements.txt (line 2))
  Using cached pytest-8.3.5-py3-none-any.whl.metadata (7.6 kB)
Collecting pytest-cov>=4.0.0 (from -r requirements.txt (line 3))
  Using cached pytest_cov-6.1.1-py3-none-any.whl.metadata (28 kB)
Collecting pytest-html>=3.2.0 (from -r requirements.txt (line 4))
  Downloading pytest_html-4.1.1-py3-none-any.whl.metadata (3.9 kB)
Collecting flake8>=6.0.0 (from -r requirements.txt (line 5))
  Downloading flake8-7.2.0-py2.py3-none-any.whl.metadata (3.8 kB)
Collecting parse>=1.8.2 (from behave>=1.2.6->-r requirements.txt (line 1))
  Using cached parse-1.20.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting parse-type>=0.4.2 (from behave>=1.2.6->-r requirements.txt (line 1))
  Using cached parse_type-0.6.4-py2.py3-none-any.whl.metadata (12 kB)
Collecting six>=1.11 (from behave>=1.2.6->-r requirements.txt (line 1))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting iniconfig (from pytest>=7.0.0->-r requirements.txt (line 2))
  Using cached iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting packaging (from pytest>=7.0.0->-r requirements.txt (line 2))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest>=7.0.0->-r requirements.txt (line 2))
  Using cached pluggy-1.5.0-py3-none-any.whl.metadata (4.8 kB)
Collecting coverage>=7.5 (from coverage[toml]>=7.5->pytest-cov>=4.0.0->-r requirements.txt (line 3))
  Using cached coverage-7.8.0-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (8.5 kB)
Collecting jinja2>=3.0.0 (from pytest-html>=3.2.0->-r requirements.txt (line 4))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting pytest-metadata>=2.0.0 (from pytest-html>=3.2.0->-r requirements.txt (line 4))
  Downloading pytest_metadata-3.1.1-py3-none-any.whl.metadata (8.6 kB)
Collecting mccabe<0.8.0,>=0.7.0 (from flake8>=6.0.0->-r requirements.txt (line 5))
  Using cached mccabe-0.7.0-py2.py3-none-any.whl.metadata (5.0 kB)
Collecting pycodestyle<2.14.0,>=2.13.0 (from flake8>=6.0.0->-r requirements.txt (line 5))
  Downloading pycodestyle-2.13.0-py2.py3-none-any.whl.metadata (4.5 kB)
Collecting pyflakes<3.4.0,>=3.3.0 (from flake8>=6.0.0->-r requirements.txt (line 5))
  Downloading pyflakes-3.3.2-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting MarkupSafe>=2.0 (from jinja2>=3.0.0->pytest-html>=3.2.0->-r requirements.txt (line 4))
  Using cached MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Using cached behave-1.2.6-py2.py3-none-any.whl (136 kB)
Using cached pytest-8.3.5-py3-none-any.whl (343 kB)
Using cached pytest_cov-6.1.1-py3-none-any.whl (23 kB)
Downloading pytest_html-4.1.1-py3-none-any.whl (23 kB)
Downloading flake8-7.2.0-py2.py3-none-any.whl (57 kB)
Using cached coverage-7.8.0-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (244 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Using cached parse-1.20.2-py2.py3-none-any.whl (20 kB)
Using cached parse_type-0.6.4-py2.py3-none-any.whl (27 kB)
Using cached pluggy-1.5.0-py3-none-any.whl (20 kB)
Downloading pycodestyle-2.13.0-py2.py3-none-any.whl (31 kB)
Downloading pyflakes-3.3.2-py2.py3-none-any.whl (63 kB)
Downloading pytest_metadata-3.1.1-py3-none-any.whl (11 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Installing collected packages: parse, six, pyflakes, pycodestyle, pluggy, packaging, mccabe, MarkupSafe, iniconfig, coverage, pytest, parse-type, jinja2, flake8, pytest-metadata, pytest-cov, behave, pytest-html
Successfully installed MarkupSafe-3.0.2 behave-1.2.6 coverage-7.8.0 flake8-7.2.0 iniconfig-2.1.0 jinja2-3.1.6 mccabe-0.7.0 packaging-25.0 parse-1.20.2 parse-type-0.6.4 pluggy-1.5.0 pycodestyle-2.13.0 pyflakes-3.3.2 pytest-8.3.5 pytest-cov-6.1.1 pytest-html-4.1.1 pytest-metadata-3.1.1 six-1.17.0

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
(act9) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad7/belly_project(main)$ 

```

----

## Ejecución de Pruebas

Ejecución de pruebas con behave:

```bash
(act9) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad7/belly_project(main)$ behave
Característica: Comportamiento del Estómago # features/belly.feature:3

  Escenario: Comer muchos pepinos y gruñir  # features/belly.feature:5
    Dado que he comido 42 pepinos           # features/steps/steps.py:19 0.000s
    Cuando espero 2 horas                   # features/steps/steps.py:23 0.001s
    Entonces mi estómago debería gruñir     # features/steps/steps.py:50 0.000s

  Escenario: Comer pocos pepinos y no gruñir  # features/belly.feature:10
    Dado que he comido 10 pepinos             # features/steps/steps.py:19 0.000s
    Cuando espero 2 horas                     # features/steps/steps.py:23 0.000s
    Entonces mi estómago no debería gruñir    # features/steps/steps.py:54 0.000s

  Escenario: Comer muchos pepinos y esperar menos de una hora  # features/belly.feature:15
    Dado que he comido 50 pepinos                              # features/steps/steps.py:19 0.000s
    Cuando espero media hora                                   # features/steps/steps.py:23 0.000s
    Entonces mi estómago no debería gruñir                     # features/steps/steps.py:54 0.000s

  Escenario: Comer pepinos y esperar en minutos  # features/belly.feature:20
    Dado que he comido 30 pepinos                # features/steps/steps.py:19 0.000s
    Cuando espero 90 minutos                     # features/steps/steps.py:23 0.000s
    Entonces mi estómago debería gruñir          # features/steps/steps.py:50 0.000s

  Escenario: Comer pepinos y esperar en diferentes formatos  # features/belly.feature:25
    Dado que he comido 25 pepinos                            # features/steps/steps.py:19 0.000s
    Cuando espero "dos horas y treinta minutos"              # features/steps/steps.py:23 0.000s
    Entonces mi estómago debería gruñir                      # features/steps/steps.py:50 0.000s

1 feature passed, 0 failed, 0 skipped
5 scenarios passed, 0 failed, 0 skipped
15 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.003s
(act9) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad7/belly_project(main)$ 

```

Realizamos los cambios sugeridos por el autor, y notamos que son el mismo código Gherkin:

```bash
(act9) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad7/belly_project(main)$ behave
Característica: Comportamiento del Estómago # features/belly.feature:3

  Escenario: Comer muchos pepinos y gruñir  # features/belly.feature:5
    Dado que he comido 42 pepinos           # features/steps/steps.py:19 0.000s
    Cuando espero 2 horas                   # features/steps/steps.py:23 0.001s
    Entonces mi estómago debería gruñir     # features/steps/steps.py:50 0.000s

  Escenario: Comer pocos pepinos y no gruñir  # features/belly.feature:10
    Dado que he comido 10 pepinos             # features/steps/steps.py:19 0.000s
    Cuando espero 2 horas                     # features/steps/steps.py:23 0.000s
    Entonces mi estómago no debería gruñir    # features/steps/steps.py:54 0.000s

  Escenario: Comer muchos pepinos y esperar menos de una hora  # features/belly.feature:15
    Dado que he comido 50 pepinos                              # features/steps/steps.py:19 0.000s
    Cuando espero media hora                                   # features/steps/steps.py:23 0.000s
    Entonces mi estómago no debería gruñir                     # features/steps/steps.py:54 0.000s

  Escenario: Comer pepinos y esperar en minutos  # features/belly.feature:20
    Dado que he comido 30 pepinos                # features/steps/steps.py:19 0.000s
    Cuando espero 90 minutos                     # features/steps/steps.py:23 0.000s
    Entonces mi estómago debería gruñir          # features/steps/steps.py:50 0.000s

  Escenario: Comer pepinos y esperar en diferentes formatos  # features/belly.feature:25
    Dado que he comido 25 pepinos                            # features/steps/steps.py:19 0.000s
    Cuando espero "dos horas y treinta minutos"              # features/steps/steps.py:23 0.000s
    Entonces mi estómago debería gruñir                      # features/steps/steps.py:50 0.000s

1 feature passed, 0 failed, 0 skipped
5 scenarios passed, 0 failed, 0 skipped
15 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.003s
(act9) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad7/belly_project(main)$ 

```

----

## Ejercicios

### Setup Inicial

"Cuando termines **todos los ejercicios** (del 1 al 15, o los que hayas incluido en tu proyecto) y ejecutes tanto las pruebas **unitarias** (Pytest) como las **pruebas BDD** (Behave) dentro de tu pipeline de CI/CD (o localmente), la **salida final** que verás será algo parecido a esto..."

Para ello, vamos a realizar el setup inicial de nuestro directorio `tests`, el cual se irá modificando con el avance de los ejercicios, así como nuestro archivo de instalación `requirements.txt`

```bash
(act9) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividad7/belly_project/tests(main)$ tree
.
├── __init__.py
└── test_belly.py

1 directory, 2 files
```

----

### Ejercicio 1: **Añadir soporte para minutos y segundos en tiempos de espera**

#### Paso 1:

Para este ejercicio, vamos a realizar un par de cambios significativos en cuanto a código. Los primeros cambios serán la modificación del archivo `steps.py` y la creación de`src/time_parser.py`.  La creación de este archivo corresponde a delegar la parte lógica dentro de `steps.py` y pasar el parsing completamente a este archivo para manejar la lógica de manera completa y separada. Esto lo realizamos con el propósito de mantener un BDD coherente, pues no es propio de un lenguaje natural.

##### `steps.py` :

```python
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
```



##### `time_parser.py`:

```python
# src/time_parser.py

import re

# Diccionario
NUMEROS = {
    "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
    "veintiuno": 21, "veintidos": 22, "veintitres": 23, "veinticuatro": 24,
    "veinticinco": 25, "veintiseis": 26, "veintisiete": 27, "veintiocho": 28,
    "veintinueve": 29, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
    "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "media": 0.5
}

# Proceso de conversión
def palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        return NUMEROS.get(palabra, 0)

def parse_time_to_hours(texto: str) -> float:
    """
    Acepta formatos como:
      - '1 hora y 30 minutos'
      - '90 minutos'
      - '3600 segundos'
      - '1 hora, 30 minutos y 45 segundos'
    Devuelve el tiempo total en horas (float).
    """
    # Normalizar separadores
    texto = texto.replace(",", " ").replace(" y ", " ")
    # Regex con tres grupos opcionales
    pattern = re.compile(
        r'(?:(\w+)\s*horas?)?\s*'
        r'(?:(\w+)\s*minutos?)?\s*'
        r'(?:(\w+)\s*segundos?)?'
    )
    match = pattern.fullmatch(texto.strip())
    if not match:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: '{texto}'")
    # Asignamos las palabras a cada variable
    horas_word, minutos_word, segundos_word = match.groups()
    # Hacemos uso de nuestro diccionario
    horas   = palabra_a_numero(horas_word or "0")
    minutos = palabra_a_numero(minutos_word or "0")
    segundos= palabra_a_numero(segundos_word or "0")
    return horas + minutos/60 + segundos/3600

```

#### Paso 2: Implementación escenario Gherkin

Para esto, nos guíamos de `src/belly.py`, para establecer un escenario de esperarse, y lo añadimos a `features/belly.feature`

##### belly.feature

```gherkin
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

# Ejercicio 1: Nuevos escenarios Gherkin
  Escenario: Comer pepinos y esperar en minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar solo segundos
    Dado que he comido 5 pepinos
    Cuando espero "3600 segundos"
    Entonces mi estómago no debería gruñir

```



#### Paso 3: Validación (testing)

Agregamos la validación de resultados para nuestra lógica implementada en el primer paso, a través de la librería `pytest` y con el siguiente código

##### `test/test_time_parser.py`

```python
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
```



#### Paso 4:

Para nuestro desarrollo de la integración en un entorno DevOps, primero debemos pensar en qué cosas deben suceder cuando hagamos push de nuestro repositorio. Esto implica, ¿qué acciones deben realizarse y cómo vamos a lograrlo? 
Primero, debemos ejecutar las pruebas unitarias con pytest para verificar si se cumple la lógica esperada. Segundo, debemos correr los BDD escenarios para validar el comportamiento. Finalmente, realizar el reporte del estado final en nuestra pipeline.

**Notemos** que el deploy en Github Actions requeriría realizar cambios en las direcciones debido a cómo se está manejando el repositorio

Iniciamos el archivo `.github/ci.yaml`, y especificamos que las acciones por definirse se van a activar cuando se hagan push y pull_request cuando trabajemos con las ramas main, develop

```yaml
name: CI

on:
	push:
		branches: [main, develop]
	pull_request:
		branches: [main, develop]
...
```

Diseñamos qué tests se van a ejecutar y como dentro de jobs, y empezamos con la primera acción `- uses: actions/checkout@v3` para acceder a nuestros archivos dentro del repositorio.

```yaml
...
jobs:
	test:
		runs-on: ubuntu-latest
		
		steps:
			- uses: actions/checkout@v3
```

Continuamos con la especificación de cómo se van a realizar las pruebas con la versión de python a utilizar y la instalación de las dependencias:

```yaml
...
jobs:
	test:
		runs-on: ubuntu-latest
		
		steps:
			- uses: actions/checkout@v3
			
			- name: Set up Python
			  uses: actions/setup-python@v5
			  with:
			  	python-version: '3.11'
			
			- name: Install dependencies
			  run: |
			  	python -m pip install --upgrade pip
			  	pip install -r requirements.txt
```

Y finalizamos especificando que se va a hacer las pruebas unitarias con `pytest` y el BDD con `behave`:

```yaml
...
jobs:
	test:
		runs-on: ubuntu-latest
		
		steps:
			- uses: actions/checkout@v3
			
			- name: Set up Python
			  uses: actions/setup-python@v5
			  with:
			  	python-version: '3.11'
			
			- name: Install dependencies
			  run: |
			  	python -m pip install --upgrade pip
			  	pip install -r requirements.txt
			  	
			- name: Run Pytest
			  run: pytest --maxfail=1 --disable-warnings -q
			
			- name: Run Behave BDD
			  run: behave --no-capture
```

Finalmente, añadimos el paso final del reporte, utilizando Codecov, y añadimos el token a nuestros secretos de GitHub, y accedemos a este a través de una variable.

```yaml
...
jobs:
	test:
		runs-on: ubuntu-latest
		
		steps:
			- uses: actions/checkout@v3
			
			- name: Set up Python
			  uses: actions/setup-python@v5
			  with:
			  	python-version: '3.11'
			
			- name: Install dependencies
			  run: |
			  	python -m pip install --upgrade pip
			  	pip install -r requirements.txt
			  	
			- name: Run Pytest
			  run: pytest --maxfail=1 --disable-warnings -q
			
			- name: Run Behave BDD
			  run: behave --no-capture
			  
			- name: Upload coverage report
			  uses: owner/repo-activity7@v3
			  with:
			  	token: ${{ secrets.CODECOV_TOKEN}}
```



----

### Ejercicio 2: **Manejo de cantidades fraccionarias de pepinos**



### Ejercicio 3: **Soporte para idiomas múltiples (Español e Inglés)**



### Ejercicio 4: **Manejo de tiempos aleatorios**



### Ejercicio 5: **Validación de cantidades no válidas**



### Ejercicio 6: **Escalabilidad con grandes cantidades de pepinos**



### Ejercicio 7: **Descripciones de tiempo complejas**



### Ejercicio 8: **De TDD a BDD – Convertir requisitos técnicos a pruebas en Gherkin**



### Ejercicio 9: **Identificación de criterios de aceptación para historias de usuario**



### Ejercicio 10: **Escribir pruebas unitarias antes de escenarios BDD**



### Ejercicio 11: **Refactorización guiada por TDD y BDD**



### Ejercicio 12: **Ciclo completo de TDD a BDD – Añadir nueva funcionalidad**



### Ejercicio 13: **Añadir criterios de aceptación claros**



### Ejercicio 14: **Integración con Mocking, Stubs y Fakes (para DevOps)**



### Ejercicio 15: **Despliegue y validación continua en un entorno de integración (CI/CD)**
