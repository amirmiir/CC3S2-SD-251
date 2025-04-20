# Inicio de la actividad durante la sesión de clase

### Prueba fast forward merge

```

[amirmiir@zenbook14-aacg-EndOS Actividad5]$ mkdir prueba-fast-forward-merge
[amirmiir@zenbook14-aacg-EndOS Actividad5]$ cd prueba-fast-forward-merge/
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ git init
Initialized empty Git repository in /home/amirmiir/Escritorio/UNI/ds-251/Actividad5/prueba-fast-forward-merge/.git/
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ echo "# Mi Proyecto" > README.md
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ git add README.md 
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ git commit -m "Commit inicial en main"
[main (root-commit) d069068] Commit inicial en main
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ 
```

```
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ git checkout -b add-description
Switched to a new branch 'add-description'
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ echo "Este proyecto es un ejemplo de como usar Git" >> README.md
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ git add README.md
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ git commit -m "Agregar descripcion al README.md"
[add-description ddbaecc] Agregar descripcion al README.md
 1 file changed, 1 insertion(+)
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ git checkout main
Switched to branch 'main'
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ 
```

Realizamos merge

```
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ git merge add-description
Updating d069068..ddbaecc
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ git log --graph --oneline
* ddbaecc (HEAD -> main, add-description) Agregar descripcion al README.md
* d069068 Commit inicial en main
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ 
```

### Prueba no fast forward merge

```
[amirmiir@zenbook14-aacg-EndOS prueba-fast-forward-merge]$ cd ..
[amirmiir@zenbook14-aacg-EndOS Actividad5]$ mkdir prueba-no-fast-forward-merge
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ git init
Initialized empty Git repository in /home/amirmiir/Escritorio/UNI/ds-251/Actividad5/prueba-no-fast-forward-merge/.git/
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ echo "# Mi Proyecto" > README.md
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ git add README.md 
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ git commit -m "Commit inicial en main"
[main (root-commit) 705e16e] Commit inicial en main
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ git checkout -b add-feature
Switched to a new branch 'add-feature'
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ echo "Implementando una nueva caracteristica..." >> README.md
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ git add README.md 
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ git commit -m "Implementar nueva caracteristica"
[add-feature 56d3060] Implementar nueva caracteristica
 1 file changed, 1 insertion(+)
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ git checkout main
Switched to branch 'main'
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ git merge --no-ff add-feature 
Merge made by the 'ort' strategy.
 README.md | 1 +
 1 file changed, 1 insertion(+)
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ git log --graph --oneline
*   d258973 (HEAD -> main) Merge branch 'add-feature'
|\  
| * 56d3060 (add-feature) Implementar nueva caracteristica
|/  
* 705e16e Commit inicial en main
[amirmiir@zenbook14-aacg-EndOS prueba-no-fast-forward-merge]$ 

```

### Prueba Squash Merge

```
[amirmiir@zenbook14-aacg-EndOS Actividad5]$ mkdir prueba-squash-merge
[amirmiir@zenbook14-aacg-EndOS Actividad5]$ cd prueba-squash-merge/
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git init
Initialized empty Git repository in /home/amirmiir/Escritorio/UNI/ds-251/Actividad5/prueba-squash-merge/.git/
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ echo "# Mi Proyecto" > README.md
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git add README.md
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git commit -m "Commit inicial en main"
[main (root-commit) 02727ed] Commit inicial en main
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git checkout -b add-basic-files
Switched to a new branch 'add-basic-files'
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ echo "# COMO CONTRIBUIR" > CONTRIBUTING.md 
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git add CONTRIBUTING.md 
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git commit -m "Agregar CONTRIBUTING.md"
[add-basic-files aa5a439] Agregar CONTRIBUTING.md
 1 file changed, 1 insertion(+)
 create mode 100644 CONTRIBUTING.md
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ echo "# LICENCIA" >> LICENSE.txt
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git add LICENSE.txt 
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git commit -m "Agregar LICENSE.txt"
[add-basic-files 48dcfe2] Agregar LICENSE.txt
 1 file changed, 1 insertion(+)
 create mode 100644 LICENSE.txt

```

Se procede con el merge --squash

```
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git checkout main
Switched to branch 'main'
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git merge --squash add-basic-files 
Updating 02727ed..48dcfe2
Fast-forward
Squash commit -- not updating HEAD
 CONTRIBUTING.md | 1 +
 LICENSE.txt     | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 CONTRIBUTING.md
 create mode 100644 LICENSE.txt
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git add .
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git commit -m "Agregar documentación estándar del repositorio"
[main 1297684] Agregar documentación estándar del repositorio
 2 files changed, 2 insertions(+)
 create mode 100644 CONTRIBUTING.md
 create mode 100644 LICENSE.txt
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ git log --graph --oneline
* 1297684 (HEAD -> main) Agregar documentación estándar del repositorio
* 02727ed Commit inicial en main
[amirmiir@zenbook14-aacg-EndOS prueba-squash-merge]$ 
```

### Prueba Merge Conflict

```bash
[amirmiir@zenbook14-aacg-EndOS Actividad5]$ cd prueba-merge-conflict
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ ls
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git init
Initialized empty Git repository in /home/amirmiir/Escritorio/UNI/ds-251/Actividad5/prueba-merge-conflict/.git/
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ echo "<html><body><h1> Proyecto Inicial </h1></body></html>" > index.html 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git add index.html 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git commit -m "commit inicial del index-html en main"
[main (root-commit) 8604ca6] commit inicial del index-html en main
 1 file changed, 1 insertion(+)
 create mode 100644 index.html
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git checkout -b feature-update
Switched to a new branch 'feature-update'
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ echo "<p>...</p>" >> index.html
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ cat index.html
<html><body><h1> Proyecto Inicial </h1></body></html>
<p>...</p>
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git add index.html 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git commit -m "Actualiza..."
[feature-update 6c1bc25] Actualiza...
 1 file changed, 1 insertion(+)
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git checkout main
Switched to branch 'main'
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ cat index.html
<html><body><h1> Proyecto Inicial </h1></body></html>
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ echo "<footer>Contacta aquí example@example.com </footer>" >> index.html
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git add index.html 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git commit -m "...index.html"
[main b058a75] ...index.html
 1 file changed, 1 insertion(+)
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ cat index.html
<html><body><h1> Proyecto Inicial </h1></body></html>
<footer>Contacta aquí example@example.com </footer>
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ 
```

Procedemos a resolver el conflicto con nano:

```bash
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git merge --no-ff feature-update 
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ nano index.html 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ cat index.html
<html><body><h1> Proyecto Inicial </h1></body></html>

<footer>Contacta aquí example@example.com </footer>

<p>...</p>

[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git add index.html 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git commit
[main 377dca1] Merge branch 'feature-update'
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ 
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ git log --graph --oneline
*   377dca1 (HEAD -> main) Merge branch 'feature-update'
|\  
| * 6c1bc25 (feature-update) Actualiza...
* | b058a75 ...index.html
|/  
* 8604ca6 commit inicial del index-html en main
[amirmiir@zenbook14-aacg-EndOS prueba-merge-conflict]$ 

```



### Prueba Compare Merge

```bash
```

