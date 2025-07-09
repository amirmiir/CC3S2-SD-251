# Actividad17 - Reporte

## Parte 1: Github Projects -  Configuración de Kanban Board

![](./images/p1-10.png)

![](./images/p1-13.png)



## Parte 2: Creación de issue template

### Crea una issue template en github

![](./images/p2-2.png)



![](./images/p2-7.png)



## Parte 3: Creación de siete historias de usuarios

### Crear nuevas historias de usuario usando github issues

Se realizaron una modificacion en labels para poder marcar como user story: 

````markdown
amirmiir@zenbook14-aacg-EndOS:~/Escritorio/UNI/CC3S2-SD-251/.github/ISSUE_TEMPLATE(main)$ cat user-story.md 
---
name: User Story
about: This is the user story for the CC3S2 - Activity17 - Part 2.
title: ''
labels: '["user story"]'
assignees: ''

---

---
name: User Story
about: Template for defining clear and structured user stories
title: "[User Story] <Short Title>"
labels: ["user story"]
assignees: ""
---

## User story  

**As a** _(specific role - e.g., "developer," "admin," "customer")_  
**I need** _(clear functionality or feature needed)_  
**So that** _(explain the value or business reason for this feature)_

---

##  **Context & Assumptions**  
- _List any known constraints, assumptions, or dependencies._
- _Mention related user stories or issues (if applicable)._

---

##  **Acceptance criteria**  
```gherkin
Scenario: <Short Description>
Given <initial context or system state>
When <user performs an action>
Then <expected outcome or behavior>
And <optional additional conditions>
````



#### Historias de la lección:

##### 1. Creación de issues

![](./images/p3-1.png)

##### Adición de issues al Kanban board

![](./images/p3-8.png)

##### Ejercicio: Priorizar el product backlog

###### 

## Parte 4:

### 3. Creación de Label

![](./images/p4-label-1.png)

### 4. Añadir labels a las historias

Procedemos a añadir nuestra primera label a la historia indicada en el backlog

![](./images/p4-4-1.png)

![](./images/p4-4-2.png)

## Ejercicios:

### 1. Crear un Epic y vincular historias de usuario

Creamos la épica para"Gestión de Contadores" y le vinculamos historias de usuarios ya existentes.

![](./images/e1-1.png)

Utilizamos la siguiente estructura para poder vincular las issues existentes.

![](./images/e1-2.png)

Procedemos a ver que si se actualiza el estado de una tarea, esta se marca de manera automática.

![](./images/e1-3.png)

### 2. Uso avanzado de etiquetas (labels) para priorización y estado



###  3. Automatización de Kanban board con GitHub Actions

### 4. Seguimiento de tiempo y esfuerzo usando GitHub Projects

### 5. Refinamiento de backlog basado en comentarios de los stakeholders

### 6. Análisis del flujo de trabajo usando el Kanban board
