
##
    Apprentissage non supervisé


###
    Classification Ascendante Hiérarchique


[TOC]



## Ce que vous apprendrez dans ce cours

Ce cours introduit l’algorithme de classification ascendante hiérarchique. Comme son nom l’indique cette méthode commence par faire l’hypothèse que chaque observation appartient à une classe différente et va ensuite rapprocher une à une chaque observation en fonction de leur proximité pour finalement arriver au point final où toutes les observations sont rangées dans une seule et même classe. Cette méthode construit ainsi une hiérarchie sous la forme d’un genre d’arbre généalogique qui donne les liens de filiation des différentes classes.


## Classification ascendante hiérarchique

La classification ascendante hiérarchique est une autre technique d’apprentissage non supervisé qui permet de classer une population de *n* observations dans un certain nombre de classes. L’algorithme repose sur une mesure de _dissimilarité_ entre les observations, autrement dit une distance. Elle est dite ascendante car le point de départ de cette méthode est une configuration dans laquelle chaque observation appartient à une classe qui lui est propre, on a donc autant de classes que d’observations dans la population. Elle est dite hiérarchique car elle se comporte à la manière d’un arbre avec des branches, cela signifie qu’au sommet de la hiérarchie, toutes les observations appartiennent à la même classe, en bas de la classification, on a autant de classes que d’observations, et pour toutes les classes intermédiaires deux classes intermédiaires n’ont soit aucune observation commune, soit l’une est incluse dans l’autre. Si l’on note la population <img src="https://latex.codecogs.com/svg.latex?\Large&space;\Omega=\{\omega_1,...,\omega_n\}" /> et l’ensemble des classes de la hiérarchie *H* on peut écrire mathématiquement ces propriétés de la manière suivante :



*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;\Omega\in\;H" />, l’ensemble contenant toute la population appartient à la hiérarchie
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;\farall{\omega}\in\Omega,\;\{\omega\}\in\;H" />, tous les ensembles contenant une seule observation appartiennent à la hiérarchie
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;\farall{h,h'}\in\;H,h\cap\;h'=\emptyset\;ou\;h\subset{h'}\;ou\;h\supset{h'}" />, les classes de la hiérarchie sont soit distinctes soit incluses l’une dans l’autre.

Ces propriétés peuvent se comprendre facilement à l’aide d’une visualisation de l’arbre des classes, aussi appelé _dendrogramme._



![alt_text](images/Apprentissage-non0.png "image_tooltip")


Dans la figure ci-dessus, les observations sont représentées sur l’axe des abscisses, on parlera plus tard de l’axe des ordonnées, chaque branche représente une classe. On voit bien qu’en bas du dendrogramme on observe une branche pour chaque observation, et en remontant les branches fusionnent pour ne former plus qu’une branche/classe contenant toutes les observations se trouvant au bout de ces dernières.



1. Algorithme de formation de la classification ascendante hiérarchique.
    1. Principe général

Lors de l’étape initiale, chaque observation appartient à une classe qui lui est propre. A chaque étape à partir de là on fusionne ensemble les deux classes qui sont les plus “proches” au sens de la distance qu’on a choisi d’utiliser pour l’algorithme. La valeur de la dissimilarité ou distance minimale entre deux classes est appelé _indice d’agrégation._ Souvent les premiers indices d’agrégation sont faibles car les premières classes sont très proches, mais cet indice va croître au fur et à mesure des étapes de l’algorithme.



    2. Mesure de dissimilarité

La dissimilarité entre deux classes qu’on notera *d(h,h')* est l’élément essentiel de l’algorithme, c’est elle qui va déterminer de quelle manière les classes vont être formées. Lorsque les classes ne contiennent qu’un seul individu, la dissimilarité entre ces classes est égale à la dissimilarité entre les éléments qu’elles contiennent.



<img src="https://latex.codecogs.com/svg.latex?\Large&space;h=\{x\},h'=\{x'\},d(h,h')=d(x,x')" />


Lorsque les classes contiennent plusieurs éléments, il existe différentes manière de calculer leur dissimilarité que nous allons exposer maintenant.



*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,h')=\min_{x\in{h},x'\in{h'}}d(x,x')" />, la dissimilarité entre deux classes peut être égale à la dissimilarité minimum entre deux individus pris dans chaque classe.

*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,h')=\max_{x\in{h},x'\in{h'}}d(x,x')" />, la dissimilarité entre deux classes peut être égale à la dissimilarité maximale entre deux observations prises dans chacune des classes.
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,h')=\frac{1}{Card(h)\cdot{Card(h')}}\sum_{x\in{h}}\sum_{x\in{h'}}d(x,x')" />
, la dissimilarité entre deux classes peut être calculée comme la moyenne des dissimilarités entre chaque couples d’observations pris dans chaque classe.

*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,h')=\frac{Card(h)\cdot{Card(h')}}{Card(h)+Card(h')}d(G,G')" />
, où sont les centres de gravité de *h, h'* respectivement. Cette mesure de dissimilarité est appelée la distance de Ward.

Dans tous les exemples de mesure de dissimilarité ci-dessus intervient l’objet mathématique *d* qui est une distance définie pour mesurer la distance entre deux observations et qui doit donc être choisie par le data scientist. On choisit souvent par défaut la distance euclidienne que nous avons vu précédemment, à condition d’avoir traité les données en amont afin qu’elles soient quantitatives et normalisées, pour éviter qu’une variables dont les valeurs sont plus grandes ne capture tout le pouvoir discriminant pour elle.
