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

