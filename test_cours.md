

## Machine learning supervisé


### Naive Bayes


[TOC]



## Qu’est ce que vous apprendrez dans ce cours ?

Ce cours est dédié à l’enseignement du modèle bayésien dit naïf, ou Naive Bayes en anglais. C’est un modèle qui repose sur l’indépendance des variables explicatives entre elles, c’est une hypothèse très forte et très rarement vérifée en pratique, néanmoins, ce modèle peut se montrer très utile et permet d’avoir une bonne vision de l’influence de chaque variable sur la variable cible au sein du modèle.

En statistiques, les classification naïves Bayésienne appartiennent à une famille de classifications probabilistes reposant sur le théorème de Bayes.



1. Théorème de Bayes

Le théorème de Bayes correspond à l’affirmation suivante :

Soit ***A*** et ***B*** deux variables aléatoires, alors l’égalité suivante est vérifiée :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(A/B)=\frac{P(B/A)\cdot{P(A)}}{P(A)}" />


La probabilité conditionnelle de ***A*** sachant ***B*** est égale au produit de la probabilité conditionnelle de ***B*** sachant ***A*** et la probabilité de ***A*** divisé par la probabilité de ***B***.



2. Naive Bayes

On considère la situation où on dispose de ***Y***
 la variable cible qualitative (c’est donc un problème de classification) que l’on cherche à prédire, et une collection de variables explicatives <img src="https://latex.codecogs.com/svg.latex?\Large&space;X=(X_1,X_2,...,X_p)" />. Le problème revient à estimer pour chaque observation la loi ***P(Y/X)***, qui donne la probabilité pour ***Y*** de prendre chacune de ses valeurs possibles sachant les valeurs de ***X*** pour cette observation.

Le théorème de Bayes intervient ici et nous donne l’écriture suivante :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(Y|X)=\frac{P(X|Y)\cdot{P(Y)}}{P(X)}" />



Le dénominateur ne fait pas intervenir ***Y*** et n’a donc aucune influence sur les résultats du modèle, on s’intéressera uniquement au numérateur qu’on peut décomposer récursivement grâce aux propriétés des probabilités conditionnelles.




<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(X|Y)\cdot{P(Y)}=P(X_1,X_2,...,X_p,Y)" />


<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(X|Y)\cdot{P(Y)}=P(X_1|X_2,...,X_p,Y)\cdot{P(X_2,...,X_p,Y)}" />


<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(X|Y)\cdot{P(Y)}=P(X_1|X_2,...,X_p,Y)\cdot{P(X_2|X_3,...,X_p,Y)}\cdot{P(X_3,...,X_p,Y)}" />


<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(X|Y)\cdot{P(Y)}=P(X_1|X_2,...,X_p,Y)\cdot{P(X_2|X_3,...,X_p,Y)}\cdot{P(X_3,...,X_p,Y)}...P(X_p|Y)\cdot{P(Y)}" />


C’est ici qu’on a besoin de l’hypothèse fondamentale et naïve qui nous permet de construire nos estimations et qui dit que toutes les variables explicatives doivent être indépendantes, car ainsi on a quelque soit ***i*** entre 1 et ***p***:


<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(X_i|X_{i+1},...,X_p,Y)=P(X_i|Y)" />


De fait on obtient :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(X|Y)=\frac{P(Y)P(X_1|Y)P(X_2|Y)...P(X_p|Y)}{P(X)}" />



Qui est très simple à calculer puisqu’il suffit d’estimer pour chaque valeur de ***Y*** la loi de distribution des <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" />.



    1. Cas où <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> est qualitative

Dans le cas où <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> est une variable explicative qualitative qui prend les modalités <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_{i1},...,x_{iq}" /> alors on peut écrire :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\hat{P}(X_i=x_{ik}|Y=y)=\frac{Card(X_i=x_{ik},Y=y)}{Card(Y=y)}" />


On estime la probabilité que <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> prenne la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_{ik}" /> sachant que ***Y = y*** comme la proportion d’observations où <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i=x_{ik}" /> parmi toutes les observations où ***Y = y***.



    2. Cas où <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> est quantitative

Pour les cas où <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> est quantitative en général on se ramène au cas qualitatif en découpant l’intervalle des valeurs de <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> en ***K*** morceaux indexés par <img src="https://latex.codecogs.com/svg.latex?\Large&space;k\in{[[1,K]]}" /> et délimité par les valeurs <img src="https://latex.codecogs.com/svg.latex?\Large&space;-\infty=\alpha_0,\alpha_1,...,\alpha_{k-1},+\infty=\alpha_k" /> et la loi de probabilité devient :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\hat{P}(X_i=x_{ik}\in[\alpha_j,\alpha_{j+1}]|Y=y)=\frac{Card(X_i\in[\alpha_j,\alpha_{j+1}],Y=y)}{Card(Y=y)}" />


C’est à dire la proportion d’observations pour lesquelles la valeurs de <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> appartient à l’intervalle <img src="https://latex.codecogs.com/svg.latex?\Large&space;[\alpha_j,\alpha_{j+1}]" /> parmi toutes les observations pour lesquelles ***Y = y***.

Une autre manière d’estimer la loi de <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> sachant ***Y*** est de faire l’hypothèse que <img src="https://latex.codecogs.com/svg.latex?\Large&space;P(X_i|Y)" /> suit une loi normale dont on estime les paramètres <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu_i" /> et <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sigma_i" /> grâce aux données disponibles sur <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" />. Sous l’hypothèse de normalité, <img src="https://latex.codecogs.com/svg.latex?\Large&space;P(X_i|Y)" /> sui une loi normale de paramètres :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu_{iy}=\frac{1}{N_y}\sum_{j=1}^{N-y}x_{ij}" />


Qui est la valeur moyenne de <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> parmi les <img src="https://latex.codecogs.com/svg.latex?\Large&space;N_y" /> individus pour qui ***Y = y***. De même on calcule la variance de la loi normale :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;\sigma_{iy}^2=\frac{1}{N_y-1}\sum_{j=1}^{N-y}(x_{ij}-\mu_{iy})^2" />



L’estimateur de la variance de <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_i" /> parmi les individus pour qui ***Y = y***. Une fois cette estimation effectuée, on obtient:



<img src="https://latex.codecogs.com/svg.latex?\Large&space;\hat{P}(X_i=x_{ik}|Y=y)=\frac{1}{\sqrt{2\pi\sigma_{iy}}}exp(\frac{-(x_{ik}-\mu_{iy})^2}{2\sigma_{iy}^2})" />


Une fois toutes les probabilités conditionnelles calculées on obtient pour chaque observation et pour chaque modalité de ***Y*** une probabilité qui détermine notre classification. Chaque observation sera classée dans la modalité de ***Y*** la plus probable en fonction des valeurs des variables explicatives ***X***.



3. Remarques générales

Un avantage du modèle bayésien naïf est qu’il permet de ne pas faire d’hypothèse sur les lois de distribution des variables explicatives si on transforme ces dernières en variables quantitatives. Cependant il est très rare que l’hypothèse fondamentale d’indépendance des variables explicatives soit vérifiée en pratique.

Les modèles bayésiens naïfs peuvent faire l’objet d’une agrégation au même titre que les arbres aléatoires, cela permet en général d’obtenir des résultats bien plus stables et également de mieux respecter l’hypothèse d’indépendance des variables explicatives si, comme on l’a vu dans le cas des random forest, on utilise qu’une partie des variables explicatives pour construire chaque modèle.


Les vecteurs propres de la matrice des variances-covariances sont des combinaisons linéaires des variables <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...,X_p" /> que l’on note <img src="https://latex.codecogs.com/svg.latex?\Large&space;{X'}_1^,{X'}_2^,...,{X'}_p" />


<img src="https://latex.codecogs.com/svg.latex?\Large&space;B=\frac{1}{n}\sum_{k=1}^{m}n_k(\mu_k-\mu)^T\cdot(\mu_k-\mu)" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;n_k" /> est le nombre d’observations qui prennent la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Q_k,\;\mu" /> est le centre de gravité de l’ensemble des observations, <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu_k" /> est le centre de gravité des observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Q_k" />.


Le <img src="https://latex.codecogs.com/svg.latex?\Large&space;l^{eme}" /> profil ligne est


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{l1}}{n_{X_l}},...,\frac{n_{lr}}{n_{X_l}}\}=\frac{1}{n}T^{T}D_{X}^{-1}=A" />

Le <img src="https://latex.codecogs.com/svg.latex?\Large&space;h^{eme}" />  profil colonne est


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{1h}}{n_{Y_h}},...,\frac{n_{mh}}{n_{Y_h}}\}=\frac{1}{n}T^{T}D_{Y}^{-1}=B" />
