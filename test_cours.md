
## Machine learning supervisé


### Régression logistique


[TOC]



## Ce que vous apprendrez dans ce cours

Ce cours a pour but de vous enseigner les principes de la régression logistique et comment appliquer ce modèle à des problème de classification binaire. Vous apprendrez également comment vous protéger du sur-apprentissage grâce à une méthode très utile en machine learning supervisé : la cross validation.



1. Définition

A la différence des régressions linéaires qui vous prédisent un nombre, les modèles de classifications vous prédisent une catégorie. Par exemple, si vous essayez de prédire si quelqu’un va vous acheter un produit en fonction de certaines variables indépendantes, vous entrez dans une problématique de classification car les catégories que vous essayez de prédire sont “oui, la personne va acheter le produit” ou “non, la personne ne va pas acheter mon produit”.

Les régressions logistiques sont une catégorie dans les modèles de classification mais vous en avez beaucoup d’autres comme les arbres de décisions (_decision tree_), SVM (_support vector machine_) ou Naive Bayes



2. Equation

Lorsqu’on construit un modèle de régression logistique, on suppose qu’il existe une fonction *f* qui lie la variables cible *Y* aux variables explicatives représentées dans la matrice *X* de la manière suivante :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(Y=1)=f(X)+\epsilon" />


<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(X)=\frac{1}{1+exp(-(\beta_{0}+X_{1}\beta_{1}+...+X_{p}\beta_{p}))}" />

Où ε est l’erreur.



3. Régression logistique

####




![reg_logistique1](https://drive.google.com/uc?export=view&id=1PM8NiLz9yydMsPErNg1sF5Rl-xS6U4s8)


Lorsque nous avons les régressions linéaires, nous avons vu que notre prédicteur était la ligne que traçait notre modèle. Dans une régression logistique, la ligne est simplement une frontière qui sépare deux catégories. Dans le graphique du dessus, nous essayons de voir si une personne va acheter un produit (représenté par le chiffre 1) ou ne va pas acheter un produit (représenté par le chiffre 0) la ligne représente la probabilité qu’une personne achète (_purchased) _ou non en fonction de son Âge.

L’allure de la courbe est la représentation pour une variable explicative (ici l’âge) de l’équation introduite plus haut.

Dans cet exemple, nous n’avons qu’une variable indépendante et une constante. L’équation ressemble beaucoup à une régression linéaire comme vous pouvez le constater, seulement ici une fonction logistique est appliquée à la variable explicative utilisée pour la régression. Cette fonction contraint les valeurs de <img src="https://latex.codecogs.com/svg.latex?\Large&space;f(X^t\beta)" /> à rester dans l’intervalle [0,1] qui est l’ensemble des valeurs que peut prendre une probabilité. En fonction de la probabilité obtenue, l’algorithme va savoir dans quelle catégorie placer notre individu. 	



    1. Comment faire notre classification  

Maintenant que nous avons dessiné la ligne, nous pouvons commencer nos interprétations. Puisque notre modèle est cette fois probabiliste, les points qui auront une probabilité supérieure à 50% appartiendront à la catégorie A tandis que les points qui auront une probabilité inférieure à 50% appartiendront à une catégorie B. Selon le problème considéré, un autre seuil pourra être choisi, par exemple dans des problématiques de fraude bancaires, on aura tendance à classer dans la catégorie des fraudeurs des individus qui ont des probabilités de fraude inférieures à 50% car on souhaite sécuriser au maximum le système bancaire de menaces frauduleuses. \


Prenons un exemple, en fonction de certaines variables indépendantes, nous avons découvert qu’une personne A a 60% de chance d’acheter le produit. Elle sera donc considérée comme un “acheteur” pour notre modèle. De l’autre côté, si nous avons cette fois une personne B qui a seulement 45% de chances d’acheter le produit, elle sera considérée comme “non-acheteur”.



    2. Régression logistique en python  

```
from sklearn.linear_model import LogisticRegression
logisticreg = LogisticRegression() # on définit le modèle de régression logistique à appliquer aux données

logisticreg.fit(X, y) # estimation du modèle
y_pred = logisticreg.predict(X) # predictions du modèle
MSE = np.sqrt(np.mean((y_pred-y)**2)) # on calcule la racine carré de l'erreur carré moyenne
compare_y_ypred = pd.DataFrame() # on créé un data frame pour comparer les prédictions et la réalité
compare_y_ypred['pred'] = y_pred
compare_y_ypred['y'] = y
logisticreg.score(X, y) # la précision du modèle
```


4. Faux positifs - Faux Négatifs

Puisque notre modèle est fondé sur des probabilités, il peut arriver qu’il ait tort parfois. Les faux positifs et les faux négatifs représentent les erreurs commise par notre modèle de classification.



    3. Faux positif

Continuons sur l’exemple du dessus. Si notre modèle catégorise notre personne A comme “acheteur” et que cette personne dans la réalité n’achète pas le produit alors nous avons affaire à un faux positif. Le modèle s’attendait à un résultat positif qui n’est finalement pas arrivé.



    4. Faux négatif

A l’inverse, si la personne B, que le modèle avait prédit comme non-acheteuse, achète finalement le produit, c’est un faux négatif. Nous avons prédit un résultat négatif mais il n’est pas arrivé.



    5. Soyez attentifs aux faux positif et SURTOUT faux négatifs

Soyez vigilant des faux positifs et négatifs car une erreur de prédiction peut avoir des conséquences plus ou moins graves en fonction de ce que vous essayez de prédire. Par exemple, si vous êtes scientifiques et que vous essayez de prédire un tremblement de terre et que vous tombez sur une faux négatif (c’est à dire que vous aviez prédit que le tremblement n’arriverait pas alors qu’il est arrivé), personne n’était de fait préparé à l’événement.

De manière général, les faux négatifs sont pires que les faux positifs car dans le premier cas, personne n’est préparé à ce que l’événement se passe. Dans le second, vous y êtes préparé et même s’il n’arrive pas, ce n’est pas le plus grave.



5. Comment évaluer votre modèle

La régression logistique est une transposition dans l’intervalle [0,1] de la régression linéaire multiple, les méthodes de sélection et d’évaluation utilisées pour les modèles de régressions linéaires peuvent donc être utilisés pour cette dernière. Cependant, nous aborderons ici d’autres méthodes spécifiquement adaptées aux problèmes de classification binaires.



    6. Matrice de confusion


###
![mat_confusion](https://drive.google.com/uc?export=view&id=11g8FW4ZB-4LSEq2Z_xj426xuhYJ7a3jf)


Une des façons rapides et faciles de mesurer la performance de votre modèle grâce aux matrices de confusion. L’idée est de voir les prédictions que votre modèle a vu juste ainsi que les faux-positifs et faux-négatifs. En faisant les sommes des erreurs sur le total de prédiction vous avez le taux de précision de votre modèle.

Une mesure simple et pertinente de la performance de votre modèle serait de comparer le taux de précision du modèle avec la proportion de positifs dans la base. En effet, le modèle de plus simple dans le cas d’un problème de classification et de classer tous les individus dans la même classe, dans le cas de ce modèle trivial, le taux de précision sera égal à la proportion occupée par le groupe majoritaire dans les données. Mettons que nous avons à notre disposition une base de données qui donne les résultats du baccalauréat pour un échantillon de population. Si l’échantillon contient 70% d’individus qui ont eu leur bac, alors si notre modèle prédit que tout le monde aura son bac, il a raison 70% du temps. De fait, on a intérêt à construire une modèle plus complexe uniquement si sa précision peut être plus élevée que 70%.



    7. Matrice de confusion en python

```
from sklearn import metrics
cm = metrics.confusion_matrix(y, y_pred) # on calcule la matrice de confusion
```


    8. Courbe ROC, AUC et indice de GINI

La courbe ROC (receiver operating characteristic curve) qui permet de visualiser les performances d’un modèle de classification binaire en fonction de son critère de discrimination (le seuil de probabilité à partir duquel le modèle estime qu’une observation est classée comme “positif”).

Cette courbe est obtenue en traçant le taux de vrais positifs (sensitivity) détectés en fonction du taux de faux positifs (*fall out* or *1 - specificity*) pour différentes valeurs du seuil.

![courbe_roc](https://drive.google.com/uc?export=view&id=1uno8_q_YU183T7xwDRoRggr_Zy0i13uW)


Une courbe ROC revêt en général un aspect similaire à l’illustration ci-dessus. Il est très rare et très mauvais signe que la courbe ROC se trouve sous la diagonale, cela signifierait que pour chaque vrai positif détecté, on récupère une quantité plus grande en proportion de faux positifs. La courbe ROC permet immédiatement de décrire les performances du modèle en termes de détection des observations positives, cependant elle permet aussi d’avoir une appréciation générale du modèle. Le biais par lequel la courbe évalue la performance générale du modèle est un indicateur numérique appelé AUC (Area Under the Curve). L’AUC est littéralement le calcul de l’aire délimitée par la courbe ROC et les côtés du carré unité.

 L’AUC s'interprète comme la probabilité que le modèle donne un score plus élevé à une observation positive choisie aléatoirement qu’à une observation négative choisie aléatoirement. L’AUC est également lié à l’indice de GINI qui décrit la dispersion statistique de la population et qui est très utilisé en économie pour quantifier les inégalités.


<img src="https://latex.codecogs.com/svg.latex?\Large&space;GINI=2AUC-1" />


L’AUC varie entre 0 et 1 en théorie, mais les modèles dont l’AUC est inférieure à 0.5 (50%) sont à exclure immédiatement car cela signifie que le modèle est moins bien performant que le hasard total.



    9. Courbe ROC, AUC en python

```
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y, logisticreg.predict(X))
fpr, tpr, thresholds = roc_curve(y, logisticreg.predict_proba(X)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()
```


    10. Comment se protéger du sur-apprentissage ?

Les situations de sous-apprentissage interviennent peu en pratique, ou elles sont souvent dues à un manque de données pertinentes ou d’autres problèmes qui ne peuvent pas être réglés directement par les data sciences. Le véritable ennemi des data scientists est le sur-apprentissage, car il donne l’illusion de la performance, mais est en réalité un piège!

Une manière simple et efficace de se garantir de ce piège est de pratiquer la cross-validation (ou k-fold cross validation). C’est un procédé qui consiste à choisir un entier k (souvent on choisit 10 par défaut), on répartit les observations au hasard dans k groupes de taille égale. Puis on répète k fois la méthode suivante :



*   On isole un groupe i parmi 10 groupes, qu’on appellera **base de test**, et on rassemble les 9 autres, qu’on appellera base **d’apprentissage**.
*   On estime le modèle choisi à l’aide de la base d’apprentissage.
*   On calcule l’erreur commise par le modèle i sur la base de test (le groupe i) que l’on compare à l’erreur commise sur la base d’apprentissage après optimisation.

La comparaison de l’erreur d’apprentissage et l’erreur de test permet de comprendre le réel pouvoir explicatif d’un modèle, car elle quantifie la performance du modèle sur des données inconnues par rapport à sa performance sur des données connues.


![sur_apprentissage](https://drive.google.com/uc?export=view&id=1Dx7vSLocMMcjiYmowVS2GzKXbvxgkN5l)


La figure ci dessus illustre le principe de la k-fold cross-validation. Chaque itération produit des résultat en termes d’erreurs de test et d’apprentissage dont on se sert pour évaluer le modèle. Pour calculer ces erreurs on se base en général sur la fonction de coût qu’on a choisit pour optimiser le modèle, ou bien tout simplement la moyenne des erreur au carré. En général on s’attend à ce que l’erreur de test et de validation soient du même ordre de grandeur, et on espère que l’erreur de manière générale sera petite par rapport aux valeurs prises par la variable cible.



    11. Cross Validation en python

```
''' k fold cross validation'''
from sklearn.model_selection import KFold
kf = KFold(n_splits=10)

# le code ci-dessous permet de générer les 10 séparation train/test pour
# la 10-folds cross-validation
for train_index, test_index in kf.split(X):
      print("Train:", train_index, "Validation:",test_index)
      X_train, X_test = X[train_index], X[test_index]
      y_train, y_test = y[train_index], y[test_index]

# cette méthode permet d'obtenir rapidement des score de précisions
# pour e=les différents modèles estimés par cross-validation      
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn import metrics
scores = cross_val_score(logisticreg, X, y, cv=10)
predictions = cross_val_predict(logisticreg, X, y, cv=10)
```
