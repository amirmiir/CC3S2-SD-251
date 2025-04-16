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
Pasos 1 y 2:
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch feature/advanced-feature
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch
  develop
  feature/advanced-feature
* feature/login
  hotfix/bugfix
  main
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout feature/advanced-feature 
Switched to branch 'feature/advanced-feature'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ kate main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "feat: added greet function in advanced feature"
[feature/advanced-feature ff2e807] feat: added greet function in advanced feature
 1 file changed, 4 insertions(+), 1 deletion(-)
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

Paso 3 y 4: Realizamos cambios en main, y luego procedemos a intentar un merge con la rama feature/advanced-feature

```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout main
Switched to branch 'main'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ echo "print('Hello World - updated in main')" > main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "feat: Update main.py message in main branch"
[main 5f4c951] feat: Update main.py message in main branch
 1 file changed, 1 insertion(+), 1 deletion(-)
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git merge feature/advanced-feature 
Auto-merging main.py
CONFLICT (content): Merge conflict in main.py
Automatic merge failed; fix conflicts and then commit the result.
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

Pasos 5 y 6:
Abrimos el archivo en conflicto en vscode para utilizar su gestor de conflictos y resolver el conflicto manualmente. Elijo 'accept incoming change' para elegir el cambio de la rama que está fusionandose con nuestra rama actual.

```
Automatic merge failed; fix conflicts and then commit the result.
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ code main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "feat: Resolve merge conflict between main and feature/advanced-feature"
[main 07ad9bc] feat: Resolve merge conflict between main and feature/advanced-feature
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

Realizamos la eliminación de la rama que se ha fusionado.

```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch -d feature/advanced-feature 
Deleted branch feature/advanced-feature (was ff2e807).
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch
  develop
  feature/login
  hotfix/bugfix
* main
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```


## Ejercicio 2
Ejecutamos el comando _git log -p_:
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log -p
commit 07ad9bc09c5843efd5288db90814dbda2aa56656 (HEAD -> main)
Merge: 5f4c951 ff2e807
Author: amirmiir <00aamircg@gmail.com>
Date:   Tue Apr 15 15:10:59 2025 -0500

    feat: Resolve merge conflict between main and feature/advanced-feature

commit 5f4c9517d6572a78f41b3f4ca790fd4cb95a8833
Author: amirmiir <00aamircg@gmail.com>
Date:   Tue Apr 15 15:06:55 2025 -0500

    feat: Update main.py message in main branch

diff --git a/main.py b/main.py
index 2307a3a..971e8f4 100644
--- a/main.py
+++ b/main.py
@@ -1 +1 @@
-print('This belongs to feature/login')
+print('Hello World - updated in main')

commit ff2e807904eb2f19c996ff370f4a536f214ac0b8
Author: amirmiir <00aamircg@gmail.com>
Date:   Tue Apr 15 15:03:35 2025 -0500

    feat: added greet function in advanced feature

diff --git a/main.py b/main.py
index 2307a3a..40d2543 100644
--- a/main.py
+++ b/main.py
@@ -1 +1,4 @@
-print('This belongs to feature/login')
+def greet():
+    print('Hello from advanced feature')
+
+greet()

commit 413961241d73735b31247ee831ffa53a0e9a34f9 (feature/login)
Author: amirmiir <00aamircg@gmail.com>
Date:   Tue Apr 15 12:09:26 2025 -0500

    feat: changed main.py

diff --git a/main.py b/main.py
index df1dc68..2307a3a 100644
--- a/main.py
+++ b/main.py
@@ -1 +1 @@
-print('Hello World')
+print('This belongs to feature/login')
```

Realizamos la busqueda de los cambios realizados por mí, _git log --author="amirmiir"_
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --author="amirmiir"
commit 07ad9bc09c5843efd5288db90814dbda2aa56656 (HEAD -> main)
Merge: 5f4c951 ff2e807
Author: amirmiir <00aamircg@gmail.com>
Date:   Tue Apr 15 15:10:59 2025 -0500

    feat: Resolve merge conflict between main and feature/advanced-feature

commit 5f4c9517d6572a78f41b3f4ca790fd4cb95a8833
Author: amirmiir <00aamircg@gmail.com>
Date:   Tue Apr 15 15:06:55 2025 -0500

    feat: Update main.py message in main branch

commit ff2e807904eb2f19c996ff370f4a536f214ac0b8
Author: amirmiir <00aamircg@gmail.com>
Date:   Tue Apr 15 15:03:35 2025 -0500

    feat: added greet function in advanced feature

commit 413961241d73735b31247ee831ffa53a0e9a34f9 (feature/login)
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

Ejecutamos el comando _git revert HEAD_
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git revert HEAD
error: commit 07ad9bc09c5843efd5288db90814dbda2aa56656 is a merge but no -m option was given.
fatal: revert failed
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```
Dado que el último commit proviene de un merge, nos pide utilizar el parámetro _-m_ para elegir cual de los padres será rama fuente para prevalecer en nuestra rama actual.
Ejecutamos _git revert -m 1 HEAD_
```
se abre en consola:
Revert "feat: Resolve merge conflict between main and feature/advanced-feature"

This reverts commit 07ad9bc09c5843efd5288db90814dbda2aa56656, reversing
changes made to 5f4c9517d6572a78f41b3f4ca790fd4cb95a8833.

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Changes to be committed:
#       modified:   main.py
#
```

Y se obtiene en terminal:
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git revert -m 1 HEAD
[main 3d668d6] Revert "feat: Resolve merge conflict between main and feature/advanced-feature"
 1 file changed, 7 deletions(-)
```

Se han estado presentando errores en la reversión del merge, por lo que decidí crear un nuevo commit para verificar el cambio del estado, el cual ha resultado satisfactorio.

 ```
 [amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ echo "print('hello world - recent main change')" > main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "feat: modified main.py for future revert"
[main c7a4024] feat: modified main.py for future revert
 1 file changed, 1 insertion(+), 1 deletion(-)
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main
nothing to commit, working tree clean
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --oneline
c7a4024 (HEAD -> main) feat: modified main.py for future revert
112083f Revert "Reapply "feat: Resolve merge conflict between main and feature/advanced-feature""
1af2369 Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
3d668d6 Revert "feat: Resolve merge conflict between main and feature/advanced-feature"
07ad9bc feat: Resolve merge conflict between main and feature/advanced-feature
5f4c951 feat: Update main.py message in main branch
ff2e807 feat: added greet function in advanced feature
4139612 (feature/login) feat: changed main.py
8238124 (develop) Add main.py
34f7128 Set up the repository base documentation
fad1331 (hotfix/bugfix) Corrected, initial commit with README.md
1ddb19c Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git revert HEAD
[main aa83101] Revert "feat: modified main.py for future revert"
 1 file changed, 1 insertion(+), 1 deletion(-)
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --oneline
aa83101 (HEAD -> main) Revert "feat: modified main.py for future revert"
c7a4024 feat: modified main.py for future revert
112083f Revert "Reapply "feat: Resolve merge conflict between main and feature/advanced-feature""
1af2369 Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
3d668d6 Revert "feat: Resolve merge conflict between main and feature/advanced-feature"
07ad9bc feat: Resolve merge conflict between main and feature/advanced-feature
5f4c951 feat: Update main.py message in main branch
ff2e807 feat: added greet function in advanced feature
4139612 (feature/login) feat: changed main.py
8238124 (develop) Add main.py
34f7128 Set up the repository base documentation
fad1331 (hotfix/bugfix) Corrected, initial commit with README.md
1ddb19c Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ code main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
 ```
 Realizamos el rebase:
 
 ```
 [amirmiir@zenbook14-aacg-EndOS ejercicios]$ git rebase -i HEAD~4
You asked to amend the most recent commit, but doing so would make
it empty. You can repeat your command with --allow-empty, or you can
remove the commit entirely with "git reset HEAD^".
interactive rebase in progress; onto 3d668d6
Last commands done (2 commands done):
   pick 1af2369 Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
   squash 112083f Revert "Reapply "feat: Resolve merge conflict between main and feature/advanced-feature""
Next commands to do (2 remaining commands):
   squash c7a4024 feat: modified main.py for future revert
   squash aa83101 Revert "feat: modified main.py for future revert"
  (use "git rebase --edit-todo" to view and edit)
You are currently rebasing branch 'main' on '3d668d6'.
  (all conflicts fixed: run "git rebase --continue")

No changes
Could not apply 112083f... Revert "Reapply "feat: Resolve merge conflict between main and feature/advanced-feature""
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --oneline
1af2369 (HEAD) Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
3d668d6 Revert "feat: Resolve merge conflict between main and feature/advanced-feature"
07ad9bc feat: Resolve merge conflict between main and feature/advanced-feature
5f4c951 feat: Update main.py message in main branch
ff2e807 feat: added greet function in advanced feature
4139612 (feature/login) feat: changed main.py
8238124 (develop) Add main.py
34f7128 Set up the repository base documentation
fad1331 (hotfix/bugfix) Corrected, initial commit with README.md
1ddb19c Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
 ```
 
 Ejecutamos el grafo, y verificamos que la forma ya no es lineal:
 
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'
*        1af2369 2 hours ago ("amirmiir") Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
*        3d668d6 2 hours ago ("amirmiir") Revert "feat: Resolve merge conflict between main and feature/advanced-feature"
*        07ad9bc 2 hours ago ("amirmiir") feat: Resolve merge conflict between main and feature/advanced-feature
|\  
| *      ff2e807 2 hours ago ("amirmiir") feat: added greet function in advanced feature
* |      5f4c951 2 hours ago ("amirmiir") feat: Update main.py message in main branch
|/  
*        4139612 5 hours ago ("amirmiir") feat: changed main.py
*        8238124 30 hours ago ("amirmiir") Add main.py
*        34f7128 30 hours ago ("amirmiir") Set up the repository base documentation
*        fad1331 31 hours ago ("amirmiir") Corrected, initial commit with README.md
*        1ddb19c 31 hours ago ("amirmiir") Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```
 
## Ejercicio 3: Creación y gestión de ramas desde commits específicos
Procedemos a seguir las instrucciones y elegimos como commit de origen para nuestra rama: '07ad9bc'
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --oneline
1af2369 (HEAD) Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
3d668d6 Revert "feat: Resolve merge conflict between main and feature/advanced-feature"
07ad9bc feat: Resolve merge conflict between main and feature/advanced-feature
5f4c951 feat: Update main.py message in main branch
ff2e807 feat: added greet function in advanced feature
4139612 (feature/login) feat: changed main.py
8238124 (develop) Add main.py
34f7128 Set up the repository base documentation
fad1331 (hotfix/bugfix) Corrected, initial commit with README.md
1ddb19c Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch bugfix/rollback-feature 07ad9bc
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout bugfix/rollback-feature 
M       main.py
Previous HEAD position was 1af2369 Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
Switched to branch 'bugfix/rollback-feature'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ code main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ kate main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "fix: fix bug in rollback feature"
[bugfix/rollback-feature 29e0f74] fix: fix bug in rollback feature
 1 file changed, 1 insertion(+), 7 deletions(-)
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout main
Switched to branch 'main'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

Realizamos el cambio al main, y notamos que se presenta un bug en mi versión de vscode la cual está cargando una versión antigua del archivo main.py, para la cual no se presentan las indicaciones pertinentes para realizar un merge con conflictos y resolverlo manualmente.

```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout main
Switched to branch 'main'
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git merge bugfix/rollback-feature 
Auto-merging main.py
CONFLICT (content): Merge conflict in main.py
Automatic merge failed; fix conflicts and then commit the result.
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ code main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git merge bugfix/rollback-feature 
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch
  bugfix/rollback-feature
  develop
  feature/login
  hotfix/bugfix
* main
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git checkout bugfix/rollback-feature 
main.py: needs merge
error: you need to resolve your current index first
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main
Last commands done (2 commands done):
   pick 1af2369 Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
   squash 112083f Revert "Reapply "feat: Resolve merge conflict between main and feature/advanced-feature""
Next commands to do (2 remaining commands):
   squash c7a4024 feat: modified main.py for future revert
   squash aa83101 Revert "feat: modified main.py for future revert"
  (use "git rebase --edit-todo" to view and edit)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch
  bugfix/rollback-feature
  develop
  feature/login
  hotfix/bugfix
* main
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ code main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ kate main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ code main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ code main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "fix: fix bug in rollback feature"
[main 9d20e99] fix: fix bug in rollback feature
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```
Realizamos la ejecución de _git log --graph --oneline_
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git log --graph --oneline
*   9d20e99 (HEAD -> main) fix: fix bug in rollback feature
|\  
| * 29e0f74 (bugfix/rollback-feature) fix: fix bug in rollback feature
* | aa83101 Revert "feat: modified main.py for future revert"
* | c7a4024 feat: modified main.py for future revert
* | 112083f Revert "Reapply "feat: Resolve merge conflict between main and feature/advanced-feature""
* | 1af2369 Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
* | 3d668d6 Revert "feat: Resolve merge conflict between main and feature/advanced-feature"
|/  
*   07ad9bc feat: Resolve merge conflict between main and feature/advanced-feature
|\  
| * ff2e807 feat: added greet function in advanced feature
* | 5f4c951 feat: Update main.py message in main branch
|/  
* 4139612 (feature/login) feat: changed main.py
* 8238124 (develop) Add main.py
* 34f7128 Set up the repository base documentation
* fad1331 (hotfix/bugfix) Corrected, initial commit with README.md
* 1ddb19c Initial commit with README
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

Y eliminamos la rama utilizada.
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch -d bugfix/rollback-feature 
Deleted branch bugfix/rollback-feature (was 29e0f74).
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```


## Ejercicio 4: Manipulación y restauración de commits con git reset y git restore

We edit the main.py file to address a change a to be changed.
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git branch
  develop
  feature/login
  hotfix/bugfix
* main
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ echo "print('This change will be reset')" > main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git add main.py
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git commit -m "feat: Introduce a change to be reset"
[main a80193f] feat: Introduce a change to be reset
 1 file changed, 1 insertion(+), 2 deletions(-)
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

Regresamos a una versión anterior.
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git reset --hard HEAD~1
HEAD is now at 9d20e99 fix: fix bug in rollback feature
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```

Seguimos la guía y vemos el funcionamiento de _git restore_ para un archivo específico.
```
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ echo "Another line in README" >> README.md
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main
Last commands done (2 commands done):
   pick 1af2369 Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
   squash 112083f Revert "Reapply "feat: Resolve merge conflict between main and feature/advanced-feature""
Next commands to do (2 remaining commands):
   squash c7a4024 feat: modified main.py for future revert
   squash aa83101 Revert "feat: modified main.py for future revert"
  (use "git rebase --edit-todo" to view and edit)
You are currently editing a commit while rebasing branch 'main' on '3d668d6'.
  (use "git commit --amend" to amend the current commit)
  (use "git rebase --continue" once you are satisfied with your changes)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git restore README.md
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ git status
On branch main
Last commands done (2 commands done):
   pick 1af2369 Reapply "feat: Resolve merge conflict between main and feature/advanced-feature"
   squash 112083f Revert "Reapply "feat: Resolve merge conflict between main and feature/advanced-feature""
Next commands to do (2 remaining commands):
   squash c7a4024 feat: modified main.py for future revert
   squash aa83101 Revert "feat: modified main.py for future revert"
  (use "git rebase --edit-todo" to view and edit)
You are currently editing a commit while rebasing branch 'main' on '3d668d6'.
  (use "git commit --amend" to amend the current commit)
  (use "git rebase --continue" once you are satisfied with your changes)

nothing to commit, working tree clean
[amirmiir@zenbook14-aacg-EndOS ejercicios]$ 
```
Ejecutamos kate README.md para verificar el contenido, y se muestra el siguiente contenido:
```
 README \n\nWelcome to the project
```

## Ejercicio 5

Creamos un repositorio con un README.md vacío en Github y lo clonamos.
```
[amirmiir@zenbook14-aacg-EndOS UNI]$ git clone git@github.com:amirmiir/testing-for-activities.git testing-for-activities
Cloning into 'testing-for-activities'...
Enter passphrase for key '/home/amirmiir/.ssh/id_ed25519': 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.
[amirmiir@zenbook14-aacg-EndOS UNI]$ 
[amirmiir@zenbook14-aacg-EndOS UNI]$ ls
ds-251  NUM1  testing-for-activities  trivia-game-python
[amirmiir@zenbook14-aacg-EndOS UNI]$ cd testing-for-activities/
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ 
```
Continuamos con la creación de collaboration.py

```
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ git branch feature/team-feature
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ git checkout feature/team-feature 
Switched to branch 'feature/team-feature'
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ echo "print('Collaboration is key\!')" > collaboration.py
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ 
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ git add .
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ git commit -m "feat: add collaboration script"
[feature/team-feature 2562e25] feat: add collaboration script
 1 file changed, 1 insertion(+)
 create mode 100644 collaboration.py
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ 
```
Enviamos los cambios realizados al repositorio:
```
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ git push origin feature/team-feature
Enter passphrase for key '/home/amirmiir/.ssh/id_ed25519': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 324 bytes | 324.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'feature/team-feature' on GitHub by visiting:
remote:      https://github.com/amirmiir/testing-for-activities/pull/new/feature/team-feature
remote: 
To github.com:amirmiir/testing-for-activities.git
 * [new branch]      feature/team-feature -> feature/team-feature
[amirmiir@zenbook14-aacg-EndOS testing-for-activities]$ 
```

![imagen de pull request en github](Actividad4/misc/ej5_1.png)


## Ejercicio 6





