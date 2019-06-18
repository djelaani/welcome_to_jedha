## Réduction de dimensions


### ACP AFD


[TOC]



## Ce que vous apprendrez dans ce cours

Ce cours a pour but d’introduire des techniques de réduction de dimensions, qui sont aussi bien utilisées pour faire des analyses et comprendre des jeux de données, mais aussi pour préparer le terrain avant d’appliquer un modèle d’apprentissage. Nous nous intéresserons dans un premier temps à deux techniques que sont l’analyse en composantes principales et l’analyse factorielle discriminante. La première s’intéresse uniquement à des variables quantitatives et l’autre au relation entre une variable qualitative et des variables quantitatives.


## Réduction de dimensions

On a souvent le sentiment en data science que plus on a de variables explicatives à notre disposition, meilleur sera le modèle que l’on pourra en tirer. Cela n’est que partiellement vrai, le but d’un data scientist n’est pas toujours de créer un modèle qui soit un excellent prédicteur de la réalité peu importe sa complexité, tous les problèmes ne s’apparentent pas à la classification d’images. Souvent il s’agit d’extraire de l’information pertinente, compréhensible par des non spécialistes, comme en sociologie, en économie et bien d’autres domaines encore. Comme toujour en data science, l’important est de produire des résultats qui soient utiles dans un contexte donné. D’autres fois, on se heurte à des contraintes techniques, car le matériel à notre disposition n’est pas très performant, ou parce qu’on souhaite comprendre mieux des données avec lesquelles on est pas très familier.

De fait, il est essentiel d’aborder des techniques qui permettent de résumer l’information de manière pertinente et simple. On peut ranger ces différentes techniques sous le nom de réduction de dimensions, on démarre avec un grand nombre de variables qui forment un espace de grande dimension et on souhaite se ramener à un espace plus petit.


### Analyse en composantes principales (ACP)



1. Intuition

En pratique il est très difficile de produire des visualisations simples de jeux de données contenant de nombreuses variables explicatives (à partir de quatres variables explicatives il est impossible de représenter simplement les données comme un nuage de point, puisque notre monde est en trois dimensions, et nos écrans d’ordinateur en seulement deux dimensions). Le principe général de l’ACP est d’utiliser les variables à notre disposition et de les combiner linéairement entres elles afin de créer un espace de dimension plus petite qui représente le mieux possible l’ensemble de l’information.

Graphiquement, si on a *p* variables, on cherche un espace vectoriel de dimension <img src="https://latex.codecogs.com/svg.latex?\Large&space;p'<p" /> sur lequel on puisse projeter chaque observation en modifiant le moins possible l’allure du nuage de points de dimension *p* originel. Pour donner une intuition visuelle de ce que représente mathématiquement l’analyse en composantes principales on prend un exemple jouet en deux dimensions qu’on souhaite réduire à une seule dimension. On dispose d’un nuage de point en deux dimensions et on trouve la droite de projection qui permette le mieux de représenter les données en une seule dimension. On en profite pour remarquer que cette droite de projection correspond à la direction suivant laquelle la variance est la plus grande.


![intro_ACP](https://drive.google.com/uc?export=view&id=1NydGu6Lc4mupX-RuPjoT7lpyjFYQNoJo)



2. Remarque importante

L’ACP est une méthode de réduction de dimensions qui s’applique uniquement aux cas où on s’intéresse uniquement à des variables quantitatives.



3. Décomposition de la matrice des covariances
    1. Matrice des covariances

La matrice des covariances, ou matrice des variances-covariances de la famille de variables

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> est une matrice carré de taille *px* où *p* est le nombre de variables auxquelles on s’intéresse et dont éléments sont :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;a_{ii}=Var(X_i)" />
<img src="https://latex.codecogs.com/svg.latex?\Large&space;a_{ii}=Cov(X_i,X_j),\;i\neq{j}" />


    2. Décomposition

La matrice des variances-covariances est donc une matrice symétrique par rapport à sa diagonale que l’on va devoir analyser afin de représenter nos données dans un espace de faible dimension. Comme l’intuition nous le suggérait plus tôt, le but de l’analyse en composantes principales est de trouver les directions selon lesquelles la variance des données est la plus grande possible, ce qui mathématiquement correspond à trouver les vecteurs propres de la matrice des variances-covariances.

Les vecteurs propres de la matrice des variances-covariances sont des combinaisons linéaires des variables <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> que l’on note <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1^{'},X_2^{'},...,X_p^{'}" />, ils ont pour propriétés d’être perpendiculaires entre eux et la valeur propre associée à chacun d’entre eux correspond à la quantité de variance existant dans cette direction (En d’autre termes, c’est la variance qu’on obtient si l’on calcule la variance de la population une fois projetée sur un des vecteurs propres). Les vecteurs propres construits lors de la décomposition de la matrice des variances-covariances sont aussi appelés facteurs. En utilisant les facteurs comme nouvelles collection de variables explicatives, on peut représenter la matrice des variances-covariances initiales sous la forme d’une matrice diagonale (c’est à dire que tous ses éléments valent zéro, à l’exception des éléments se trouvant sur la diagonale) dont les éléments sur la diagonale sont respectivement égaux aux valeurs propres de la matrice des variance-covariances initiale.

On remarque que la somme des valeurs propres de cette matrice est égale à la somme des variances respectives des variables initiales, c’est à dire la variance totale de la population. Le passage des variables initiales aux facteurs n’a donc pas entraîné de perte d’information.



4. Analyse en composantes principales
    3. Intérêt

La construction des facteurs permet de représenter les données par de nouvelles variables, mais quel est le véritable intérêt de ces variables? Eh bien il s’avère qu’en général, quelques facteurs associés aux plus grandes valeurs propres de la matrice des variances-covariances suffisent à expliquer une très grande portion de la variance totale de la population, ce qui permet de résumer l’information de manière condensée sans s’éloigner trop de la réalité observée.


    4. Interprétation des facteurs

Comme on l’a dit, les facteurs sont des combinaisons linéaires des variables initiales, en fonction de leur composition, on peut en déduire leur sens.


### Analyse factorielle discriminante


1. Intuition

Cette méthode s’applique aux cas où l’on s’intéresse à un ensemble de variables quantitatives et UNE variable qualitative. On dispose de *p* variables quantitatives <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> qui jouent le rôle de variables explicatives et une variable qualitative *Q* qui possède *m* modalités <img src="https://latex.codecogs.com/svg.latex?\Large&space;Q_1,Q_2,...,Q_m" /> qui joue le rôle de variable cible. L’intuition derrière cette méthode réduction de dimension est similaire à une régression linéaire multiple, mais étant donné que la variable cible est qualitative, la méthode va être assez différente. On va en fait chercher parmis les ACP possibles sur les variables <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> celle dont la représentation graphiques des individus sépare le mieux les différentes modalités de la variable qualitative *Q*.



2. Analyse factorielle discriminante
    1. Matrice des variances-covariances totale

La matrice des variances-covariances totale est simplement la matrice des variances covariances des variables <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> sans tenir compte des modalités de la variable qualitative *Q*. On notera cette matrice *V*.



<img src="https://latex.codecogs.com/svg.latex?\Large&space;V=\frac{1}{n}\sum_{i=1}{n}(x_i-\mu)^T(x_i-\mu)" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> est le vecteur représentant l’individu *i* et <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu" /> est le vecteur qui représente le centre de gravité de l’ensemble des observations.


    2. Matrice des variances-covariances inter-groupes

La matrice des variances-covariances inter-groupes représente l’éloignement entre les groupes définis par les modalités de la variable qualitative *Q*. Cette matrice est définie par l’équation suivante :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;B=\frac{1}{n}\sum_{k=1}^{m}n_k(\mu_k-\mu)^T(\mu_k-\mu)" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;n_k" /> est le nombre d’observations qui prennent la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Q_k\;\mu" /> est le centre de gravité de l’ensemble des observations, <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu_k" /> est le centre de gravité des observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Q_k" />.



    3. Trouver les facteurs

Les facteurs qui permettent de résumer l’information le mieux possible tout en séparant au plus les différentes modalités de la variable qualitative *Q* sont les vecteurs propres de la matrice suivantes:


<img src="https://latex.codecogs.com/svg.latex?\Large&space;V^{-1}B" />


On voit ici le lien avec l’ACP dans le fait de devoir trouver les valeurs et les vecteurs propres d’une matrice qui représente la dispersion des observations. Cependant, contrairement à une ACP classique, l’AFD travaille sur une matrice qui représente à la fois la dispersion totale et aussi l’éloignement des différentes modalités de la variable qualitative les unes par rapport aux autres.



![ACP_iris](https://drive.google.com/uc?export=view&id=1A4-Vvbzo9wxuTn4FNROzi457Vxo4YJw-)


On montre ici un exemple de la représentation d’observations représentant différentes espèces d’iris dans le plan défini par les facteurs.
