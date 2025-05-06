# PD 3 - Reporte

## Procedimiento de la actividad

### Inicio del Script y Agregación de submódulo

Para la ejecución del codigo descargamos git_avanzado.sh, lo ubicamos en nuestra carpeta (por comodidad), lo convertimos en ejecutable. Luego, lo ejecutamos para elegir las siguientes opciones.

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/PD3$ ./git_avanzado.sh 

====== Menú avanzado de Git ======
1) Listar reflog y restaurar un commit
2) Agregar un submódulo
3) Agregar un subtree
4) Gestión de ramas
5) Gestión de stashes
6) Mostrar estado y últimos commits
7) Gestión de tags
8) Gestión de git bisect
9) Gestión de git diff
10) Gestión de Hooks
11) Salir
Seleccione una opción: 2

Ingrese la URL del repositorio para el submódulo: git@github.com:amirmiir/CC3S2-PD3.git
Ingrese el directorio donde se ubicará el submódulo: ./libs
Cloning into '/home/amirmiir/Escritorio/UNI/CC3S2-SD-251/PD3/libs'...
Enter passphrase for key '/home/amirmiir/.ssh/id_ed25519': 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.
Submódulo agregado en: ./libs

====== Menú avanzado de Git ======
1) Listar reflog y restaurar un commit
2) Agregar un submódulo
3) Agregar un subtree
4) Gestión de ramas
5) Gestión de stashes
6) Mostrar estado y últimos commits
7) Gestión de tags
8) Gestión de git bisect
9) Gestión de git diff
10) Gestión de Hooks
11) Salir
Seleccione una opción: 11
Saliendo del script.
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/PD3$ 

```

#### ¿Qué hace?

El código, por detrás, está ejecutando el siguiente código con la información que nos ha solicitado.

``` bash
git submodule add https://github.com/usuario/repositorio-submodulo.git libs/submodulo
git submodule update --init --recursive
```

Y verificamos que se ha ejecutado de manera apropiada en la siguiente linea `Submódulo agregado en: ./libs`



### Gestión de ramas



