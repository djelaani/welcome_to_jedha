
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
, où *G,G'* sont les centres de gravité de *h, h'* respectivement. Cette mesure de dissimilarité est appelée la distance de Ward.

Dans tous les exemples de mesure de dissimilarité ci-dessus intervient l’objet mathématique *d* qui est une distance définie pour mesurer la distance entre deux observations et qui doit donc être choisie par le data scientist. On choisit souvent par défaut la distance euclidienne que nous avons vu précédemment, à condition d’avoir traité les données en amont afin qu’elles soient quantitatives et normalisées, pour éviter qu’une variables dont les valeurs sont plus grandes ne capture tout le pouvoir discriminant pour elle.



    3. Algorithme

L’algorithme de la classification ascendante hiérarchique peut se décrire de manière simple en utilisant du pseudo-code :



*   **Initialisation :**

<img src="https://latex.codecogs.com/svg.latex?\Large&space;H_0=\{\{x_1\},...\{x_n\}}" />, la hiérarchie contient toutes les classes à une seule observation.


*   **Tant que** <img src="https://latex.codecogs.com/svg.latex?\Large&space;\Omega\;\notin\;H_1" />**:** <img src="https://latex.codecogs.com/svg.latex?\Large&space;i=0\;\\i=i+1" />



Pour tout <img src="https://latex.codecogs.com/svg.latex?\Large&space;h,h'\in\;H_{i-1},h\neq{h'}" />, calculer <img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,h')" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;H_i=H_{i-1}-\{h_{min}\}-\{h_{min}}\}^'+\{h_{min},h_{min}^'\}" />, on retire de la hiérarchie précédente les deux classes les plus proches et on ajoute la fusion des deux classes les plus proches qui vérifient

<img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h_{min},h_{min}^')=\min_{h,h'\in{H_{i-1}},h\neq{h'}}d(h,h')" />


*   **Résultat :** <img src="https://latex.codecogs.com/svg.latex?\Large&space;\{H_0,H_1,...,H_1,\Omega\}" />. On obtient la hiérarchie complète.

Et ainsi on obtient le dendrogramme que nous avons pu observé précédemment.



![alt_text](images/Apprentissage-non1.png "image_tooltip")


On peut maintenant parler de l’axe des ordonnées que nous n’avions jusqu’alors pas commenté, il correspond à l’indices d’agrégation que nous calculons à chaque étape de l’algorithme, lorsque deux classes *h,h'* sont rassemblées en une, on forme un noeud dans le dendrogramme, la hauteur de ce noeud correspond à la valeur de *d(h,h')*.



2. Comment déterminer la partition la plus pertinente.

Dans l’algorithme de classification ascendante hiérarchique que nous avons vu, les classes sont formées par agrégation de classes plus petites jusqu’à se retrouver avec une seule classe contenant toute la population. La hiérarchie obtenue permet de définir un grand nombre de partition des données possible, imaginez-vous que nous coupons l’arbre selon un axe vertical à une certaine hauteur, les classes que nous retiendrons seront les classes les plus basses parmi les classes se trouvant au-dessus de l’axe de coupe.



![drawing](https://docs.google.com/a/google.com/drawings/d/12345/export/png)

Si on adopte cette coupe, on obtient en définitive les 5 classes suivantes :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;h_1=\{2,10\},h_2=\{5,8,9\},h_3=\{1,4\},h_4=\{3\},h_5=\{6,7\}" />


Il n’existe pas de technique qui fasse l’unanimité en termes de partition à retenir, cependant il existe des règles qui permettent de guider de votre choix afin de retenir la partition des données qui réponde le mieux à vos besoin ou à vos attentes.



*   Privilégier les troncatures de l’arbre au niveau de branches longues/hautes, plus la hauteur en ordonnée mesurée entre deux branches consécutives du dendrogramme, plus les classes ainsi formées seront éloignées les unes des autres. Si on coupe entre deux noeuds qui sont très proches au niveau du axes des ordonnées, cela signifie qu’on forme deux classes très proches quand on pourrait les rassembler pour n’en former qu’une qui resterait malgré tout assez cohérente. Une règle facile à mettre en application est de regarder la hauteur entre chaque noeuds consécutifs et de couper là où la différence entre deux hauteurs calculées est la plus grande. C’est ce qu’on a fait dans l’exemple au-dessus.
*   Si votre objectif n’est pas nécessairement d’obtenir les classes les plus grosses et les plus disparates possibles, mais qu’au contraire vous souhaitez également obtenir des classes dont les effectifs sont comparables, vous pourrez couper, si l’arbre s’y prête, au niveau qui vous donnera les classes les plus équilibrées. Attention, car il arrive souvent que les observations ne puissent pas naturellement être partitionnée de manière équilibrée.
*   Un critère populaire existe qui porte le nom de _critère de Ward _, qui repose sur une nouvelle mesure appelée _l’inertie._

    L’inertie d’une classe est définie de la manière suivante :




***Inertie totale:*** <img src="https://latex.codecogs.com/svg.latex?\Large&space;I_t=\frac{1}{n}\sum_{i=1}^{n}d(x_i,g)^2" />



***Inertie interclasse:*** <img src="https://latex.codecogs.com/svg.latex?\Large&space;I_e=\frac{1}{n}\sum_{i=1}^{k}n_i\cdot{d(g_i,g)^2}" />



***Inertie intraclasse:*** <img src="https://latex.codecogs.com/svg.latex?\Large&space;I_a=\frac{1}{n}\sum_{i=1}^{k}\sum_{j=1}^{n_i}d(x_i,g_i)^2}" />



Où *n*  est le nombre d’observations, <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_1,...,x_n" /> est l’ensemble des observations, *d* est la distance choisie pour l’algorithme, *g* est le centre de gravité de la population, et <img src="https://latex.codecogs.com/svg.latex?\Large&space;g_1,...,g_k" /> sont les centres gravité respectifs des *k* classes formées par la classification ascendante hiérarchique avec une certaine coupure.


La méthode de Ward correspond à calculer l’inertie interclasse pour chaque niveau d’agrégation des données (c’est à dire à chaque étape de l’algorithme quand deux classes fusionnent) et retiendra comme dernière étape d’agrégation l’étape qui correspond à l’augmentation maximale de l’inertie interclasse.
