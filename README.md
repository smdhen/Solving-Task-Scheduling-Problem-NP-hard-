# <center>Solving Task Scheduling Problem (NP hard)<center>

## Table of contents
- [Project Overview (Definitions)](#project-overview--definitions-)
- [Objectif 1 ](#objectif-1)
- [Objectif 2](#objectif-2)
- [la modélisation mathématique de 1er objectif](#la-modélisation-mathématique-de-1er-objectif)
- [la modélisation mathématique de 2 eme objectif](#la-modélisation-mathématique-de-2-eme-objectif)
- [Références](#références)



## Project Overview (Definitions)
Les problèmes d'ordonnancement font partie de notre vie quotidienne !
Ces problèmes concernent bien évidemment aussi de nombreuses activités
des entreprises dans le monde industriel.
Ordonnancer un ensemble de tâches c'est de planifier leur exécution en
leur affectant la ou les ressource /ressources nécessaire et en
déterminant la date de début pour chaque tache.
Dans un problème d’ordonnancement deux notions principales
s’intervient :
1. La notion de la tâche : C’est un travail élémentaire dont la réalisation
nésite un certain nombre de unités de temps.
Chaque tache peut se caractérisée par :

  - Sa durée

  - La date à laquelle elle doit être achevée
  
  - Le cas échéant les contraintes entre les dates de début de ces tâches
  
2. Notions de la ressource : c’est le moyen par laquelle en réalise les
tâches par exemple les processeurs, la mémoire…,

### Objectif 1

Dans ce cas, on considère n tâches à exécuter sur une seule ressource afin de
minimiser l’objectif 1 : 1|| ∑Ui. (Somme des retards)

Les tâches sont toutes disponibles à l’instant 0 avec chacune une durée
opératoire pi et une date de livraison di. Noter qu’après le démarrage de la
première tâche aucun temps mort n’est autorisé sur la ressource (i.e. chaque
solution réalisable doit commencer à t=0 et se terminer à t=∑pi).

### Objectif 2

Dans ce cas, on considère n tâches à exécuter sur une seule ressource afin de
minimiser l’objectif 2 : 1|| ∑αiEi+ βiTi

Les tâches sont toutes disponibles à l’instant 0 avec chacune une durée
opératoire pi et une date de livraison di. Noter qu’après le démarrage de la
première tâche aucun temps mort n’est autorisé sur la ressource.

### la modélisation mathématique de 1er objectif

Dans ce premier objectif on s’intéresse à minimiser le nombre de tache en
retard.
Minimiser : ∑Ui
Avec :
𝑈𝑖 = 0 , 𝑠𝑖 𝑙𝑎 𝑡𝑎𝑐ℎ𝑒 𝑖 𝑛′ 𝑒𝑠𝑡 𝑝𝑎𝑠 𝑒𝑛 𝑟𝑒𝑡𝑎𝑟𝑑
𝑈𝑖 = 1 , 𝑠𝑖 𝑙𝑎 𝑡𝑐ℎ𝑒 𝑒𝑠𝑡 𝑒𝑛 𝑟𝑒𝑡𝑎𝑟𝑑
Soit : Cj=∑Pj



la somme des dures des taches déjà exécutée.

𝑈𝑖 = 0  𝑠𝑖 𝐶𝑗 > 𝑑𝑗
𝑈𝑖  = 1 𝑠𝑖 𝐶𝑗 < 𝑑𝑗


Relation de récurrence : pour traite ce problème d’ordonnancement en va
le simplifier par supposé que on a exécuter toutes les tache sauf une seule
tâche qui sera le dernier

soit N l’ensemble des taches N= {1,2,3,4, 5 ,….,i}

La fonction peut être donnée par : 𝑓(𝑁) = 𝑚𝑖𝑛(𝑓(𝑁/𝑗) + 𝑈𝑗)


( 𝑗 ∈ 𝑁)(N/j) : L’ensembles des taches supposées déjà exécutée sauf la tâche j.
Condition initiale :

∀ j ∈ N on a f(j)=min (f (∅) +Uj) = Uj. (j une seul tache)

f (∅) : condition d’arrêt on a aucune tache à exécuter encoure

Pour ’implémentation on a commencé à calculer f pour une seul tache puis 2
… n tache (forward programming)


### la modélisation mathématique de 2 eme objectif

Dans ce deuxième objectif on s’intéresse à minimiser des pénalités d'avances
et de retards sur une machine (weighted earliness-tardiness).la différence
entre ce problème et le premier c’est la présence des couts d’avance et de
retard sur chaque tache.

Minimiser : ∑αiEi+βiTi

Soit Ci=∑Pi

-Ei : l’avancement de la tache i tel que Ei =max (0. di -Ci)

-Ti : le retard de la tache i tel que, Ti =max (0. Ci- di)

Relation de récurrence : encoure dans ce problème on va suit la même
logique que le premier problème on va supposer que on a exécuter N/j tache
(toutes les taches sauf la tache j est) on a :

soit N l’ensemble des taches N = {1,2,3,4, 5, …, i}

𝑓 (𝑁) = 𝑚𝑖𝑛(𝑓(𝑁/𝑗) + αjEi + βjTj) ( 𝑗 ∈ 𝑁)

(N/j) : L’ensembles des taches supposées déjà exécutée sauf la tâche j.

Condition initiale : ∀ j ∈ N on a f(j)=min(f(∅) + αjEj + βjTj) = αjEj+βjTj.

f(∅) : condition d’arrêt on a aucune tache à exécuter

### Références 

- [1] PIERRE HANSEN and NENAD MLADENOVIC, Chapter 8 “Variable
neighborhood search”.

- [2] RAIRO. Recherche opérationnelle, tome 27, no 1 (1993), p. 77-150.
  
- [3] JOSEPH CHERIYANA and R. RAVIB and Martin SKUTELLAC “A simple
proof of the Moore-Hodgson Algorithm for minimizing the number of late jobs”.

- [4] PENG GUO and WENMING Cheng “a general variable neighborhood search for
single-machine total tardiness scheduling problems with step-deteriorating jobs”.
