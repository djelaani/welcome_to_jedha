
## Boosting


### ADABOOST


## Ce que vous apprendrez dans ce cours

Ce cours s’intéresse à la notion de boosting, qui permet d’améliorer les performances d’un modèle de machine learning supervisé simple en répétant l’apprentissage plusieurs fois de suite en tenant compte des erreurs commises, puis par combinaison des différents modèles. Cette méthode fait appel à la notion de bagging que nous avons vue précédemment.



1. Introduction

Les algorithmes de boosting ont pour but de transformer des prédicteurs faibles et de les transformer en prédicteurs, c’est à dire partir de modèles qui ne sont que partiellement corrélés à la vrai distribution des données et obtenir un nouveau modèle qui puisse approcher la vraie distribution des données autant qu’on le souhaite.

Si de nombreux algorithmes de boosting existent, la première grande percée dans ce domaine fut l’invention de la méthode AdaBoost par Schapire et Freund qui a remporté le prestigieux prix Gödel de computer science en 2003.

L’idée générale de la méthode AdaBoost est de construire successivement des modèles suffisamment bons prédicteurs, en changeant les poids attribués aux observations en gonflant l’importance de celles qui sont à l’origine d’erreurs et réduisant celle des observations correctement classées par le modèle. A la fin, les modèles sont agrégé en utilisant une fonction de leur erreur d’entraînement.



2. AdaBoost
    1. Algorithme

La manière peut être la plus simple d’introduire la méthode Adaboost est de décrire l’algorithme utilisé sous forme de pseudo-code. On considère ici un problème de modélisation où l’on dispose d’observations <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,...,X_i,...,X_n" /> qui sont des vecteurs dont les éléments sont les valeurs des variables explicatives, et d’une variable cible binaire <img src="https://latex.codecogs.com/svg.latex?\Large&space;Y\;\in[-1,+1]" />.

L’algorithme s’écrit ainsi

**Initialisation :**

<img src="https://latex.codecogs.com/svg.latex?\Large&space;D_{1}(i)=\frac{1}{n}\;pour\;{i}\in[1,n]" />


**Pour** <img src="https://latex.codecogs.com/svg.latex?\Large&space;t\;\in[1,T]" /> **:**

*   Entraîner un modèle sur les données d’apprentissage en pondérant les observations grâce à <img src="https://latex.codecogs.com/svg.latex?\Large&space;D_{1}" />

*   On obtient un prédicteur qu’on notera <img src="https://latex.codecogs.com/svg.latex?\Large&space;h_t:\;X\rightarrow[-1,+1]" />

*   On calcule l’erreur de prédiction pondérée 

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\epsilon_t=\frac{1}{n}\sum_{i=1}^{n}1[h_t(X_i)\neq{Y_i}]\cdot{D_t(i)}" />

*   On calcule

 <img src="https://latex.codecogs.com/svg.latex?\Large&space;\alpha_t=\frac{1}{2}ln(\frac{1-\epsilon_t}{\epsilon_t})" />, le poids de ce modèle lors de l’agrégation finale

*   On met à jour les poids des observations :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;D_{t+1}(i)=\frac{D_t(i)exp(-\alpha_t{Y_i}h_t(X_i))}{Z_t}" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;Z_t" /> est simplement le facteur de normalisation pour que <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sum_{i=1}^{n}D_{t+1}(i)=1" />


**Résultat :** le modèle final obtenu à l’issu de l’algorithme AdaBoost est le suivant :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;H(X)=sign(\sum_{t=1}^{T}\alpha_t{h_t}(X))=sign(F(x))" />


On commence donc par attribuer le même poids à toutes les observations, on construit ensuite itérativement des modèles de prédictions, par exemple une régression logistique, à chaque itération on modifie les poids des différentes observations, ces poids auront une influence sur la manière dont les paramètres du modèles seront optimisés par le modèle. En définitive le modèle produit est une agrégation par vote pondéré des différents en modèle en fonction de leurs performances individuelles sur les données d’entraînement.



    2. Condition de performance

De manière intuitive, un modèle de classification binaire a besoin de rassembler trois caractéristiques afin d’être performant et précis :


*   Il doit avoir été entraîné sur un nombre suffisant d’exemples
*   Il doit pouvoir décrire précisément les observation de la base d’entraînement, autrement dit l’erreur d’entraînement doit être faible.
*   Il doit être simple (une idée existe en statistiques qu’en général qu’un modèle simple a plus de chance de bien performer qu’un modèle complexe, cette idée est souvent citée comme le rasoir d’Ockham)

Ces conditions essentielles doivent être formalisées mathématiquement afin d’avoir un sens concret lorsqu’on se lance dans la modélisation. Il est assez difficile de dire précisément à priori qu’elle nombre d’observations sont nécessaire pour constituer un jeu d’entraînement de taille suffisante, cela dépend de la proportion relative des observations positives et négatives et de la nature du modèle que l’on souhaite utiliser dans la méthode AdaBoost, par exemple on aura sans doute besoin de moins d’observations pour pouvoir optimiser correctement une régression logistique (cela ne veut pas dire qu’on aura de bon résultats mais au moins on atteindra la convergence des paramètres), et plus d’observations si notre modèle de classification binaire est plus complexe, comme par exemple un réseau de neurones.

Le deuxième critère de performance, communément appelé la _weak learning condition_ correspond à l’idée que chaque modèle de classification binaire qui compose le modèle final présente une erreur d’entraînement plus faible que le pure hasard. En termes mathématiques cela signifie que : 

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\epsilon_t\;<\frac{1}{2-\gamma}" /> où <img src="https://latex.codecogs.com/svg.latex?\Large&space;\gamma\;>0" />.



    3. Sur-apprentissage d’AdaBoost

Avec ces deux conditions vérifiées, l’algorithme AdaBoost permet de réduire l’erreur d’apprentissage à zéro en relativement peu d’itérations. Cependant comme souvent en statistiques, on s’attend à tomber dans le sur-apprentissage à force de coller trop prêt des données d’apprentissage comme le montre la figure ci-dessous :



![alt_text](images/Copy-of0.png "image_tooltip")


A droite, on peut voir le comportement théorique du modèle qu’on s’attend à observer si on réalise un trop grand nombre d’itérations lors de l’apprentissage. A gauche, on présente un exemple utilisant le _Cleveland heart disease dataset_ comme jeu de données.



    4. Marges

On a vu dans l’exemple précédent qu’il arrive que l’algorithme AdaBoost produise un modèle sur-entraîné, c’est à dire qu’il performe très bien, voire parfaitement sur les données d’apprentissage, mais donne des résultats sous-optimaux sur les données de validation. Cependant, l’algorithme AdaBoost ne tombe pas toujours dans ce travers tant redouté des data scientist, en effet, il existe des critères qui permettent à l’algorithme de produire un modèle final qui prédit de mieux en mieux les données de validation lorsqu’on augmente le nombre d’itérations. Il existe même un cadre théorique dans lequel l’algorithme AdaBoost fournit un modèle dont l’erreur sur l’échantillon de validation atteigne un niveau optimal!

Pour expliquer ce cadre théorique, on introduit la notion de marge. On à notre disposition un modèle construit par agrégation de plusieurs modèles élémentaires dont les résultats sont obtenus à l’aide d’un vote pondéré des différents modèles élémentaires. Hors on accordera pas nécessairement la même confiance aux résultats issus du modèle pour toutes les observations en fonction du résultats du vote. Tout comme lors d’une élection dans le monde réel, on aura plus tendance à faire confiance à une décision qui recueille une forte majorité des voix plutôt qu’une faible majorité. Derrière cette idée de vote fortement ou faible majoritaire se cache la notion de marge. La marge est une valeur qui oscille dans l’intervalle *[-1,1]* qu’on définit de la manière suivante :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_{i}F(x)=\sum_{t:Y_i=h_t(X_i)}\alpha_t-\sum_{t:Y_i\neq{h_t}(X_i)}\alpha_t" />


C’est donc la différence entre le poids cumulé des modèles qui ont raison et le poids cumulé des modèles qui ont tort.

Ce concept de marges est essentiel car on peut montrer que le modèle produit par l’algorithme AdaBoost, et l’ensemble des modèles reposant sur un vote majoritaire de modèles élémentaires, présentent une erreur de généralisation (erreur sur la base de validation) qui dépend non pas du nombre d’itérations (du nombres de modèles élémentaires utilisés pour construire le prédicteur final), mais uniquement des marges obtenues pour les observations dans l’échantillon d’apprentissage. Autrement dit, peu importe combien de modèles sont utilisés pour le vote final, plus les marges des observations du set d’entraînement sont élevées, plus notre erreur de validation sera petite. De fait, si l’ajout de nouveaux modèles participe à augmenter les marges de confiance, alors on ne risque pas le sur-apprentissage, au contraire, le modèle final devrait obtenir de meilleurs résultats sur les données de validation.



![alt_text](images/Copy-of1.png "image_tooltip")


Cette exemple montre les performance d’Adaboost appliqué à un dataset de reconnaissance optique de caractères alphanumériques. On constate à droite que malgré une erreur d’apprentissage qui atteint zéro, la multiplication des itérations continue à faire baisser l’erreur de validation. A gauche on visualise en petit pointillés la distribution cumulée des marges pour cinq itérations, en tirets après cent itérations et en plein après mille itérations. Dans les situations où l’algorithme permet d’augmenter les marges des observations du jeu d’entraînement, on constate bien que la multiplication des itérations augmente le pouvoir prédictif du modèle final.
