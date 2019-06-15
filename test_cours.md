## Semaine 5 - Réduction de dimension et Séries temporelles


## Réduction de dimensions

On a souvent le sentiment en data science que plus on a de variables explicatives à notre disposition, meilleur sera le modèle que l’on pourra en tirer. Cela n’est que partiellement vrai, le but d’un data scientist n’est pas toujours de créer un modèle qui soit un excellent prédicteur de la réalité peu importe sa complexité, tous les problèmes ne s’apparentent pas à la classification d’images. Souvent il s’agit d’extraire de l’information pertinente, compréhensible par des non spécialistes, comme en sociologie, en économie et bien d’autres domaines encore. Comme toujour en data science, l’important est de produire des résultats qui soient utiles dans un contexte donné. D’autres fois, on se heurte à des contraintes techniques, car le matériel à notre disposition n’est pas très performant, ou parce qu’on souhaite comprendre mieux des données avec lesquelles on est pas très familier.

De fait, il est essentiel d’aborder des techniques qui permettent de résumer l’information de manière pertinente et simple. On peut ranger ces différentes techniques sous le nom de réduction de dimensions, on démarre avec un grand nombre de variables qui forment un espace de grande dimension et on souhaite se ramener à un espace plus petit.


### Analyse en composantes principales (ACP)



1. Intuition

En pratique il est très difficile de produire des visualisations simples de jeux de données contenant de nombreuses variables explicatives (à partir de quatres variables explicatives il est impossible de représenter simplement les données comme un nuage de point, puisque notre monde est en trois dimensions, et nos écrans d’ordinateur en seulement deux dimensions). Le principe général de l’ACP est d’utiliser les variables à notre disposition et de les combiner linéairement entres elles afin de créer un espace de dimension plus petite qui représente le mieux possible l’ensemble de l’information.

Graphiquement, si on a ***p*** variables, on cherche un espace vectoriel de dimension <img src="https://latex.codecogs.com/svg.latex?\Large&space;p'<p" /> sur lequel on puisse projeter chaque observation en modifiant le moins possible l’allure du nuage de points de dimension ***p*** originel. Pour donner une intuition visuelle de ce que représente mathématiquement l’analyse en composantes principales on prend un exemple jouet en deux dimensions qu’on souhaite réduire à une seule dimension. On dispose d’un nuage de point en deux dimensions et on trouve la droite de projection qui permette le mieux de représenter les données en une seule dimension. On en profite pour remarquer que cette droite de projection correspond à la direction suivant laquelle la variance est la plus grande.


![alt_text](images/Semaine-50.png "image_tooltip")



2. Remarque importante

L’ACP est une méthode de réduction de dimensions qui s’applique uniquement aux cas où on s’intéresse uniquement à des variables quantitatives.



3. Décomposition de la matrice des covariances
    1. Matrice des covariances

La matrice des covariances, ou matrice des variances-covariances de la famille de variables

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> est une matrice carré de taille <img src="https://latex.codecogs.com/svg.latex?\Large&space;pxp" /> où ***p*** est le nombre de variables auxquelles on s’intéresse et dont éléments sont :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;a_{ij}=Var(X_i)" />


<img src="https://latex.codecogs.com/svg.latex?\Large&space;a_{ij}=Cov(X_i,X_j),i\neq{j}" />


    2. Décomposition

La matrice des variances-covariances est donc une matrice symétrique par rapport à sa diagonale que l’on va devoir analyser afin de représenter nos données dans un espace de faible dimension. Comme l’intuition nous le suggérait plus tôt, le but de l’analyse en composantes principales est de trouver les directions selon lesquelles la variance des données est la plus grande possible, ce qui mathématiquement correspond à trouver les vecteurs propres de la matrice des variances-covariances.

**Inclure l’exemple pour montrer la transformation de la matrice**

Les vecteurs propres de la matrice des variances-covariances sont des combinaisons linéaires des variables <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> que l’on note <img src="https://latex.codecogs.com/svg.latex?\Large&space;{X'}_1,{X'}_2,...,{X'}_p" />, ils ont pour propriétés d’être perpendiculaires entre eux et la valeur propre associée à chacun d’entre eux correspond à la quantité de variance existant dans cette direction (En d’autre termes, c’est la variance qu’on obtient si l’on calcule la variance de la population une fois projetée sur un des vecteurs propres). Les vecteurs propres construits lors de la décomposition de la matrice des variances-covariances sont aussi appelés facteurs. En utilisant les facteurs comme nouvelles collection de variables explicatives, on peut représenter la matrice des variances-covariances initiales sous la forme d’une matrice diagonale (c’est à dire que tous ses éléments valent zéro, à l’exception des éléments se trouvant sur la diagonale) dont les éléments sur la diagonale sont respectivement égaux aux valeurs propres de la matrice des variance-covariances initiale.

**(inclure nouvelle matrice)**

On remarque que la somme des valeurs propres de cette matrice est égale à la somme des variances respectives des variables initiales, c’est à dire la variance totale de la population. Le passage des variables initiales aux facteurs n’a donc pas entraîné de perte d’information.



4. Analyse en composantes principales
    3. Intérêt

La construction des facteurs permet de représenter les données par de nouvelles variables, mais quel est le véritable intérêt de ces variables? Eh bien il s’avère qu’en général, quelques facteurs associés aux plus grandes valeurs propres de la matrice des variances-covariances suffisent à expliquer une très grande portion de la variance totale de la population, ce qui permet de résumer l’information de manière condensée sans s’éloigner trop de la réalité observée.

**Ajouter un exemple ou on voit ça**



    4. Interprétation des facteurs

Comme on l’a dit, les facteurs sont des combinaisons linéaires des variables initiales, en fonction de leur composition, on peut en déduire leur sens **exemple**




### Analyse factorielle discriminante



1. Intuition

Cette méthode s’applique aux cas où l’on s’intéresse à un ensemble de variables quantitatives et UNE variable qualitative. On dispose de ***p*** variables quantitatives <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> qui jouent le rôle de variables explicatives et une variable qualitative ***Q*** qui possède ***m*** modalités <img src="https://latex.codecogs.com/svg.latex?\Large&space;Q_1,Q_2,...,Q_m" /> qui joue le rôle de variable cible. L’intuition derrière cette méthode réduction de dimension est similaire à une régression linéaire multiple, mais étant donné que la variable cible est qualitative, la méthode va être assez différente. On va en fait chercher parmis les ACP possibles sur les variables <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> celle dont la représentation graphiques des individus sépare le mieux les différentes modalités de la variable qualitative ***Q***.



2. Analyse factorielle discriminante
    1. Matrice des variances-covariances totale

La matrice des variances-covariances totale est simplement la matrice des variances covariances des variables <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> sans tenir compte des modalités de la variable qualitative ***Q***. On notera cette matrice ***V***.



<img src="https://latex.codecogs.com/svg.latex?\Large&space;V=\frac{1}{n}\sum_{i=1}^n(x_i-\mu)^T\cdot(x_i-\mu)" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> est le vecteur représentant l’individu *i* et <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu" /> est le vecteur qui représente le centre de gravité de l’ensemble des observations.


    2. Matrice des variances-covariances inter-groupes

La matrice des variances-covariances inter-groupes représente l’éloignement entre les groupes définis par les modalités de la variable qualitative *Q*. Cette matrice est définie par l’équation suivante :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;B=\frac{1}{n}\sum_{k=1}^{m}n_k(\mu_k-\mu)^T\cdot(\mu_k-\mu)" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;n_k" /> est le nombre d’observations qui prennent la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Q_k,\;\mu" /> est le centre de gravité de l’ensemble des observations, <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu_k" /> est le centre de gravité des observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Q_k" />.


    3. Trouver les facteurs

Les facteurs qui permettent de résumer l’information le mieux possible tout en séparant au plus les différentes modalités de la variable qualitative *Q*
 sont les vecteurs propres de la matrice suivantes:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;V^{-1}B" />


On voit ici le lien avec l’ACP dans le fait de devoir trouver les valeurs et les vecteurs propres d’une matrice qui représente la dispersion des observations. Cependant, contrairement à une ACP classique, l’AFD travaille sur une matrice qui représente à la fois la dispersion totale et aussi l’éloignement des différentes modalités de la variable qualitative les unes par rapport aux autres.


![alt_text](images/Semaine-51.jpg "image_tooltip")


On montre ici un exemple de la représentation d’observations représentant différentes espèces d’iris dans le plan défini par les facteurs.


### Analyse factorielle des correspondances



1. Intuition

L’analyse factorielle des correspondances est une méthode de réduction de dimension pour l’exploration de deux variables qualitatives simultanément. On dispose donc de deux variables qualitatives *X* qui possède *m* modalités <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,...,X_m" /> et *Y* qui possède *r* observations <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,...,X_r" />.


2. Tableau de contingence

Le tableau de contingence de deux variables qualitatives *X* et *Y* correspond à un tableau possédant *m* lignes et *r* colonnes correspondant au nombre de modalités respectives de *X* et *Y* de la forme suivante :


![alt_text](images/Semaine-51.jpg "image_tooltip")


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{ij}" /> est le nombre d’observations qui prennent la modalité *i* pour la variable *X* et la modalité *j* pour la variable *Y*. Le tableau de contingence est noté *T*.


3. Fréquences marginales, profils lignes et profils colonnes

Les fréquences marginales de *X* sont les éléments du vecteur :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{X_1}}{n},...,\frac{n_{X_m}}{n}\}" /> notées <img src="https://latex.codecogs.com/svg.latex?\Large&space;\{f_{X_1},...,f_{X_m}\}" />


Les fréquences marginales de *Y* sont les éléments du vecteur :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{Y_1}}{n},...,\frac{n_{Y_r}}{n}\}" /> notées <img src="https://latex.codecogs.com/svg.latex?\Large&space;\{f_{Y_1},...,f_{Y_r}\}" />


On définit d’ailleurs des matrices diagonales <img src="https://latex.codecogs.com/svg.latex?\Large&space;D_X" /> dont les éléments diagonaux sont les <img src="https://latex.codecogs.com/svg.latex?\Large&space;f_{X_1}" /> et une matrice <img src="https://latex.codecogs.com/svg.latex?\Large&space;D_y" /> dont les éléments sont les <img src="https://latex.codecogs.com/svg.latex?\Large&space;f_{Y_1}" /> et qui serviront à définir des distances dans les parties qui suivent.

On définit les profils-lignes et les profils-colonnes sont des vecteurs qu’on peut extraire de *T* et qu’on définit ainsi :

Le <img src="https://latex.codecogs.com/svg.latex?\Large&space;l^{eme}" /> profil ligne est


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{l1}}{n_{X_l}},...,\frac{n_{lr}}{n_{X_l}}\}=\frac{1}{n}T^{T}D_{X}^{-1}=A" />

Le <img src="https://latex.codecogs.com/svg.latex?\Large&space;h^{eme}" />  profil colonne est


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{1h}}{n_{Y_h}},...,\frac{n_{mh}}{n_{Y_h}}\}=\frac{1}{n}T^{T}D_{Y}^{-1}=B" />


Ces deux vecteurs contiennent respectivement, pour *X* les proportions d’observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_1,...,Y_r" /> parmi les observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_l" />, et pour *Y* les proportions d’observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,...,X_m" /> parmi les observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_h" />.


4. Calcul des liaisons entre les variables explicatives

Pour comprendre la liaison entre les variables *X* et *Y*, on peut procéder à une double ACP :


*   Une ACP sur les profils-colonnes

Cette ACP revient à trouver les valeurs et les vecteurs propres de la matrice *BA*


*   Une ACP sur les profils-lignes

Cette ACP revient à trouver les valeurs et les vecteurs propres de la matrice *AB*. Ces deux ACP donneront des facteurs qui permettent de représenter facilement les relations entre *X* et *Y*, la première permet de représenter *X* à l’aide de combinaisons des modalités de *Y* et la deuxième de représenter les modalités de *Y* en fonctions des modalités de *X*.


### Analyse factorielle multiple des correspondances


1. Intuition

L’analyse factorielle multiple des correspondances est une généralisation de l’analyse factorielle des correspondance au cas où l’on étudie plus de deux variables qualitatives simultanément.



2. Tableau disjonctif complet
    1. Variable indicatrice

Considérons une variable qualitative *X* avec *m* modalités, on définit la variable indicatrice de la <img src="https://latex.codecogs.com/svg.latex?\Large&space;k^{eme}" /> modalité la variable <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_{(k)}" /> :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_{(k)}(i)=\{1,\;si\;X(i)=X_k,\;0\;sinon\}" />


Où *i* est un indice qui représente un individu dans la population.



    2. Matrice des indicatrices

La matrice des indicatrices des modalités de *X* la matrice notée <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_l" /> et définie de la manière suivante :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1=\{X_{(k)}(i),i\in[1,n],k\in[1,m]\}" />


C’est la matrice dont les lignes correspondent aux variables indicatrices de *X* pour chaque individu *i*.


    3. Tableau disjonctif complet

Si on considère maintenant une collection de variables qualitatives <img src="https://latex.codecogs.com/svg.latex?\Large&space;X^{(1)},...,X^{(p)}" />, le tableau disjonctif complet correspond à la concaténation des matrices des indicatrices de chaque variable :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;T=[X_{I}^{(1)}|...|X_{I}^{(p)}]" />


La somme de tous les éléments d’une ligne vaut toujours *p* puisqu’on a *p* variables et que chaque individu ne prend qu’une modalité par variable. De plus, la somme de tous les éléments du tableau vaut *np*, car le tableau comprends *n* lignes.


3. Analyse factorielle multiple des correspondances

L’analyse factorielle multiple des correspondances correspond à une ACP que l’on applique au tableau disjonctif complet. Pour cela on introduit le tableau de Burt qui est en quelque sorte la matrice des variances-covariances du tableau disjonctif complet :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;B=T^{T}T" />


On définit également une matrice des poids qui est une matrice diagonale et chaque portion est de taille égale au nombre de modalités de chacunes des variables explicatives <img src="https://latex.codecogs.com/svg.latex?\Large&space;m^{(1)},...,m{(p)}]" />. On défini chaque portion de diagonale :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;D_k=\frac{1}{n}\{n_{I}^{k},...,n_{m(1)}^{k}\}" />


Et la matrice des poids est définie comme:


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Delta=diag(D_1,...,D_p)" />


Et l’ACP consiste ici à chercher les valeurs et les vecteurs propres de la matrice suivante :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{1}{np}B\Delta^{-1}" />


On obtiendra donc une représentation résumée des individus en fonction de combinaisons des diverses modalités des variables qualitatives considérées.




## Boosting



1. Introduction

Les algorithmes de boosting ont pour but de transformer des prédicteurs faibles et de les transformer en prédicteurs, c’est à dire partir de modèles qui ne sont que partiellement corrélés à la vrai distribution des données et obtenir un nouveau modèle qui puisse approcher la vraie distribution des données autant qu’on le souhaite.

Si de nombreux algorithmes de boosting existent, la première grande percée dans ce domaine fut l’invention de la méthode AdaBoost par Schapire et Freund qui a remporté le prestigieux prix Gödel de computer science en 2003.

L’idée générale de la méthode AdaBoost est de construire successivement des modèles suffisamment bons prédicteurs, en changeant les poids attribués aux observations en gonflant l’importance de celles qui sont à l’origine d’erreurs et réduisant celle des observations correctement classées par le modèle. A la fin, les modèles sont agrégé en utilisant une fonction de leur erreur d’entraînement.



2. AdaBoost
    1. Algorithme

La manière peut être la plus simple d’introduire la méthode Adaboost est de décrire l’algorithme utilisé sous forme de pseudo-code. On considère ici un problème de modélisation où l’on dispose d’observations <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,...,X_i,...,X_n" /> qui sont des vecteurs dont les éléments sont les valeurs des variables explicatives, et d’une variable cible binaire <img src="https://latex.codecogs.com/svg.latex?\Large&space;Y\;\in\;\{-1,+1\}" />.

L’algorithme s’écrit ainsi

	**Initialisation :**  <img src="https://latex.codecogs.com/svg.latex?\Large&space;D_1(i)=\frac{1}{n}\;pour\;i\in\;[1,n]" />


	**Pour**  <img src="https://latex.codecogs.com/svg.latex?\Large&space;t\;\in\;[1,T]" /> **:**


*   Entraîner un modèle sur les données d’apprentissage en pondérant les observations grâce à <img src="https://latex.codecogs.com/svg.latex?\Large&space;D_1" />


*   On obtient un prédicteur qu’on notera <img src="https://latex.codecogs.com/svg.latex?\Large&space;h_t:X\longrightarrow\{-1,+1\}" />


*   On calcule l’erreur de prédiction pondérée <img src="https://latex.codecogs.com/svg.latex?\Large&space;\epsilon_t=\frac{1}{n}\sum_{i=1}^{n}1[h_t(X_i)\neq{Y_i}]\cdot{D_t(i)}" />

*   On calcule <img src="https://latex.codecogs.com/svg.latex?\Large&space;\alpha_t=\frac{1}{2}ln(\frac{1-\epsilon_t}){\epsilon_t}" />, le poids de ce modèle lors de l’agrégation finale

*   On met à jour les poids des observations :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;D_{t+1}(i)=\frac{D_t(i)exp(-\alpha_t{Y_t}h_t(X_i))}{Z_t}" />

Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;Z_t" /> est simplement le facteur de normalisation pour que

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\sum_{i=1}^{n}D_{t+1}(i)=1" />



	**Résultat :** le modèle final obtenu à l’issu de l’algorithme AdaBoost est le suivant :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;H(X)=sign(\sum_{t=1}^{T}\alpha_t{h_t}(X))=sign(F(x))" />


On commence donc par attribuer le même poids à toutes les observations, on construit ensuite itérativement des modèles de prédictions, par exemple une régression logistique, à chaque itération on modifie les poids des différentes observations, ces poids auront une influence sur la manière dont les paramètres du modèles seront optimisés par le modèle. En définitive le modèle produit est une agrégation par vote pondéré des différents en modèle en fonction de leurs performances individuelles sur les données d’entraînement.



    2. Condition de performance

De manière intuitive, un modèle de classification binaire a besoin de rassembler trois caractéristiques afin d’être performant et précis :



*   Il doit avoir été entraîné sur un nombre suffisant d’exemples
*   Il doit pouvoir décrire précisément les observation de la base d’entraînement, autrement dit l’erreur d’entraînement doit être faible.
*   Il doit être simple (une idée existe en statistiques qu’en général qu’un modèle a plus de chance de bien performer qu’un modèle complexe, cette idée est souvent citée comme le rasoir d’Ockham)

Ces conditions essentielles doivent être formalisées mathématiquement afin d’avoir un sens concret lorsqu’on se lance dans la modélisation. Il est assez difficile de dire précisément à priori qu’elle nombre d’observations sont nécessaire pour constituer un jeu d’entraînement de taille suffisante, cela dépend de la proportion relative des observations positives et négatives et de la nature du modèle que l’on souhaite utiliser dans la méthode AdaBoost, par exemple on aura sans doute besoin de moins d’observations pour pouvoir optimiser correctement une régression logistique (cela ne veut pas dire qu’on aura de bon résultats mais au moins on atteindra la convergence des paramètres), et plus d’observations si notre modèle de classification binaire est plus complexe, comme par exemple un réseau de neurones.

Le deuxième critère de performance, communément appelé la _weak learning condition_ correspond à l’idée que chaque modèle de classification binaire qui compose le modèle final présente une erreur d’entraînement plus faible que le pure hasard. En termes mathématiques cela signifie que : <img src="https://latex.codecogs.com/svg.latex?\Large&space;\epsilon_t\;<\frac{1}{2}-\gamma" /> où <img src="https://latex.codecogs.com/svg.latex?\Large&space;\gamma\;>0" />.


    3. Sur-apprentissage d’AdaBoost

Avec ces deux conditions vérifiées, l’algorithme AdaBoost permet de réduire l’erreur d’apprentissage à zéro en relativement peu d’itérations. Cependant comme souvent en statistiques, on s’attend à tomber dans le sur-apprentissage à force de coller trop prêt des données d’apprentissage comme le montre la figure ci-dessous :


![alt_text](images/Semaine-52.png "image_tooltip")


A droite, on peut voir le comportement théorique du modèle qu’on s’attend à observer si on réalise un trop grand nombre d’itérations lors de l’apprentissage. A gauche, on présente un exemple utilisant le _Cleveland heart disease dataset_ comme jeu de données.

    4. Marges

On a vu dans l’exemple précédent qu’il arrive que l’algorithme AdaBoost produise un modèle sur-entraîné, c’est à dire qu’il performe très bien, voire parfaitement sur les données d’apprentissage, mais donne des résultats sous-optimaux sur les données de validation. Cependant, l’algorithme AdaBoost ne tombe pas toujours dans ce travers tant redouté des data scientist, en effet, il existe des critères qui permettent à l’algorithme de produire un modèle final qui prédit de mieux en mieux les données de validation lorsqu’on augmente le nombre d’itérations. Il existe même un cadre théorique dans lequel l’algorithme AdaBoost fournit un modèle dont l’erreur sur l’échantillon de validation atteigne un niveau optimal!

Pour expliquer ce cadre théorique, on introduit la notion de marge. On à notre disposition un modèle construit par agrégation de plusieurs modèles élémentaires dont les résultats sont obtenus à l’aide d’un vote pondéré des différents modèles élémentaires. Hors on accordera pas nécessairement la même confiance aux résultats issus du modèle pour toutes les observations en fonction du résultats du vote. Tout comme lors d’une élection dans le monde réel, on aura plus tendance à faire confiance à une décision qui recueille une forte majorité des voix plutôt qu’une faible majorité. Derrière cette idée de vote fortement ou faible majoritaire se cache la notion de marge. La marge est une valeur qui oscille dans l’intervalle *[-1,1]* qu’on définit de la manière suivante :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_{i}F(x)=\sum_{t:Y_i=h_t(X_i)}\alpha_t-\sum_{t:Y_i\neq{h_t}(X_i)}\alpha_t" />


C’est donc la différence entre le poids cumulé des modèles qui ont raison et le poids cumulé des modèles qui ont tort.

Ce concept de marges est essentiel car on peut montrer que le modèle produit par l’algorithme AdaBoost, et l’ensemble des modèles reposant sur un vote majoritaire de modèles élémentaires, présentent une erreur de généralisation (erreur sur la base de validation) qui dépend non pas du nombre d’itérations (du nombres de modèles élémentaires utilisés pour construire le prédicteur final), mais uniquement des marges obtenues pour les observations dans l’échantillon d’apprentissage. Autrement dit, peu importe combien de modèles sont utilisés pour le vote final, plus les marges des observations du set d’entraînement sont élevées, plus notre erreur de validation sera petite. De fait, si l’ajout de nouveaux modèles participe à augmenter les marges de confiance, alors on ne risque pas le sur-apprentissage, au contraire, le modèle final devrait obtenir de meilleurs résultats sur les données de validation.


![alt_text](images/Semaine-53.png "image_tooltip")


Cette exemple montre les performance d’Adaboost appliqué à un dataset de reconnaissance optique de caractères alphanumériques. On constate à droite que malgré une erreur d’apprentissage qui atteint zéro, la multiplication des itérations continue à faire baisser l’erreur de validation. A gauche on visualise en petit pointillés la distribution cumulée des marges pour cinq itérations, en tirets après cent itérations et en plein après mille itérations. Dans les situations où l’algorithme permet d’augmenter les marges des observations du jeu d’entraînement, on constate bien que la multiplication des itérations augmente le pouvoir prédictif du modèle final.






## Séries temporelles


1. Définition


Une série temporelle est une succession ordonnée de valeurs d’une variable qui sont toutes séparées par un même intervalle de temps. Par exemple si on mesure tous les jours le cours du pétrole à midi pendant sept jours, on obtient une série temporelle de période 1 jour comprenant sept observations consécutives. Ce chapitre introduit l’étude des séries temporelles.


2. Applications

Deux usages courants des séries temporelles sont :
*   Comprendre les lois sous-jacentes qui régissent et et structure les données observées
*   Construire des modèles de prédiction qui permettent d’anticiper les futures valeurs de la série de manière à prendre des décisions ou monitoré la série.
Les champs d’application des séries temporelles sont très variés : économie, prévision de ventes, analyse budgétaire, analyse boursière, prévision de rendement, logistique et inventaire et bien d’autres encore.


3.	Analyse des séries temporelles

Nous allons ici voir différentes manières d’analyser les séries temporelles de différentes techniques et explorer différentes caractéristiques remarquables des séries temporelles.

a.	Moyennes mobiles et techniques de lissage

La plupart des séries temporelles ne se comportent pas comme des fonctions simples du temps, leurs variations peuvent souvent sembler assez imprévisible, c’est pourquoi il existe un certain nombres de techniques qui vont permettre de transformer une série temporelle difficilement compréhensible en une version très simplifiée. C’est techniques sont ce qu’on appelle du lissage et permettent comme leur nom l’indique, d’obtenir des versions résumées des séries temporelles dont les variations sont très atténuées afin d’en extraire la tendance générale.
De manière générale il existe deux grandes familles de techniques de lissage, les moyennes mobiles et les technique de lissage exponentiel.

i.	Moyenne mobile simple

Une technique de lissage très courante et très simple à comprendre et interpréter des séries temporelles. Imaginons que nous étudions la séries temporelle qui donne les montants dépensés par une entreprise en matières premières par jour cette série temporelle est notée X est la réalisation de X à la date t est notée X_t. On définit l’ensemble des moyennes mobiles associées à cette série, l’ensemble des séries temporelles de la forme :
