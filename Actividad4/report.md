### Ejercicios introductorios

Se nos pide crear un repositorio

realizamos el cambio de directorio, a un directorio dentro de Actividades4:

Inicializamos el repositoriom y agregamos el README. Verificamos su estado, el cual nos indica que hay archivos pendientes de ser añadidos como cambios a la rama actual.
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git init
Initialized empty Git repository in /home/amirmiir/Escritorio/UNI/ds-251/Actividad4/ejercicios/.git/
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ echo "README" > README.md
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        report.md

nothing added to commit but untracked files present (use "git add" to track)
```

Añadimos los archivos a través de _git add <nombre_de_archivo>_:
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add README.md
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        report.md

[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add report.md

```
Para pasar de Staged -> Unstaged con _git rm --cached <nombre_de_archivo>_...

```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
        new file:   report.md

[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "Initial commit with README"
[main (root-commit) 1ddb19c] Initial commit with README
 2 files changed, 48 insertions(+)
 create mode 100644 README.md
 create mode 100644 report.md
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main
nothing to commit, working tree clean
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 

```

Revisamos el log de commits:
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "Corrected, initial commit with README.md"
[main fad1331] Corrected, initial commit with README.md
 1 file changed, 47 deletions(-)
 delete mode 100644 report.md
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log
commit fad133172f091862e68e85a09b1ace3878392a4e (HEAD -> main)
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 10:34:38 2025 -0500

    Corrected, initial commit with README.md

commit 1ddb19ca453bef663ca8610cb50de662e435e39d
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 10:32:10 2025 -0500

    Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 

```

Mostramos el árbol correspondiente al historial de cambios (nos muestra un grafo lineal, pues solo se han ejecutado cambios en una rama, main, hasta el momento):
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'
*        fad1331 83 seconds ago ("amirmiir") Corrected, initial commit with README.md
*        1ddb19c 4 minutes ago ("amirmiir") Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 

```

Seguimos la guía y creamos CONTRIBUTING.md y modificamos README.md

```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ echo " README \\n\\nWelcome to the project" > README.md
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ kate README.md
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add .
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ echo " CONTRIBUTING" > CONTRIBUTING.md 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add .
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "Set up the repository base documentation"
[main 34f7128] Set up the repository base documentation
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 CONTRIBUTING.md
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 

```

Añadimos main.py y verificamos el log.

```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ echo "print('Hello World')" > main.py 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add .
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "Add main.py"
[main 8238124] Add main.py
 1 file changed, 1 insertion(+)
 create mode 100644 main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --oneline
8238124 (HEAD -> main) Add main.py
34f7128 Set up the repository base documentation
fad1331 Corrected, initial commit with README.md
1ddb19c Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'
*        8238124 17 seconds ago ("amirmiir") Add main.py
*        34f7128 36 minutes ago ("amirmiir") Set up the repository base documentation
*        fad1331 69 minutes ago ("amirmiir") Corrected, initial commit with README.md
*        1ddb19c 71 minutes ago ("amirmiir") Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
 ```

 Creamos una nueva rama y revisamos las ramas existentes:

 ```
 [amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch
* main
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch feature/new-feature
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch
  feature/new-feature
* main
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout feature/new-feature 
Switched to branch 'feature/new-feature'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

Realizamos las instrucciones, para crear una nueva rama basada en la rama develop.

```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch
  develop
* feature/new-feature
  main
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout develop
Switched to branch 'develop'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch feature/login develop
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout feature/login
Switched to branch 'feature/login'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

Creamos una rama basada en un commit anterior.

```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --oneline
8238124 (HEAD -> feature/login, main, feature/new-feature, develop) Add main.py
34f7128 Set up the repository base documentation
fad1331 Corrected, initial commit with README.md
1ddb19c Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch hotfix/bugfix fad1331
```
### git switch:z
Busca crear una nueva rama y cambiar a esta, en versiones más recientes de git.
```
git switch -c <nombre_nueva_rama>
```

### git merge: fusionando dos ramas
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout main
Switched to branch 'main'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git merge feature/new-feature 
Already up to date.
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

### git branch -d: eliminando una rama

```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch -d feature/new-feature 
Deleted branch feature/new-feature (was 8238124).
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

# Preguntas
## Pregunta 1: ¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?
Me ha permitido poder revisar un historial de mis acciones, mantener un seguimiento ordenando de qué y cuándo se realizó, a través de _git log_, y junto al uso de sus parámetros, una visualización de este historial, a través de un grafo o una vista minima con el mensaje de commit.

## Pregunta 2: ¿Qué beneficios ves en el uso de ramas para desarrollar nuevas características o corregir errores?
Como principal beneficio, observo la separación de trabajo, pues se puede trabajar diferentes características aisladas a la vez y separar sus errores de manera independiente. Para corregir errores, también es muy útil, pues permite realizar un seguimiento de acuerdo al equipo encargado de trabajar en cada rama.
    
## Pregunta 3: Realiza una revisión final del historial de commits para asegurarte de que todos los cambios se han registrado correctamente.
```[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main
nothing to commit, working tree clean
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log
commit 823812442dea39844525e2fcf43a4581c2c2c58c (HEAD -> main, feature/login, develop)
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 11:42:52 2025 -0500

    Add main.py

commit 34f7128492c07376309470bb53749d326a5289f4
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 11:07:37 2025 -0500

    Set up the repository base documentation

commit fad133172f091862e68e85a09b1ace3878392a4e (hotfix/bugfix)
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 10:34:38 2025 -0500

    Corrected, initial commit with README.md

commit 1ddb19ca453bef663ca8610cb50de662e435e39d
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 10:32:10 2025 -0500

    Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --oneline
8238124 (HEAD -> main, feature/login, develop) Add main.py
34f7128 Set up the repository base documentation
fad1331 (hotfix/bugfix) Corrected, initial commit with README.md
1ddb19c Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'
*        8238124 24 hours ago ("amirmiir") Add main.py
*        34f7128 25 hours ago ("amirmiir") Set up the repository base documentation
*        fad1331 25 hours ago ("amirmiir") Corrected, initial commit with README.md
*        1ddb19c 25 hours ago ("amirmiir") Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

## Pregunta 4: Revisa el uso de ramas y merges para ver cómo Git maneja múltiples líneas de desarrollo.
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout feature/login 
Switched to branch 'feature/login'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ kate main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ echo "print('This belongs to feature/login')" > main.py 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add .
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "feat: changed main.py"
[feature/login 4139612] feat: changed main.py
 1 file changed, 1 insertion(+), 1 deletion(-)
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout main
Switched to branch 'main'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main
nothing to commit, working tree clean
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git merge feature/login 
Updating 8238124..4139612
Fast-forward
 main.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```
realizamos el merge para verificar como maneja los merges y el uso de ramas.
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'
*        4139612 2 minutes ago ("amirmiir") feat: changed main.py
*        8238124 24 hours ago ("amirmiir") Add main.py
*        34f7128 25 hours ago ("amirmiir") Set up the repository base documentation
*        fad1331 26 hours ago ("amirmiir") Corrected, initial commit with README.md
*        1ddb19c 26 hours ago ("amirmiir") Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout feature/login 
Switched to branch 'feature/login'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'
*        4139612 3 minutes ago ("amirmiir") feat: changed main.py
*        8238124 24 hours ago ("amirmiir") Add main.py
*        34f7128 25 hours ago ("amirmiir") Set up the repository base documentation
*        fad1331 26 hours ago ("amirmiir") Corrected, initial commit with README.md
*        1ddb19c 26 hours ago ("amirmiir") Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log
commit 413961241d73735b31247ee831ffa53a0e9a34f9 (HEAD -> feature/login, main)
Author: amirmiir <00aamircg@gmail.com>
Date:   Tue Apr 15 12:09:26 2025 -0500

    feat: changed main.py

commit 823812442dea39844525e2fcf43a4581c2c2c58c (develop)
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 11:42:52 2025 -0500

    Add main.py

commit 34f7128492c07376309470bb53749d326a5289f4
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 11:07:37 2025 -0500

    Set up the repository base documentation

commit fad133172f091862e68e85a09b1ace3878392a4e (hotfix/bugfix)
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 10:34:38 2025 -0500

    Corrected, initial commit with README.md

commit 1ddb19ca453bef663ca8610cb50de662e435e39d
Author: amirmiir <00aamircg@gmail.com>
Date:   Mon Apr 14 10:32:10 2025 -0500

    Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

# Ejercicios
## Ejercicio 1
## Ejercicio 2
## Ejercicio 3
## Ejercicio 4
## Ejercicio 5
