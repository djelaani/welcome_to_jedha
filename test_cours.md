
## Analyse des données


### AFC ACM


[TOC]



## Ce que vous apprendrez dans ce cours

Ce cours introduit deux techniques permettant d’analyser des données qualitatives, cela est très utile lorsque l’on doit par exemple s’intéresser à des réponses à des questionnaires par exemple. La première technique, l’analyse factorielle des correspondances permet d’analyser les relations entre deux variables qualitatives. La seconde, l’analyse des correspondances multiples est une généralisation de cette dernière à une collection de plusieurs variables qualitatives.


### Analyse factorielle des correspondances



1. Intuition

L’analyse factorielle des correspondances est une méthode de réduction de dimension pour l’exploration de deux variables qualitatives simultanément. On dispose donc de deux variables qualitatives *X* qui possède *m* modalités <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,..,X_m" /> et *Y* qui possède *r* observations <img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_1,...,Y_r" />.



2. Tableau de contingence

Le tableau de contingence de deux variables qualitatives *X* et *Y* correspond à un tableau possédant *m* lignes et *r* colonnes correspondant au nombre de modalités respectives de *X* et *Y* de la forme suivante :


<table>
  <tr>
   <td>
   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_1" />

   </td>
   <td>

...

   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_r" />

   </td>
   <td>Sommes
   </td>
  </tr>
  <tr>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1" />

   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{11}" />

   </td>
   <td>

...

   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{1r}" />

   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{X_1}" />

   </td>
  </tr>
  <tr>
   <td>...
   </td>
   <td>...
   </td>
   <td>...
   </td>
   <td>...
   </td>
   <td>...
   </td>
  </tr>
  <tr>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_m" />

   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{m1}" />

   </td>
   <td>...
   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{mr}" />

   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{X_m}" />

   </td>
  </tr>
  <tr>
   <td>Sommes
   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{Y_1}" />

   </td>
   <td>...
   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{Y_r}" />

   </td>
   <td>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;n" />

   </td>
  </tr>
</table>


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;n_{ij}" /> est le nombre d’observations qui prennent la modalité *i* pour la variable *X* et la modalité *j* pour la variable *Y*. Le tableau de contingence est noté *Y*.



3. Fréquences marginales, profils lignes et profils colonnes

Les fréquences marginales de *X* sont les éléments du vecteur :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{X_1}}{n},...,\frac{n_{X_m}}{n}\}" /> notées <img src="https://latex.codecogs.com/svg.latex?\Large&space;\{f_{X_1},...,f_{X_m}\}" />


Les fréquences marginales de *Y* sont les éléments du vecteur :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{Y_1}}{n},...,\frac{n_{Y_r}}{n}\}" /> notées <img src="https://latex.codecogs.com/svg.latex?\Large&space;\{f_{Y_1},...,f_{Y_r}\}" />


On définit d’ailleurs des matrices diagonales <img src="https://latex.codecogs.com/svg.latex?\Large&space;D_X" /> dont les éléments diagonaux sont les <img src="https://latex.codecogs.com/svg.latex?\Large&space;f_{X_l}" /> et une matrice <img src="https://latex.codecogs.com/svg.latex?\Large&space;D_Y}" /> dont les éléments sont les <img src="https://latex.codecogs.com/svg.latex?\Large&space;f_{Y_l}" /> et qui serviront à définir des distances dans les parties qui suivent.

On définit les profils-lignes et les profils-colonnes sont des vecteurs qu’on peut extraire de *T* et qu’on définit ainsi :

Le <img src="https://latex.codecogs.com/svg.latex?\Large&space;l^{ème}" /> profil ligne est



<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{l1}}{n_{X_l}},...,\frac{n_{lr}}{n_{X_l}}\}=\frac{1}{n}T^{T}D_{X}^{-1}=A" />


Le <img src="https://latex.codecogs.com/svg.latex?\Large&space;h^{ème}" /> profil colonne est


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\{\frac{n_{1h}}{n_{Y_h}},...,\frac{n_{mh}}{n_{Y_h}}\}=\frac{1}{n}T^{T}D_{Y}^{-1}=B" />



Ces deux vecteurs contiennent respectivement, pour *X* les proportions d’observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_1,...,Y_r" /> parmi les observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_l" />, et pour *Y* les proportions d’observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,...,X_m" /> parmi les observations prenant la modalité <img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_h" />.



4. Calcul des liaisons entre les variables explicatives

Pour comprendre la liaison entre les variables *X* et *Y*, on peut procéder à une double ACP :


*   Une ACP sur les profils-colonnes

Cette ACP revient à trouver les valeurs et les vecteurs propres de la matrice *BA*


*   Une ACP sur les profils-lignes

Cette ACP revient à trouver les valeurs et les vecteurs propres de la matrice *AB*


Ces deux ACP donneront des facteurs qui permettent de représenter facilement les relations entre *X* et *Y*, la première permet de représenter *X* à l’aide de combinaisons des modalités de *Y* et la deuxième de représenter les modalités de *Y* en fonctions des modalités de *X*.



### Analyse factorielle multiple des correspondances



1. Intuition

L’analyse factorielle multiple des correspondances est une généralisation de l’analyse factorielle des correspondance au cas où l’on étudie plus de deux variables qualitatives simultanément.



2. Tableau disjonctif complet
    1. Variable indicatrice

Considérons une variable qualitative *X* avec *m* modalités, on définit la variable indicatrice de la <img src="https://latex.codecogs.com/svg.latex?\Large&space;k^{ème}" /> modalité la variable <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_{(k)}" /> :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_{(k)}(i)=\{1,\;si\;X(i)=X_k,\;0\;sinon\}" />



Où *i* est un indice qui représente un individu dans la population.



    2. Matrice des indicatrices

La matrice des indicatrices des modalités de *X* la matrice notée <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1" /> et définie de la manière suivante :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1=\{X_{(k)}(i),\;{i}\in[1,n],\;{k}\in[1,m]\}" />


C’est la matrice dont les lignes correspondent aux variables indicatrices de *X* pour chaque individu *i*.



    3. Tableau disjonctif complet

Si on considère maintenant une collection de variables qualitatives <img src="https://latex.codecogs.com/svg.latex?\Large&space;X^{(1)},...,X¨{(p)}" />, le tableau disjonctif complet correspond à la concaténation des matrices des indicatrices de chaque variable :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;T=[X_{I}^{(1)}|...|X_{1}^{(p)}]" />


La somme de tous les éléments d’une ligne vaut toujours *p* puisqu’on a *p* variable et que chaque individu ne prend qu’une modalité par variable. De plus, la somme de tous les éléments du tableau vaut *np*, car le tableau comprends *n* lignes.



3. Analyse factorielle multiple des correspondances

L’analyse factorielle multiple des correspondances correspond à une ACP que l’on applique au tableau disjonctif complet. Pour cela on introduit le tableau de Burt qui est en quelque sorte la matrice des variances-covariances du tableau disjonctif complet :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;B=T^{T}T" />


On définit également une matrice des poids qui est une matrice diagonale et chaque portion est de taille égale au nombre de modalités de chacunes des variables explicatives <img src="https://latex.codecogs.com/svg.latex?\Large&space;m^{(1)},...,m^{(p)}" />. On défini chaque portion de diagonale :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;D_k=\frac{1}{n}\{n_{I}^{k},...,n_{m^{(1)}}^{k}\}" />

Et la matrice des poids est définie comme:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Delta=diag(D_1,...,D_p)" />

Et l’ACP consiste ici à chercher les valeurs et les vecteurs propres de la matrice suivante :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{1}{np}B\Delta^{-1}" />


On obtiendra donc une représentation résumée des individus en fonction de combinaisons des diverses modalités des variables qualitatives considérées.
