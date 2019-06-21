
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
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;\forall{omega}\in\Omega,\;\{\omega\}\in\;H" />, tous les ensembles contenant une seule observation appartiennent à la hiérarchie
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;\forall{h,h'}\in\;H,h\cap\;h'=\emptyset\;ou\;h\subset{h'}\;ou\;\supset{h'}" />, les classes de la hiérarchie sont soit distinctes soit incluses l’une dans l’autre.

Ces propriétés peuvent se comprendre facilement à l’aide d’une visualisation de l’arbre des classes, aussi appelé _dendrogramme._
