## Machine learning supervisé


### L’essentiel


## Variable cible

Le ML supervisé dépend comme son nom l’indique d’exemple pour lesquels on possède déjà l’information sur ce que l’on souhaite prédire i.e. une variable cible.


## Méthodologie

La figure ci dessous illustre un exemple assez polyvalent de structure qu’il est possible d’adopter pour entraîner un modèle de machine learning :


![svm6](https://drive.google.com/uc?export=view&id=1RyhDjgr9UR2YT3xUDJlYBhhgy_NZdx8z)


Une fois les données nettoyées et le feature engineering terminé (ou au moins pour le moment) on peut faire entrer les données dans un algorithme de Grid Search qui va tester une à une toutes les associations de paramètres possible parmi les choix proposés. Une séparation train test sera effectuée selon le type de Cross Validation spécifiée dans l’instance de GridSearchCV, les données de train seront utilisées par la pipeline afin d’estimer les paramètres de normalisation, de la PCA et du modèle qui seront ensuite utilisés pour calculer le score et les prédictions du modèle sur l’échantillon de test.


## Les 5 grandes familles de modèles


<table>
  <tr>
   <td>Famille de modèles
   </td>
   <td>Avantages
   </td>
   <td>Inconvénients
   </td>
  </tr>
  <tr>
   <td>Régressions (linéaires, ridge, lasso, logistique)
   </td>
   <td>
<ul>

<li>Simplicité

<li>Facilité d’explication

<li>Faible variance
</li>
</ul>
   </td>
   <td>
<ul>

<li>Impose de fortes contraintes sur la nature du modèle (fort biais, faible variance)

<li>Ne permet pas de prendre en compte les interactions entre variables
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Modèles Bayésiens
   </td>
   <td>
<ul>

<li>Simplicité

<li>Besoin de faibles volumes de données pour converger

<li>Faible variance
</li>
</ul>
   </td>
   <td>
<ul>

<li>Fort biais (relativement moins performants sur de gros jeux de données)

<li>Ne prend pas en compte les intéractions entre variables
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Random Forest
   </td>
   <td>
<ul>

<li>Faible variance

<li>Prise en compte des interactions entre variables

<li>Très bonnes performances en pratique

<li>Bonne gestion des problèmes aux très nombreuses variables
</li>
</ul>
   </td>
   <td>
<ul>

<li>Risque de sur-apprentissage

<li>Difficulté d’estimation des hyper-paramètres

<li>Difficulté d’interprétation
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>SVM
   </td>
   <td>
<ul>

<li>Faible variance

<li>Prise en compte des interactions entre variables

<li>Très bonnes performances en pratique

<li>Bonne gestion des problèmes aux très nombreuses variables
</li>
</ul>
   </td>
   <td>
<ul>

<li>Risque de sur-apprentissage

<li>Difficulté d’estimation des hyper-paramètres

<li>Difficulté d’interprétation
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Réseaux de neurones
   </td>
   <td>
<ul>

<li>Faible variance

<li>Prise en compte des interactions entre variables

<li>Souvent les meilleurs performances en pratique

<li>Bonne gestion des problèmes aux très nombreuses variables
</li>
</ul>
   </td>
   <td>
<ul>

<li>Risque de sur-apprentissage

<li>Difficulté d’estimation des hyper-paramètres

<li>Difficulté d’interprétation

<li>Temps d’estimation très long
</li>
</ul>
   </td>
  </tr>
</table>


## Sauvegarder et chargez vos modèles dans python

[suivez ce lien](https://deparkes.co.uk/2018/06/18/save-and-load-sci-kit-learn-models/)

