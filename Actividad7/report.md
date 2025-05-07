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





## Ejercicios

### Ejercicio 1: **Añadir soporte para minutos y segundos en tiempos de espera**



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
