### Parte 1 Git Rebase

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6(main)$ mkdir prueba-git-rebase
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6(main)$ cd prueba-git-rebase/
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ git init
Initialized empty Git repository in /home/amirmiir/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase/.git/
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase$ echo "# Mi Proyecto de Rebase" > README.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase$ git add README.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase$ git commit -m "Commit inicial en main"
[main (root-commit) 2857698] Commit inicial en main
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ git checkout -b new-feature
Switched to a new branch 'new-feature'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ echo "Esta es una nueva caracteristica." > NewFeature.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ git add NewFeature.md 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ git commit -m "Agregar nueva caracteristica"
[new-feature 757fc70] Agregar nueva caracteristica
 1 file changed, 1 insertion(+)
 create mode 100644 NewFeature.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ git branch
  main
* new-feature
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ git log --graph --oneline --all --decorate
* 757fc70 (HEAD -> new-feature) Agregar nueva caracteristica
* 2857698 (main) Commit inicial en main
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ 

```

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ git checkout main
Switched to branch 'main'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ echo "Updates to the project." >> Updates.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ git add Updates.md 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ git commit -m "Update main"
[main d56508a] Update main
 1 file changed, 1 insertion(+)
 create mode 100644 Updates.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ git checkout new-feature 
Switched to branch 'new-feature'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ git rebase main
Successfully rebased and updated refs/heads/new-feature.
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ git log --graph --oneline
* f95e1a5 (HEAD -> new-feature) Agregar nueva caracteristica
* d56508a (main) Update main
* 2857698 Commit inicial en main
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ 

```

Merge fast forward

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(new-feature)$ git checkout main
Switched to branch 'main'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ git merge new-feature 
Updating d56508a..f95e1a5
Fast-forward
 NewFeature.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 NewFeature.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ git log --graph --oneline
* f95e1a5 (HEAD -> main, new-feature) Agregar nueva caracteristica
* d56508a Update main
* 2857698 Commit inicial en main
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-git-rebase(main)$ 


```





### Parte 2 Cherry Pick

Inicializacion

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6(main)$ mkdir prueba-cherry-pick
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6(main)$ cd prueba-cherry-pick/
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(main)$ git init
Initialized empty Git repository in /home/amirmiir/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick/.git/
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick$ echo "# Mi proyecto" > README.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick$ git add README.md 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick$ git commit -m "Commit inicial"
[main (root-commit) 4b74410] Commit inicial
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(main)$ git checkout -b add-base-documents
Switched to a new branch 'add-base-documents'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ echo "# CONTRIBUTING" >> CONTRIBUTING.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ git add CONTRIBUTING.md 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ git commit -m "Se agrega CONTRIBUTING.md"
[add-base-documents 86a6fb7] Se agrega CONTRIBUTING.md
 1 file changed, 1 insertion(+)
 create mode 100644 CONTRIBUTING.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ echo "LICENSE" >> LICENSE.txt
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ git add LICENSE.txt 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ git commit -m "Agrega LICENSE.txt"
[add-base-documents 9db0cd7] Agrega LICENSE.txt
 1 file changed, 1 insertion(+)
 create mode 100644 LICENSE.txt
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ git log add-base-documents --graph --oneline
* 9db0cd7 (HEAD -> add-base-documents) Agrega LICENSE.txt
* 86a6fb7 Se agrega CONTRIBUTING.md
* 4b74410 (main) Commit inicial
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ git log --graph --oneline --all --decorate
* 9db0cd7 (HEAD -> add-base-documents) Agrega LICENSE.txt
* 86a6fb7 Se agrega CONTRIBUTING.md
* 4b74410 (main) Commit inicial
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$  

```

 hacemos cherry-pick al commit más reciente:

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(add-base-documents)$ git checkout main
Switched to branch 'main'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(main)$ git cherry-pick 9db0cd7
[main 0711d67] Agrega LICENSE.txt
 Date: Mon Apr 21 10:49:36 2025 -0500
 1 file changed, 1 insertion(+)
 create mode 100644 LICENSE.txt
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(main)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(main)$ git log --graph --oneline
* 0711d67 (HEAD -> main) Agrega LICENSE.txt
* 4b74410 Commit inicial
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/prueba-cherry-pick(main)$ 

```

Notemos que tiene un hash diferente. 0711d67 != 9db0cd7

### Preguntas

#### 1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?



#### 2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?



#### 3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?



#### 4. ¿Por qué es importante evitar hacer rebase en ramas públicas?



### Ejercicios Teóricos

#### 1. Diferencias entre git merge y git rebase

 **Pregunta**: Explica la diferencia entre git merge y git  rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.

#### 2. **Relación entre git rebase y DevOps**
 **Pregunta**: ¿Cómo crees que el uso de git rebase ayuda a  mejorar las prácticas de DevOps, especialmente en la implementación  continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.

#### 3. **Impacto del git cherry-pick en un equipo Scrum**

 **Pregunta**: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que  solo algunos commits específicos de la rama de una funcionalidad deben  aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este  caso? Explica los beneficios y posibles complicaciones.

### Ejercicios Prácticos

#### **1. Simulación de un flujo de trabajo Scrum con git rebase y git merge**

```bash
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6(main)$ mkdir scrum-workflow
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6(main)$ cd scrum-workflow/
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ git init
Initialized empty Git repository in /home/amirmiir/Escritorio/UNI/ds-251/Actividad6/scrum-workflow/.git/
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow$ echo "Commit inicial en main" > mainfile.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow$ git add mainfile.md 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow$ git commit -m "Commit inicial en main"
[main (root-commit) 581e55c] Commit inicial en main
 1 file changed, 1 insertion(+)
 create mode 100644 mainfile.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ git checkout -b feature
Switched to a new branch 'feature'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(feature)$ echo "Nueva caracteristica en feature" > featurefile.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(feature)$ git add featurefile.md 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(feature)$ git commit -m "Commit en feature"
[feature 00638e2] Commit en feature
 1 file changed, 1 insertion(+)
 create mode 100644 featurefile.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(feature)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(feature)$ git checkout main
Switched to branch 'main'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ echo "Actualizacion en main" >> mainfile.md 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ git add mainfile.md 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ git commit -m "Actualizacion en main"
[main 5c50a1a] Actualizacion en main
 1 file changed, 1 insertion(+)
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ 
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ git checkout feature
Switched to branch 'feature'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(feature)$ git rebase main
Successfully rebased and updated refs/heads/feature.
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(feature)$ git checkout main
Switched to branch 'main'
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ git merge feature --ff-only
Updating 5c50a1a..bda654e
Fast-forward
 featurefile.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 featurefile.md
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/ds-251/Actividad6/scrum-workflow(main)$ 

```

#### 2. **Cherry-pick para integración selectiva en un pipeline CI/CD**

#### Preguntas

- ¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?
- ¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?



```bash

```



### Ejercicio 1

### Ejercicio 2

### Ejercicio 3

### Ejercicio 4

### Ejercicio 5