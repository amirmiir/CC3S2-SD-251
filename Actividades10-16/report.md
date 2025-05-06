# Reporte General

## P.1

### Paso 1-3:

Empezamos con la descarga de los archivos, la creación del entorno virtual y la instalación de las dependencias especificadas en `requirements.txt`:

``` bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ python -m venv venv
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ ls -lsa
total 56
4 drwxr-xr-x 10 amirmiir amirmiir 4096 may  5 18:57 .
4 drwxr-xr-x 20 amirmiir amirmiir 4096 may  5 18:52 ..
4 drwxr-xr-x  4 amirmiir amirmiir 4096 may  5 18:40 Actividad10
4 drwxr-xr-x  2 amirmiir amirmiir 4096 abr 23 08:19 Actividad11
4 drwxr-xr-x  2 amirmiir amirmiir 4096 may  5 09:57 Actividad12
4 drwxr-xr-x  2 amirmiir amirmiir 4096 may  5 09:57 Actividad13
4 drwxr-xr-x  2 amirmiir amirmiir 4096 may  5 09:57 Actividad14
4 drwxr-xr-x  2 amirmiir amirmiir 4096 may  5 09:57 Actividad15
4 drwxr-xr-x  2 amirmiir amirmiir 4096 may  5 09:57 Actividad16
4 -rw-r--r--  1 amirmiir amirmiir 3458 may  5 18:45 Instrucciones_Generales.md
8 -rw-r--r--  1 amirmiir amirmiir 4385 may  5 18:45 Makefile
4 -rw-r--r--  1 amirmiir amirmiir  433 may  5 18:45 requirements.txt
4 drwxr-xr-x  5 amirmiir amirmiir 4096 may  5 18:57 venv
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ source venv/bin/activate
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ make install
Instalando dependencias...
pip install -r requirements.txt
Collecting Werkzeug==2.1.2 (from -r requirements.txt (line 2))
  Downloading Werkzeug-2.1.2-py3-none-any.whl.metadata (4.4 kB)
Collecting SQLAlchemy==1.4.46 (from -r requirements.txt (line 3))
  Downloading SQLAlchemy-1.4.46.tar.gz (8.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.5/8.5 MB 8.4 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting Flask==2.1.2 (from -r requirements.txt (line 6))
  Downloading Flask-2.1.2-py3-none-any.whl.metadata (3.9 kB)
Collecting Flask-SQLAlchemy==2.5.1 (from -r requirements.txt (line 7))
  Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl.metadata (3.1 kB)
Collecting requests==2.31.0 (from -r requirements.txt (line 8))
  Downloading requests-2.31.0-py3-none-any.whl.metadata (4.6 kB)
Collecting pytest==7.1.2 (from -r requirements.txt (line 11))
  Downloading pytest-7.1.2-py3-none-any.whl.metadata (7.8 kB)
Collecting pytest-cov==3.0.0 (from -r requirements.txt (line 12))
  Downloading pytest_cov-3.0.0-py3-none-any.whl.metadata (24 kB)
Collecting coverage==6.3.2 (from -r requirements.txt (line 13))
  Downloading coverage-6.3.2.tar.gz (709 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 709.3/709.3 kB 6.4 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting factory-boy==3.2.1 (from -r requirements.txt (line 14))
  Downloading factory_boy-3.2.1-py2.py3-none-any.whl.metadata (14 kB)
Collecting pylint==2.14.0 (from -r requirements.txt (line 15))
  Downloading pylint-2.14.0-py3-none-any.whl.metadata (9.6 kB)
Collecting flake8==6.0.0 (from -r requirements.txt (line 18))
  Downloading flake8-6.0.0-py2.py3-none-any.whl.metadata (3.8 kB)
Collecting greenlet!=0.4.17 (from SQLAlchemy==1.4.46->-r requirements.txt (line 3))
  Downloading greenlet-3.2.1-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
Collecting Jinja2>=3.0 (from Flask==2.1.2->-r requirements.txt (line 6))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting itsdangerous>=2.0 (from Flask==2.1.2->-r requirements.txt (line 6))
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.0 (from Flask==2.1.2->-r requirements.txt (line 6))
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting charset-normalizer<4,>=2 (from requests==2.31.0->-r requirements.txt (line 8))
  Downloading charset_normalizer-3.4.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (35 kB)
Collecting idna<4,>=2.5 (from requests==2.31.0->-r requirements.txt (line 8))
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests==2.31.0->-r requirements.txt (line 8))
  Downloading urllib3-2.4.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests==2.31.0->-r requirements.txt (line 8))
  Downloading certifi-2025.4.26-py3-none-any.whl.metadata (2.5 kB)
Collecting attrs>=19.2.0 (from pytest==7.1.2->-r requirements.txt (line 11))
  Downloading attrs-25.3.0-py3-none-any.whl.metadata (10 kB)
Collecting iniconfig (from pytest==7.1.2->-r requirements.txt (line 11))
  Using cached iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting packaging (from pytest==7.1.2->-r requirements.txt (line 11))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2.0,>=0.12 (from pytest==7.1.2->-r requirements.txt (line 11))
  Using cached pluggy-1.5.0-py3-none-any.whl.metadata (4.8 kB)
Collecting py>=1.8.2 (from pytest==7.1.2->-r requirements.txt (line 11))
  Downloading py-1.11.0-py2.py3-none-any.whl.metadata (2.8 kB)
Collecting tomli>=1.0.0 (from pytest==7.1.2->-r requirements.txt (line 11))
  Downloading tomli-2.2.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
Collecting Faker>=0.7.0 (from factory-boy==3.2.1->-r requirements.txt (line 14))
  Downloading faker-37.1.0-py3-none-any.whl.metadata (15 kB)
Collecting dill>=0.2 (from pylint==2.14.0->-r requirements.txt (line 15))
  Downloading dill-0.4.0-py3-none-any.whl.metadata (10 kB)
Collecting platformdirs>=2.2.0 (from pylint==2.14.0->-r requirements.txt (line 15))
  Downloading platformdirs-4.3.7-py3-none-any.whl.metadata (11 kB)
Collecting astroid<=2.12.0-dev0,>=2.11.5 (from pylint==2.14.0->-r requirements.txt (line 15))
  Downloading astroid-2.11.7-py3-none-any.whl.metadata (4.7 kB)
Collecting isort<6,>=4.2.5 (from pylint==2.14.0->-r requirements.txt (line 15))
  Downloading isort-5.13.2-py3-none-any.whl.metadata (12 kB)
Collecting mccabe<0.8,>=0.6 (from pylint==2.14.0->-r requirements.txt (line 15))
  Downloading mccabe-0.7.0-py2.py3-none-any.whl.metadata (5.0 kB)
Collecting tomlkit>=0.10.1 (from pylint==2.14.0->-r requirements.txt (line 15))
  Downloading tomlkit-0.13.2-py3-none-any.whl.metadata (2.7 kB)
Collecting pycodestyle<2.11.0,>=2.10.0 (from flake8==6.0.0->-r requirements.txt (line 18))
  Downloading pycodestyle-2.10.0-py2.py3-none-any.whl.metadata (31 kB)
Collecting pyflakes<3.1.0,>=3.0.0 (from flake8==6.0.0->-r requirements.txt (line 18))
  Downloading pyflakes-3.0.1-py2.py3-none-any.whl.metadata (3.8 kB)
Collecting lazy-object-proxy>=1.4.0 (from astroid<=2.12.0-dev0,>=2.11.5->pylint==2.14.0->-r requirements.txt (line 15))
  Downloading lazy_object_proxy-1.11.0-py3-none-any.whl.metadata (8.2 kB)
Collecting wrapt<2,>=1.11 (from astroid<=2.12.0-dev0,>=2.11.5->pylint==2.14.0->-r requirements.txt (line 15))
  Downloading wrapt-1.17.2-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.4 kB)
Collecting setuptools>=20.0 (from astroid<=2.12.0-dev0,>=2.11.5->pylint==2.14.0->-r requirements.txt (line 15))
  Using cached setuptools-80.3.1-py3-none-any.whl.metadata (6.5 kB)
Collecting tzdata (from Faker>=0.7.0->factory-boy==3.2.1->-r requirements.txt (line 14))
  Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.0->Flask==2.1.2->-r requirements.txt (line 6))
  Downloading MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Downloading Werkzeug-2.1.2-py3-none-any.whl (224 kB)
Downloading Flask-2.1.2-py3-none-any.whl (95 kB)
Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl (17 kB)
Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Downloading pytest-7.1.2-py3-none-any.whl (297 kB)
Downloading pytest_cov-3.0.0-py3-none-any.whl (20 kB)
Downloading factory_boy-3.2.1-py2.py3-none-any.whl (35 kB)
Downloading pylint-2.14.0-py3-none-any.whl (485 kB)
Downloading flake8-6.0.0-py2.py3-none-any.whl (57 kB)
Downloading astroid-2.11.7-py3-none-any.whl (251 kB)
Downloading attrs-25.3.0-py3-none-any.whl (63 kB)
Downloading certifi-2025.4.26-py3-none-any.whl (159 kB)
Downloading charset_normalizer-3.4.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (148 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Downloading dill-0.4.0-py3-none-any.whl (119 kB)
Downloading faker-37.1.0-py3-none-any.whl (1.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.9/1.9 MB 7.5 MB/s eta 0:00:00
Downloading greenlet-3.2.1-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (606 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 606.8/606.8 kB 7.3 MB/s eta 0:00:00
Using cached idna-3.10-py3-none-any.whl (70 kB)
Downloading isort-5.13.2-py3-none-any.whl (92 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Downloading platformdirs-4.3.7-py3-none-any.whl (18 kB)
Using cached pluggy-1.5.0-py3-none-any.whl (20 kB)
Downloading py-1.11.0-py2.py3-none-any.whl (98 kB)
Downloading pycodestyle-2.10.0-py2.py3-none-any.whl (41 kB)
Downloading pyflakes-3.0.1-py2.py3-none-any.whl (62 kB)
Downloading tomli-2.2.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (241 kB)
Downloading tomlkit-0.13.2-py3-none-any.whl (37 kB)
Downloading urllib3-2.4.0-py3-none-any.whl (128 kB)
Using cached iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Downloading lazy_object_proxy-1.11.0-py3-none-any.whl (16 kB)
Downloading MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Using cached setuptools-80.3.1-py3-none-any.whl (1.2 MB)
Downloading wrapt-1.17.2-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (89 kB)
Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Building wheels for collected packages: SQLAlchemy, coverage
  Building wheel for SQLAlchemy (pyproject.toml) ... done
  Created wheel for SQLAlchemy: filename=sqlalchemy-1.4.46-cp313-cp313-linux_x86_64.whl size=1564025 sha256=5a70fc223d84c162f097fe0209ac78d97df77a7f20b59aa38915adf228833c21
  Stored in directory: /home/amirmiir/.cache/pip/wheels/ee/0b/6b/3d4d8f65ace7e18eca88300fb57cd0e4bbbaeafc6d4d3ec4b4
  Building wheel for coverage (pyproject.toml) ... done
  Created wheel for coverage: filename=coverage-6.3.2-py3-none-any.whl size=175694 sha256=6c591a112cbbaebd05a1c7a7f45c74346b48ab3fae7c8640e17ff7d0be0dd1cd
  Stored in directory: /home/amirmiir/.cache/pip/wheels/17/d0/4e/b860bdbeb2067fe1a80572fc4d695550db5f9bac1d8e99c326
Successfully built SQLAlchemy coverage
Installing collected packages: wrapt, Werkzeug, urllib3, tzdata, tomlkit, tomli, setuptools, pyflakes, pycodestyle, py, pluggy, platformdirs, packaging, mccabe, MarkupSafe, lazy-object-proxy, itsdangerous, isort, iniconfig, idna, greenlet, dill, coverage, click, charset-normalizer, certifi, attrs, SQLAlchemy, requests, pytest, Jinja2, flake8, Faker, astroid, pytest-cov, pylint, Flask, factory-boy, Flask-SQLAlchemy
Successfully installed Faker-37.1.0 Flask-2.1.2 Flask-SQLAlchemy-2.5.1 Jinja2-3.1.6 MarkupSafe-3.0.2 SQLAlchemy-1.4.46 Werkzeug-2.1.2 astroid-2.11.7 attrs-25.3.0 certifi-2025.4.26 charset-normalizer-3.4.2 click-8.1.8 coverage-6.3.2 dill-0.4.0 factory-boy-3.2.1 flake8-6.0.0 greenlet-3.2.1 idna-3.10 iniconfig-2.1.0 isort-5.13.2 itsdangerous-2.2.0 lazy-object-proxy-1.11.0 mccabe-0.7.0 packaging-25.0 platformdirs-4.3.7 pluggy-1.5.0 py-1.11.0 pycodestyle-2.10.0 pyflakes-3.0.1 pylint-2.14.0 pytest-7.1.2 pytest-cov-3.0.0 requests-2.31.0 setuptools-80.3.1 tomli-2.2.1 tomlkit-0.13.2 tzdata-2025.2 urllib3-2.4.0 wrapt-1.17.2

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ 

```

### Paso 4:

Revisamos la funcionalidad de make:
```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ make help
Uso: make [comando] [opciones]

Comandos disponibles:
  install              Instala las dependencias en el entorno actual
  lint                 Ejecuta análisis de código (flake8, black, etc.)
  test                 Ejecuta pytest en la actividad indicada (ACTIVITY)
  test_all             Ejecuta pytest en todas las actividades
  coverage             Ejecuta pytest con reporte de cobertura unificada
  coverage_individual  Ejecuta la cobertura para cada actividad por separado
  clean                Elimina archivos temporales, caches, etc.

Opciones:
  ACTIVITY=<nombre>    Actividad específica (por defecto: aserciones_pruebas)

Ejemplos:
  make install
  make lint
  make test
  make test ACTIVITY=pruebas_pytest
  make coverage
  make coverage_individual

Actividades disponibles:
  aserciones_pruebas coverage_pruebas factories_fakes objects_mocking practica_tdd pruebas_fixtures pruebas_pytest
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ 

```



### Paso 5: 

Realizamos la ejecución del código

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ make lint
Ejecutando flake8...
flake8 .

#...

./venv/lib/python3.13/site-packages/wrapt/wrappers.py:639:1: E302 expected 2 blank lines, found 1
./venv/lib/python3.13/site-packages/wrapt/wrappers.py:667:80: E501 line too long (84 > 79 characters)
./venv/lib/python3.13/site-packages/wrapt/wrappers.py:668:80: E501 line too long (81 > 79 characters)
./venv/lib/python3.13/site-packages/wrapt/wrappers.py:671:21: E128 continuation line under-indented for visual indent
./venv/lib/python3.13/site-packages/wrapt/wrappers.py:686:80: E501 line too long (80 > 79 characters)
./venv/lib/python3.13/site-packages/wrapt/wrappers.py:690:21: E128 continuation line under-indented for visual indent
./venv/lib/python3.13/site-packages/wrapt/wrappers.py:709:21: E128 continuation line under-indented for visual indent
./venv/lib/python3.13/site-packages/wrapt/wrappers.py:711:1: E302 expected 2 blank lines, found 1
./venv/lib/python3.13/site-packages/wrapt/wrappers.py:821:17: E128 continuation line under-indented for visual indent
make: *** [Makefile:58: lint] Error 1
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ 


```



### Paso 6:

Para el siguiente paso, es importante tener la misma estructura del proyecto sugerido, pues nuestro script analiza para una estructura existente, y resultará en un error si no se coincide.

Contenido general:

````bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ ls -lsa
total 36
4 drwxr-xr-x  4 amirmiir amirmiir 4096 may  6 00:10 .
4 drwxr-xr-x 20 amirmiir amirmiir 4096 may  5 18:52 ..
4 drwxr-xr-x  9 amirmiir amirmiir 4096 may  6 00:10 Actividades
4 -rw-r--r--  1 amirmiir amirmiir 3458 may  5 18:45 Instrucciones_Generales.md
8 -rw-r--r--  1 amirmiir amirmiir 4385 may  5 18:45 Makefile
4 -rw-r--r--  1 amirmiir amirmiir   18 may  5 18:59 report.md
4 -rw-r--r--  1 amirmiir amirmiir  433 may  5 18:45 requirements.txt
4 drwxr-xr-x  5 amirmiir amirmiir 4096 may  5 18:57 venv
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ 

````

Contenido dentro de actividades:
```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades(main)$ ls -lsa
total 36
4 drwxr-xr-x 9 amirmiir amirmiir 4096 may  6 00:10 .
4 drwxr-xr-x 4 amirmiir amirmiir 4096 may  6 00:10 ..
4 drwxr-xr-x 3 amirmiir amirmiir 4096 may  6 00:10 aserciones_pruebas
4 drwxr-xr-x 2 amirmiir amirmiir 4096 may  5 09:57 coverage_pruebas
4 drwxr-xr-x 2 amirmiir amirmiir 4096 may  5 09:57 factories_fakes
4 drwxr-xr-x 2 amirmiir amirmiir 4096 may  5 09:57 objects_mocking
4 drwxr-xr-x 2 amirmiir amirmiir 4096 may  5 09:57 practica_tdd
4 drwxr-xr-x 2 amirmiir amirmiir 4096 may  5 09:57 pruebas_fixtures
4 drwxr-xr-x 4 amirmiir amirmiir 4096 may  5 18:40 pruebas_pytest
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades(main)$ 

```



Ahora realizamos la ejecución de nuestros scripts en nuestro directorio base:

#### make test:

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ make test
Ejecutando pruebas en la actividad: aserciones_pruebas
cd Actividades/aserciones_pruebas && PYTHONWARNINGS="ignore::DeprecationWarning" pytest .
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0
collected 0 items                                                                                                                                                              

============================================================================ no tests ran in 0.02s =============================================================================
make: *** [Makefile:69: test] Error 5
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ 

```

#### make test ACTIVITY=$otra_actividad

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ make test ACTIVITY=coverage_pruebas
Ejecutando pruebas en la actividad: coverage_pruebas
cd Actividades/coverage_pruebas && PYTHONWARNINGS="ignore::DeprecationWarning" pytest .
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/coverage_pruebas
plugins: cov-3.0.0, Faker-37.1.0
collected 0 items                                                                                                                                                              

============================================================================ no tests ran in 0.03s =============================================================================
make: *** [Makefile:69: test] Error 5
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ 

```

### Paso 7:

#### make test_all

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ make test_all
Ejecutando pruebas en TODAS las actividades...
==========================================
EJECUTANDO PRUEBAS EN aserciones_pruebas
==========================================
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0
collected 0 items                                                                                                                                                              

============================================================================ no tests ran in 0.03s =============================================================================
make: *** [Makefile:74: test_all] Error 1
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ 

```

### Paso 8:

#### make coverage_individual

Generación de reportes de cobertura individual para cada actividad:

Hemos de notar en la ejecución de este comando que se está ejecutando unicamente para `./Actividades/aserciones_pruebas`, lo cual lo comprobamos cuando nos dirigimos a otra carpeta y notamos que no se ha creado ningún archivo.

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ make coverage_individual
Ejecutando cobertura individual para cada actividad...
==========================================
Generando cobertura para aserciones_pruebas
==========================================
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0
collected 0 items                                                                                                                                                              

============================================================================ no tests ran in 0.10s =============================================================================
/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/coverage/control.py:793: CoverageWarning: No data was collected. (no-data-collected)
  self._warn("No data was collected.", slug="no-data-collected")
make: *** [Makefile:88: coverage_individual] Error 1
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ cd Actividades/
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades(main)$ ls
aserciones_pruebas  coverage_pruebas  factories_fakes  objects_mocking  practica_tdd  pruebas_fixtures  pruebas_pytest
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades(main)$ cd pruebas_
bash: cd: pruebas_: No such file or directory
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades(main)$ cd pruebas_pytest/
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/pruebas_pytest(main)$ ls
act10  Instrucciones.md  report.md  requirements.txt  setup.cfg  test_triangle.py  triangle.py
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/pruebas_pytest(main)$ act10
bash: act10: command not found
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/pruebas_pytest(main)$ cd act10
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/pruebas_pytest/act10(main)$ cd ..
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/pruebas_pytest(main)$ cd ..
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades(main)$ cd ..
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ ls -lsa
total 36
4 drwxr-xr-x  4 amirmiir amirmiir 4096 may  6 00:10 .
4 drwxr-xr-x 20 amirmiir amirmiir 4096 may  5 18:52 ..
4 drwxr-xr-x  9 amirmiir amirmiir 4096 may  6 00:10 Actividades
4 -rw-r--r--  1 amirmiir amirmiir 3458 may  5 18:45 Instrucciones_Generales.md
8 -rw-r--r--  1 amirmiir amirmiir 4385 may  5 18:45 Makefile
4 -rw-r--r--  1 amirmiir amirmiir   18 may  5 18:59 report.md
4 -rw-r--r--  1 amirmiir amirmiir  433 may  5 18:45 requirements.txt
4 drwxr-xr-x  5 amirmiir amirmiir 4096 may  5 18:57 venv
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ cd Actividades/
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades(main)$ cd aserciones_pruebas/
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ ls
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ ls -lsa
total 64
 4 drwxr-xr-x 3 amirmiir amirmiir  4096 may  6 00:19 .
 4 drwxr-xr-x 9 amirmiir amirmiir  4096 may  6 00:10 ..
52 -rw-r--r-- 1 amirmiir amirmiir 53248 may  6 00:19 .coverage
 4 drwxr-xr-x 3 amirmiir amirmiir  4096 may  6 00:10 .pytest_cache
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ cd .coverage
bash: cd: .coverage: Not a directory
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ nano .pytest_cache/
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ nano .coverage 
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ cd ..
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades(main)$ cd ..
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ 

```

Su funcionamiento es similar a cuando realizamos `make test`, pues debemos especificar a qué actividad en concreto nos referimos. Y crea dos archivos `.coverage`  y `.pytest_cache`



### Paso 9:

#### make clean

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ make clean
Eliminando archivos de caché y reportes...
find . -type d -name "__pycache__" -exec rm -rf {} +
rm -rf .pytest_cache
rm -rf htmlcov htmlcov_*
coverage erase
Limpieza completa.
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16(main)$ cd Actividades/aserciones_pruebas/
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ ls -lsa
total 64
 4 drwxr-xr-x 3 amirmiir amirmiir  4096 may  6 00:19 .
 4 drwxr-xr-x 9 amirmiir amirmiir  4096 may  6 00:10 ..
52 -rw-r--r-- 1 amirmiir amirmiir 53248 may  6 00:19 .coverage
 4 drwxr-xr-x 3 amirmiir amirmiir  4096 may  6 00:10 .pytest_cache
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ nano .coverage
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ nano .pytest_cache/
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```



## P.2

Espera de resultados...

1. **Pruebas exitosas**:  
   - Si todo está correcto, al ejecutar las pruebas (`make test` o `make test_all`) verás en la terminal mensajes de éxito, por ejemplo:
     ```
     =========== test session starts ===========
     collected 2 items
     
     test_stack.py . .
     =========== 2 passed in 0.03s ============
     ```

2. **Reporte de cobertura en terminal**:
   - Tras ejecutar la cobertura, el comando mostrará un resumen como:
     ```
     Name          Stmts   Miss  Cover   Missing
     -------------------------------------------
     stack.py         30      5    83%   20-25
     -------------------------------------------
     TOTAL            30      5    83%
     ```
   - Aquí se indican el total de líneas, las faltantes y el porcentaje de cobertura.

3. **Reporte HTML de cobertura**:
   - Se generarán directorios HTML (por ejemplo, `htmlcov_aserciones_pruebas`, `htmlcov_coverage_pruebas`, etc.) para cada actividad.
   - Abre el archivo `index.html` dentro del directorio correspondiente para visualizar el reporte de cobertura de forma gráfica.

4. **Problemas de estilo (Lint)**:
   - Si existen errores de estilo o sintaxis, `flake8` mostrará mensajes indicando el archivo, la línea y la naturaleza del error, como:
     ```
     ./Actividades/aserciones_pruebas/stack.py:10:1: E302 expected 2 blank lines, found 1
     ```
   - Deberás corregir estos detalles y volver a ejecutar `make lint` hasta que el análisis quede limpio.
