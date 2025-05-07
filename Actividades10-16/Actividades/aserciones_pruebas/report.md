# Reporte Actividad 11

### Paso 1: Instalación de pytest y pytest-cov

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ python3 -m pip install pytest pytest-cov
Requirement already satisfied: pytest in /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages (7.1.2)
Requirement already satisfied: pytest-cov in /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages (3.0.0)
Requirement already satisfied: attrs>=19.2.0 in /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages (from pytest) (25.3.0)
Requirement already satisfied: iniconfig in /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages (from pytest) (2.1.0)
Requirement already satisfied: packaging in /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages (from pytest) (25.0)
Requirement already satisfied: pluggy<2.0,>=0.12 in /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages (from pytest) (1.5.0)
Requirement already satisfied: py>=1.8.2 in /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages (from pytest) (1.11.0)
Requirement already satisfied: tomli>=1.0.0 in /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages (from pytest) (2.2.1)
Requirement already satisfied: coverage>=5.2.1 in /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages (from coverage[toml]>=5.2.1->pytest-cov) (6.3.2)

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```



### Paso 2: Archivos de prueba

Vemos lo que contiene `stack.py`

```python
class Stack:
    def push(self, data: Any) -> None:
        ...
    def pop(self) -> Any:
        ...
    def peek(self) -> Any:
        ...
    def is_empty(self) -> bool:
        ...
```

Y ejecutamos `pytest -v`

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0 -- /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0
collected 4 items                                                                                                                                                              

test_stack.py::TestStack::test_is_empty PASSED                                                                                                                           [ 25%]
test_stack.py::TestStack::test_peek PASSED                                                                                                                               [ 50%]
test_stack.py::TestStack::test_pop PASSED                                                                                                                                [ 75%]
test_stack.py::TestStack::test_push PASSED                                                                                                                               [100%]

=============================================================================== warnings summary ===============================================================================
test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================== 4 passed, 4 warnings in 0.09s =========================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```

Tras ejecutar `pytest -x`, o `pytest --exitfirst`, vemos que se detiene en el error que nos resulta tras ejecutar `pytest -v`:

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest -x
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0
collected 4 items                                                                                                                                                              

test_stack.py ....                                                                                                                                                       [100%]

=============================================================================== warnings summary ===============================================================================
test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================== 4 passed, 4 warnings in 0.08s =========================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```

Debemos notar que `--random-order` forma parte de una dependencia de python `pytest-random-order`, la cual no fue instalada inicialmente, y para ello debemos instalarlo, lo añadimos a  `requirements.txt` y ejecutamos `make install` o`pip install -r requirements.txt`

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest --random-order
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0
Using --random-order-bucket=module
Using --random-order-seed=770877

rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0, random-order-1.1.1
collected 4 items                                                                                                                                                              

test_stack.py ....                                                                                                                                                       [100%]

=============================================================================== warnings summary ===============================================================================
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================== 4 passed, 4 warnings in 0.08s =========================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest --random-order -exitfirst
/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/config/__init__.py:324: PluggyTeardownRaisedWarning: A plugin raised an exception during an old-style hookwrapper teardown.
Plugin: helpconfig, Hook: pytest_cmdline_parse
UsageError: usage: pytest [options] [file_or_dir] [file_or_dir] [...]
pytest: error: unrecognized arguments: -exitfirst
  inifile: None
  rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
For more information see https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.PluggyTeardownRaisedWarning
  config = pluginmanager.hook.pytest_cmdline_parse(
ERROR: usage: pytest [options] [file_or_dir] [file_or_dir] [...]
pytest: error: unrecognized arguments: -exitfirst
  inifile: None
  rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas

(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```

### Paso 3: Escribiendo aserciones para el método `is_empty()`

Realizamos las modificaciones a `test_stack.py` sugeridas por las instrucciones (notamos que estamos modificando `is_empty`, la cual antes no funcionaba en el test)

### Paso 4:

Tuvimos que modificar el código propuesto añadiendo el parámetro `self` a  `test_is_empty()`:

```python
from unittest import TestCase
from stack import Stack


class TestStack(TestCase):
    """Casos de prueba para la Pila"""

    def setUp(self) -> None:
        """Configuración antes de cada prueba."""
        self.stack = Stack()

    def tearDown(self) -> None:
        """Limpieza después de cada prueba."""
        self.stack = None

    def test_push(self) -> None:
        """Prueba de insertar un elemento en la pila."""
        stack = Stack()
        stack.push(1)
        self.assertEqual(
            stack.peek(), 1,
            "El valor recién agregado debe estar en la parte superior"
        )
        stack.push(2)
        self.assertEqual(
            stack.peek(), 2,
            "Después de otro push, el valor superior debe ser el último agregado"
        )

    def test_pop(self) -> None:
    	self.stack.push(3)
    	self.stack.push(5)
    	self.assertEqual(self.stack.pop(), 5)
    	self.assertEqual(self.stack.peek(), 3)
    	self.stack.pop()
    	self.assertTrue(self.stack.is_empty())

    def test_peek(self) -> None:
        """Prueba de observar el elemento superior de la pila."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(
            stack.peek(), 2,
            "El valor superior debe ser el último agregado (2)"
        )
        self.assertEqual(
            stack.peek(), 2,
            "La pila no debe cambiar después de peek()"
        )
	
    def test_is_empty(self):
	    stack = Stack()
	    assert stack.is_empty() == True  # La pila recién creada debe estar vacía
	    stack.push(5)
	    assert stack.is_empty() == False  # Después de agregar un elemento, la pila no debe estar vacía

```

Y se obtuvo el siguiente resultado ejecutando todas las pruebas.

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0 -- /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/bin/python
cachedir: .pytest_cache
Test order randomisation NOT enabled. Enable with --random-order or --random-order-bucket=<bucket_type>
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0, random-order-1.1.1
collected 4 items                                                                                                                                                              

test_stack.py::TestStack::test_is_empty PASSED                                                                                                                           [ 25%]
test_stack.py::TestStack::test_peek PASSED                                                                                                                               [ 50%]
test_stack.py::TestStack::test_pop PASSED                                                                                                                                [ 75%]
test_stack.py::TestStack::test_push PASSED                                                                                                                               [100%]

=============================================================================== warnings summary ===============================================================================
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    inlocs = ast.Compare(ast.Str(name.id), [ast.In()], [locs])

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expr = ast.IfExp(test, self.display(name), ast.Str(name.id))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    syms.append(ast.Str(sym))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expls.append(ast.Str(expl))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: 10 warnings
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    keys = [ast.Str(key) for key in current.keys()]

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    assertmsg = ast.Str("")

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    template = ast.BinOp(assertmsg, ast.Add(), ast.Str(explanation))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950: DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead
    clear = ast.Assign(variables, ast.NameConstant(None))

test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================== 4 passed, 30 warnings in 0.10s ========================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```

### Paso 5: **Escribiendo aserciones para el método `peek()`**

Tras realizar la modificación a `test_peek()`, y pasar `self` como parámetro funciona, sin embargo, al copiar y pegar el código obtenemos el siguiente resultado:

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0 -- /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/bin/python
cachedir: .pytest_cache
Test order randomisation NOT enabled. Enable with --random-order or --random-order-bucket=<bucket_type>
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0, random-order-1.1.1
collected 4 items                                                                                                                                                              

test_stack.py::TestStack::test_is_empty PASSED                                                                                                                           [ 25%]
test_stack.py::TestStack::test_peek FAILED                                                                                                                               [ 50%]
test_stack.py::TestStack::test_pop PASSED                                                                                                                                [ 75%]
test_stack.py::TestStack::test_push PASSED                                                                                                                               [100%]

=================================================================================== FAILURES ===================================================================================
_____________________________________________________________________________ TestStack.test_peek ______________________________________________________________________________

self = <unittest.case._Outcome object at 0x703239d17250>, test_case = <test_stack.TestStack testMethod=test_peek>, subTest = False

    @contextlib.contextmanager
    def testPartExecutor(self, test_case, subTest=False):
        old_success = self.success
        self.success = True
        try:
>           yield

/usr/lib/python3.13/unittest/case.py:58: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/lib/python3.13/unittest/case.py:651: in run
    self._callTestMethod(testMethod)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_stack.TestStack testMethod=test_peek>, method = <bound method TestStack.test_peek of <test_stack.TestStack testMethod=test_peek>>

    def _callTestMethod(self, method):
>       if method() is not None:
E       TypeError: TestStack.test_peek() takes 0 positional arguments but 1 was given

/usr/lib/python3.13/unittest/case.py:606: TypeError
=============================================================================== warnings summary ===============================================================================
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    inlocs = ast.Compare(ast.Str(name.id), [ast.In()], [locs])

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expr = ast.IfExp(test, self.display(name), ast.Str(name.id))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    syms.append(ast.Str(sym))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expls.append(ast.Str(expl))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: 20 warnings
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    keys = [ast.Str(key) for key in current.keys()]

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    assertmsg = ast.Str("")

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    template = ast.BinOp(assertmsg, ast.Add(), ast.Str(explanation))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950: DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead
    clear = ast.Assign(variables, ast.NameConstant(None))

test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================================================================== short test summary info ============================================================================
FAILED test_stack.py::TestStack::test_peek - TypeError: TestStack.test_peek() takes 0 positional arguments but 1 was given
=================================================================== 1 failed, 3 passed, 54 warnings in 0.17s ===================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```

Probamos con el segundo código:

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0 -- /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/bin/python
cachedir: .pytest_cache
Test order randomisation NOT enabled. Enable with --random-order or --random-order-bucket=<bucket_type>
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0, random-order-1.1.1
collected 4 items                                                                                                                                                              

test_stack.py::TestStack::test_is_empty PASSED                                                                                                                           [ 25%]
test_stack.py::TestStack::test_peek PASSED                                                                                                                               [ 50%]
test_stack.py::TestStack::test_pop PASSED                                                                                                                                [ 75%]
test_stack.py::TestStack::test_push PASSED                                                                                                                               [100%]

=============================================================================== warnings summary ===============================================================================
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    inlocs = ast.Compare(ast.Str(name.id), [ast.In()], [locs])

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expr = ast.IfExp(test, self.display(name), ast.Str(name.id))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    syms.append(ast.Str(sym))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expls.append(ast.Str(expl))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: 10 warnings
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    keys = [ast.Str(key) for key in current.keys()]

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    assertmsg = ast.Str("")

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    template = ast.BinOp(assertmsg, ast.Add(), ast.Str(explanation))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950: DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead
    clear = ast.Assign(variables, ast.NameConstant(None))

test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================== 4 passed, 30 warnings in 0.09s ========================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```

### Paso 6: **Escribiendo aserciones para el `método pop()`**

Realizamos las modificaciones, y como se espera, el primer cambio lleva a un error, pues no contiene el parámetro `self`:

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0 -- /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/bin/python
cachedir: .pytest_cache
Test order randomisation NOT enabled. Enable with --random-order or --random-order-bucket=<bucket_type>
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0, random-order-1.1.1
collected 4 items                                                                                                                                                              

test_stack.py::TestStack::test_is_empty PASSED                                                                                                                           [ 25%]
test_stack.py::TestStack::test_peek PASSED                                                                                                                               [ 50%]
test_stack.py::TestStack::test_pop FAILED                                                                                                                                [ 75%]
test_stack.py::TestStack::test_push PASSED                                                                                                                               [100%]

=================================================================================== FAILURES ===================================================================================
______________________________________________________________________________ TestStack.test_pop ______________________________________________________________________________

self = <unittest.case._Outcome object at 0x716636917250>, test_case = <test_stack.TestStack testMethod=test_pop>, subTest = False

    @contextlib.contextmanager
    def testPartExecutor(self, test_case, subTest=False):
        old_success = self.success
        self.success = True
        try:
>           yield

/usr/lib/python3.13/unittest/case.py:58: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/lib/python3.13/unittest/case.py:651: in run
    self._callTestMethod(testMethod)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_stack.TestStack testMethod=test_pop>, method = <bound method TestStack.test_pop of <test_stack.TestStack testMethod=test_pop>>

    def _callTestMethod(self, method):
>       if method() is not None:
E       TypeError: TestStack.test_pop() takes 0 positional arguments but 1 was given

/usr/lib/python3.13/unittest/case.py:606: TypeError
=============================================================================== warnings summary ===============================================================================
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    inlocs = ast.Compare(ast.Str(name.id), [ast.In()], [locs])

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expr = ast.IfExp(test, self.display(name), ast.Str(name.id))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    syms.append(ast.Str(sym))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expls.append(ast.Str(expl))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: 30 warnings
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    keys = [ast.Str(key) for key in current.keys()]

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    assertmsg = ast.Str("")

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    template = ast.BinOp(assertmsg, ast.Add(), ast.Str(explanation))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950: DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead
    clear = ast.Assign(variables, ast.NameConstant(None))

test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================================================================== short test summary info ============================================================================
FAILED test_stack.py::TestStack::test_pop - TypeError: TestStack.test_pop() takes 0 positional arguments but 1 was given
=================================================================== 1 failed, 3 passed, 78 warnings in 0.17s ===================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```

El segundo cambio, nos proporciona el siguiente resultado satisfactorio:

```bash
 
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0 -- /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/bin/python
cachedir: .pytest_cache
Test order randomisation NOT enabled. Enable with --random-order or --random-order-bucket=<bucket_type>
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0, random-order-1.1.1
collected 4 items                                                                                                                                                              

test_stack.py::TestStack::test_is_empty PASSED                                                                                                                           [ 25%]
test_stack.py::TestStack::test_peek PASSED                                                                                                                               [ 50%]
test_stack.py::TestStack::test_pop PASSED                                                                                                                                [ 75%]
test_stack.py::TestStack::test_push PASSED                                                                                                                               [100%]

=============================================================================== warnings summary ===============================================================================
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    inlocs = ast.Compare(ast.Str(name.id), [ast.In()], [locs])

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expr = ast.IfExp(test, self.display(name), ast.Str(name.id))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    syms.append(ast.Str(sym))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expls.append(ast.Str(expl))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: 20 warnings
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    keys = [ast.Str(key) for key in current.keys()]

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    assertmsg = ast.Str("")

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    template = ast.BinOp(assertmsg, ast.Add(), ast.Str(explanation))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950: DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead
    clear = ast.Assign(variables, ast.NameConstant(None))

test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================== 4 passed, 54 warnings in 0.10s ========================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```



### **Paso 7: Escribiendo aserciones para el `método push()`**

Como se espera, error en la modificación:

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0 -- /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/bin/python
cachedir: .pytest_cache
Test order randomisation NOT enabled. Enable with --random-order or --random-order-bucket=<bucket_type>
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0, random-order-1.1.1
collected 4 items                                                                                                                                                              

test_stack.py::TestStack::test_is_empty PASSED                                                                                                                           [ 25%]
test_stack.py::TestStack::test_peek PASSED                                                                                                                               [ 50%]
test_stack.py::TestStack::test_pop PASSED                                                                                                                                [ 75%]
test_stack.py::TestStack::test_push FAILED                                                                                                                               [100%]

=================================================================================== FAILURES ===================================================================================
_____________________________________________________________________________ TestStack.test_push ______________________________________________________________________________

self = <unittest.case._Outcome object at 0x710972697a80>, test_case = <test_stack.TestStack testMethod=test_push>, subTest = False

    @contextlib.contextmanager
    def testPartExecutor(self, test_case, subTest=False):
        old_success = self.success
        self.success = True
        try:
>           yield

/usr/lib/python3.13/unittest/case.py:58: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/lib/python3.13/unittest/case.py:651: in run
    self._callTestMethod(testMethod)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_stack.TestStack testMethod=test_push>, method = <bound method TestStack.test_push of <test_stack.TestStack testMethod=test_push>>

    def _callTestMethod(self, method):
>       if method() is not None:
E       TypeError: TestStack.test_push() takes 0 positional arguments but 1 was given

/usr/lib/python3.13/unittest/case.py:606: TypeError
=============================================================================== warnings summary ===============================================================================
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    inlocs = ast.Compare(ast.Str(name.id), [ast.In()], [locs])

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expr = ast.IfExp(test, self.display(name), ast.Str(name.id))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    syms.append(ast.Str(sym))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expls.append(ast.Str(expl))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: 30 warnings
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    keys = [ast.Str(key) for key in current.keys()]

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    assertmsg = ast.Str("")

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    template = ast.BinOp(assertmsg, ast.Add(), ast.Str(explanation))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950: DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead
    clear = ast.Assign(variables, ast.NameConstant(None))

test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================================================================== short test summary info ============================================================================
FAILED test_stack.py::TestStack::test_push - TypeError: TestStack.test_push() takes 0 positional arguments but 1 was given
=================================================================== 1 failed, 3 passed, 78 warnings in 0.18s ===================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```

Continuamos con la segunda modificación, la cual funciona correctamente|:

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest -v
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0 -- /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/bin/python
cachedir: .pytest_cache
Test order randomisation NOT enabled. Enable with --random-order or --random-order-bucket=<bucket_type>
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0, random-order-1.1.1
collected 4 items                                                                                                                                                              

test_stack.py::TestStack::test_is_empty PASSED                                                                                                                           [ 25%]
test_stack.py::TestStack::test_peek PASSED                                                                                                                               [ 50%]
test_stack.py::TestStack::test_pop PASSED                                                                                                                                [ 75%]
test_stack.py::TestStack::test_push PASSED                                                                                                                               [100%]

=============================================================================== warnings summary ===============================================================================
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:962: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    inlocs = ast.Compare(ast.Str(name.id), [ast.In()], [locs])

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:965: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expr = ast.IfExp(test, self.display(name), ast.Str(name.id))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1075: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    syms.append(ast.Str(sym))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:1077: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    expls.append(ast.Str(expl))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: 20 warnings
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:826: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    keys = [ast.Str(key) for key in current.keys()]

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:936: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    assertmsg = ast.Str("")

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:938: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    template = ast.BinOp(assertmsg, ast.Add(), ast.Str(explanation))

../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
../../venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950
  /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/venv/lib/python3.13/site-packages/_pytest/assertion/rewrite.py:950: DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead
    clear = ast.Assign(variables, ast.NameConstant(None))

test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================== 4 passed, 54 warnings in 0.11s ========================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```



### Paso 9: Agregando coberturas de pruebas con pytest-cov

```bash
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ pytest --cov=stack --cov-report term-missing
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.13.3, pytest-7.1.2, pluggy-1.5.0
Test order randomisation NOT enabled. Enable with --random-order or --random-order-bucket=<bucket_type>
rootdir: /home/amirmiir/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas
plugins: cov-3.0.0, Faker-37.1.0, random-order-1.1.1
collected 4 items                                                                                                                                                              

test_stack.py ....                                                                                                                                                       [100%]

=============================================================================== warnings summary ===============================================================================
test_stack.py::TestStack::test_is_empty
test_stack.py::TestStack::test_peek
test_stack.py::TestStack::test_pop
test_stack.py::TestStack::test_push
  /usr/lib/python3.13/unittest/case.py:597: RuntimeWarning: TestResult has no addDuration method
    warnings.warn("TestResult has no addDuration method",

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

---------- coverage: platform linux, python 3.13.3-final-0 -----------
Name       Stmts   Miss  Cover   Missing
----------------------------------------
stack.py      12      0   100%
----------------------------------------
TOTAL         12      0   100%

======================================================================== 4 passed, 4 warnings in 0.29s =========================================================================
(venv) amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/Actividades10-16/Actividades/aserciones_pruebas(main)$ 

```



