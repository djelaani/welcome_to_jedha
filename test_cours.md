

## Machine learning supervisé


### Support vector machines


[TOC]



## Ce que vous apprendrez dans ce cours

Ce cours est dédié à l’exploration d’une famille de modèle appelés machines à vecteurs de support (ou support vector machines SVM en anglais). Ces modèles ont été d’abord construit dans le but de faire de la classification et permettent de séparer l’espace contenant les données en deux parties dans le but que les deux zones de l’espaces séparent les points en fonction de leur classe.


## Introduction

L’idée derrière les support vector machines est de séparer des points appartenant à différentes classes en trouvant un hyperplan (un sous-espace de dimension d-1 ou d est la dimension de l’espace contenant les données) le plus distant possible de tous les points à classer. De sorte qu’il existe une zone ou marge entre les deux classes qui ne contient aucun point la plus grande possible, comme illustré dans la figure ci-dessous :


![intr_svm](https://drive.google.com/uc?export=view&id=1_HvXcNAQp0TSWncMStK19qQ22wi7-eX3)

Notons que la ligne rouge dans la figure de droite est un hyperplan de l’espace des observations en deux dimensions (c’est à dire une droite), mais que la ligne rouge dans la figure de gauche n’est pas un hyperplan de l’espace des observations, nous verrons par la suite que les support vector machines sont capables de séparer les données de manière non linéaire grâce à une astuce appelée estimateurs à noyaux.



1. Que sont les support vector machines ?

C’est un modèle de machine learning supervisé qui est utilisé en premier lieu pour la classification de données. Dans l’algorithme des SVM on représente les observations comme un nuage de point dans un espace de dimension ***d*** où ***d*** est le nombre de variables explicatives que nous utilisons pour la modélisation. Les coordonnées des observations dans cet espace sont les valeurs prises par chaque variable explicative pour ces observations. A partir de là, on réalise une classification en trouvant un hyperplan qui différencie les deux classes.



    1. Hyperplan
        1. Espace vectoriel

Un espace vectoriel construit sur l’ensemble des nombres réels <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}" /> est un ensemble ***E*** dont les éléments sont appelés vecteurs muni de deux lois :



*   Une loi de composition interne (c’est l’addition pour faire simple) “+” qu’on appelle somme vectorielle. Pour tout couple d’élément de ***E***, la somme de ces éléments appartient encore à ***E***. <img src="https://latex.codecogs.com/svg.latex?\Large&space;\farall{x,x'}\in{E},x+x'\in{E}" />.
*   Une loi de composition externe (la multiplication par un scalaire), on peut multiplier les élements de ***E*** par n’importe quel nombre réel et l’élément obtenu sera toujours dans ***E***. <img src="https://latex.codecogs.com/svg.latex?\Large&space;\farall{a}\in\mathbb{R},\farall{x}\in{E},ax\in{E}" />.

Les seuls exemples d’espaces vectoriels que nous verrons dans ce cours sont des espaces vectoriels basés sur <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}" />
. Par exemple <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}^2" /> qui est l’espace des vecteurs à deux dimensions à composantes réelles, des vecteurs de cet espace sont par exemple : ***[2.5,5.77]*** ou ***[0,3.6]***. Plus généralement les espaces vectoriels auxquels nous avons affaire sont de la forme <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}^d" /> composés de vecteurs à ***d*** composantes réelles, comme les datasets comprenant ***d*** variables explicatives.



        2. Hyperplan

Les hyperplans sont des sous-espaces vectoriels de dimension ***d - 1***, où ***d*** est la dimension de l’espace vectoriel original. Le nom vient du fait que dans <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}^3" />
 l’espace vectoriel réel en trois dimensions, les hyperplans sont des plans vectoriels (de dimension 2 donc).

Un hyperplan de <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}^d" /> est un espace vectoriel ***H*** compris dans <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}^d" />, c’est à dire que tous les éléments de ***H*** sont dans <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}^d,\farall{h}\in{H},h\in\mathbb{R}^d" />, et ***H*** est de dimension ***d - 1***.

Une notion qui peut vous aider à comprendre les hyperplans et que pour définir un hyperplan, on peut penser à sa droite supplémentaire. La droite supplémentaire est comme son nom l’indique une droite ***D*** (de dimension un donc), elle possède un vecteur directeur <img src="https://latex.codecogs.com/svg.latex?\Large&space;\overrightarrow{v}" /> qui donne sa direction dans <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}^d" />. L’hyperplan de droite supplémentaire ***D*** engendrée par le vecteur <img src="https://latex.codecogs.com/svg.latex?\Large&space;\overrightarrow{v}" /> est l’ensemble des vecteurs <img src="https://latex.codecogs.com/svg.latex?\Large&space;\overrightarrow{x}" /> de <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{R}^d" /> tels que le produit scalaire de <img src="https://latex.codecogs.com/svg.latex?\Large&space;\overrightarrow{x}" /> et <img src="https://latex.codecogs.com/svg.latex?\Large&space;\overrightarrow{v}" /> est nul.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;E=\{\overrightarrow{x}\in{\mathbb{R}^d},\overrightarrow{x}\cdot\overrightarrow{v}=0\}" />, cette notion de droite supplémentaire et vecteur générateur sont importants pour comprendre le fonctionnement des support vector machines.



    2. Support vector machine représentation graphique

Pour récapituler, les SVM sont une manière de séparer les données de deux classes distinctes par un hyperplan de l’espace des observations, c’est donc un classificateur linéaire qui sépare deux groupes d’observation. Qu’est ce qui différentie les SVM des autres classificateurs linéaires comme par exemple les deux exemples montrés ci dessous ?


![svm2](https://drive.google.com/uc?export=view&id=1tC7kyx0Cuku9v1vDHndgwo3BcYjINwCE)


A votre avis, laquelle de ces deux droites sépare le mieux les données ? Si vous pensez que c’est la ligne jaune, vous avez raison, car c’est la droite (hyperplan) que construit l’algorithme SVM, rentrons plus dans les détails pour expliquer pourquoi.

La ligne verte dans l’exemple est très proche de la classe des observations en rouge, certes elle sépare les données de manière convenable, cependant si on continue à observer de nouveaux membres des classes bleue et rouge, on risque fort de trouver des points rouges qui se trouveront du mauvais côté de la ligne verte. Cela revient à dire que le modèle de classification défini par la ligne verte risque de mal se généraliser pour la classification de nouvelles observations, hors en machine learning supervisé, l’objectif principal et de définir un modèle qui permette d’obtenir de bonnes performances sur de nouvelles observations.

Pourquoi alors, la ligne jaune est elle plus adaptée à nos exigences ? Nous en venons à la notion de support vectors, les support vectors sont les observations qui sont le plus proches de la ligne de séparation, on calcule la distance entre les support vectors et la ligne de séparation, cette distance est appelée la marge. Le but des support vector machines est de maximiser la marge, comme on le montre dans l’exemple ci dessous :



![svm3](https://drive.google.com/uc?export=view&id=1QLcdwSQ8V1lxhfRpbxg6oaaanbgOPyD4)


Cet hyperplan de séparation est optimal en terme de généralisation car c’est l’hyperplan qui est à la fois le plus éloigné de la classe rouge et de la classe, si les deux classes sont réellement limitées dans ces zones de l’espace, alors le risque qu’une observation rouge ou bleue se retrouve du mauvais côté de la ligne est plus faible, au moins aussi faible que possible.

Cet exemple constitue un exemple très simple dans lequel les données sont linéairement séparables, c’est à dire qu’on peut tracer un hyperplan qui sépare parfaitement les données, ce n’est pas toujours le cas en pratique.



2. SVM non linéaire
    3. Augmentation de dimension

Pour produire des classificateurs non linéaire à partir d’un modèle linéaire on ne pas travailler sur les données telles quelles afin de produire les estimations, on doit transformer les données grâce à une fonction appelée noyau (kernel en anglais). Cette fonction a pour but d’emmener les observations dans un espace de dimension plus grande où on espère que les propriétés géométriques des observations seront plus sympathiques pour nos estimations.

Par exemple si on observe un groupe de vaches est qu’on dispose de leur poids et taille au garrot, on peut produire une nouvelle dimension grâce par exemple à un noyau polynomial : <img src="https://latex.codecogs.com/svg.latex?\Large&space;k(\overrightarrow{poids},\overrightarrow{taille})=(\overrightarrow{poids},\overrightarrow{taille})^p" /> où ***k*** est la fonction noyau polynomial, et ***p ≥ 2*** est l’ordre du polynôme choisi. Cette nouvelle dimension n’est pas une combinaison linéaire des variables explicatives et augmente donc la dimension de l’espace des observation de deux à trois. On peut calculer un séparateur linéaire comme un SVM dans ce nouvel espace, et lorsqu’on aura l’équation de l’hyperplan séparateur dans cet espace, on pourra aussi le représenter dans l’espace original, mais il ne sera pas représenté par une droite mais par un séparateur non linéaire comme dans la figure ci dessous :


![](https://drive.google.com/uc?export=view&id=1_HvXcNAQp0TSWncMStK19qQ22wi7-eX3)


    4. SVM non linéaire

Si on considère l’exemple ci-dessous, il n’est pas possible de séparer les données ainsi présentées par un hyperplan (ici une droite) :


![svm4](https://drive.google.com/uc?export=view&id=1xWz8mJS9YQh1hG6dJAlhul-klPAZZIjN)


Cependant ce problème peut être transformé en un problème linéairement séparable dans un espace de plus grande dimension. Si on ajoute une troisième dimension <img src="https://latex.codecogs.com/svg.latex?\Large&space;z=x^2+y^2" /> qui représente la distance d’un point à l’origine du repère orthonormé, si on visualise les données sur les axes ***x*** et ***z*** on obtient la figure suivante :


![svm5](https://drive.google.com/uc?export=view&id=1qAHLPe_CxlJr7AsGu6xdOk5UohJtSg-x)


Dans cet espace, il est très simple de séparer les données par un hyperplan d’équation ***z = k*** par exemple. Lorsqu’on représente cet hyperplan dans l’espace original, on obtient un séparateur non linéaire :



![svm6](https://drive.google.com/uc?export=view&id=1YLQm6N4rHigrUphQOTudHrHB4vejXopX)


Cet exemple donne l’impression que l’utilisation des noyaux est très simple, en pratique pourtant, il est assez difficile de trouver le noyau adapté afin de pouvoir séparer simplement les données par un classificateur linéaire. Cela dit, il existe toujours un nombre de dimensions à ajouter qui permet de rendre le problème linéairement séparable, cependant, plus on ajoute de dimensions à l’espace original, plus on risque de faire du sur-apprentissage et d’obtenir un modèle SVM instable, c’est à dire qui n’aura pas une bonne capacité de généralisation.



    5. SVM en python

Afin d’importer, définir et estimer les paramètres du modèle SVM en python, il suffit d’utiliser les trois commandes ci dessous, évidemment les noms des objets “clf” , “X” et “y” sont arbitraire et peuvent être choisis à votre guise en fonction du reste du code.


```
from sklearn.svm import SVC
clf = SVC(kernel='linear')
clf = SVC.fit(X, y)
```
