
## Spark Mllib


[TOC]


Dans ce cours nous allons nous intéresser à MLlib, la librairie de Spark qui vous permettra de créer des modèle de machine learning. Cette librairie n’est pas aussi riche que scikit-learn mais elle offre tout de même de très nombreuses fonctionnalités que vous allez p


## Le workflow typique avec MLlib

Avant de passer à la pratique il est important que vous ayez une idée claire des étapes qui seront nécessaire avant d'entraîner un modèle de machine learning sur vos données.


### Le pré processing

Toutes les **variables catégorielles** devront être traité de la façon suivante:



*   On commence par associer un index à chacune des modalités de la variable, par exemple pour la variable Genre on peut associer l’index 0 à la valeur Homme et l’index 1 à la valeur Femme.
*   On transforme ensuite cet index en vecteur one hot, c’est à dire un vecteur où il y a autant de positions que de modalités, avec la valeur 1 à l’index de la modalité correspondante et 0 zéro ailleurs. Par exemple pour la variable genre on aurait homme = [1, 0] et femme = [0, 1]. En réalité la dernière position de ce vecteur est le plus souvent tronquée car elle n’apporte aucune information, par défault vous verrez donc homme = [1] et femme = [0].

Par ailleurs, **toutes les variables**, qu’elles soient numériques ou catégorielles, devront être concaténées dans un seul vecteur. Par conséquent toutes les variables sur lesquels vous vous baserez pour effectuer votre prédiction se trouveront dans une seule colonne, la plupart de temps on nomme cette colonne “features”.

Voici un schéma récapitulatif de ce processus avec le nom des classes que vous utiliserez dans vos codes.


![](https://drive.google.com/uc?export=view&id=1nqqgpyMdIR6rjIamDjgx4veumjlGvTBd)


De façon plus synthétique voici les données brutes et ce qui devrait en résulter à l’issu du pré processing :


![](https://drive.google.com/uc?export=view&id=1xjkgD7Biv4UQq5G05UykO3IK67L3zWki)


Bien entendu ce ne sont que les étapes minimales de traitement que vous devrez effectuer avant de passer au machine learning. Mais il y a réalité d’autres étapes de pré processing que vous pourriez utiliser selon les cas. En voici quelques exemples :



*   Le remplacement des valeurs manquantes avec différentes stratégies (utilisation de la moyenne, de la médiane …)
*   La normalisation ou le scaling des variables numériques
*   La discrétisation des variables numériques en quantile
*   Le pré processing de variables contenant du texte avec le TF IDF, la suppression des stop words ou la génération de n-grams.


### L’entrainement d’un modèle de ML

Une fois les étapes de pré processing effectuées vous allez pouvoir suivre les étapes classique qui vous permettront d'entraîner un modèle, à savoir  :



*   L’application d’un algorithme sur vos données pour produire un modèle
*   La définition d’un évaluateur permettant de juger de la qualité du modèle
*   L’utilisation de la cross validation pour choisir le meilleur modèle au regard de la métrique que vous avez défini

La façon typique de procéder avec MLlib est d'utiliser un pipeline. Tout comme dans scikit-learn le pipeline est un objet combinant l’ensemble des étapes de transformations qui vous permettent de passer de vos données brutes au résultat souhaité. Pour illustrer cela on pourrait donc compléter notre schéma précédent sur le pré processing :


![](https://drive.google.com/uc?export=view&id=1YBaRfe565v9o3OVODEVMrc03uBmPMEz3)


En réalité on va encore ajouter une dernière étape dans ce pipeline qui est l’application d’un algorithme de machine learning, disons dans ce cas d’une régression logistique. De cette manière le pipeline constitue l’ensemble des étapes permettant de passer des données brutes à un modèle entraîné.


![](https://drive.google.com/uc?export=view&id=1JBRhA7uU1Pug_-kKxkMiMH6_Lxp9U8Yf)


En plus de clarifier grandement le processus permettant de générer un modèle à partir de données brutes, l'intérêt des pipelines est également lié à la cross validation. Vous allez en effet pouvoir déterminer une grille de paramètres pour l’ensemble du pipeline, c’est à dire pour l’algorithme de machine learning mais aussi pour les étapes de pré processing dont le choix des paramètres peut influer sur la performance du modèle, c’est par exemple le cas :


    -       Du choix de la méthode pour remplacer les valeurs manquantes


    -       Du choix de la méthode de discrétisation des variables continues


    -       Du nombre d’axe à conserver si vous effectuez une ACP


    -       …

## Prise en main de MLlib

## Chargement des données

Pour prendre en main la librairie MLLib nous allons effectuer une classification permettant de déterminer si un individu gagne plus ou moins de 50 000 dollars par an étant donnée un ensemble de facteurs.

Comme d’habitude nous allons commencé par déclarer notre compte de stockage dans l’objet SparkSession et nous allons charger les données dans un dataframe :


![](https://drive.google.com/uc?export=view&id=1elSguFhH-gmbt1750-W1znLFCfI9mI4F)


## Preprocessing et utilisation d’un pipeline

Comme nous l’avons vu dans le cours, nous allons devoir effectuer certains traitement sur les données avant de pouvoir entraîner notre modèle.

Nous allons d’abord devoir traiter les variables catégorielles, ce sont normalement des chaînes de caractères (ce qui correspond au type StringType). Pour chacune des modalités de ces variables nous allons devoir associé un index qui sera un entier (correspondant au type IntegerType en Spark). La class StringIndexer permet de faire cela. Un objet de type StringIndexer prend argument le nom de la colonne sur laquelle il doit s’appliquer et le nom de la colonne contenant l’index.

Nous allons d’abord commencé par la variable salary, qui est la variable que nous cherchons à prévoir. Celle-ci a deux valeurs possible : “>50K” ou “<=50K”. Nous indiquons au StringIndexer que nous souhaitons que la colonne contenant l’index des valeurs soit nommée label.


![](https://drive.google.com/uc?export=view&id=1_hTFYEQ_gSee82HDGBoCYxC0o-puFkZy)


Comme dans Scikit-Learn la plupart des class de MLLib s’utilise avec les méthodes fit et transform.

Pour un objet de type StringIndexer la méthode fit va permettre d’obtenir un objet capable d’associer à chaque modalité un index. Il ensuite falloir utiliser la méthode transform de cet objet pour ajouter la colonne contenant les index à notre dataframe (la colonne label).


![](https://drive.google.com/uc?export=view&id=1xukvzW8_xfH3dS8hqgY61DIfiCwudRD3)


Cela un peu lourd, surtout quand vous avez beaucoup de transformation de ce type à faire. L’utilisation des pipelines va nous permettre de simplifier cela, nous allons donc faire comme si nous réparations de cette cellule de code :


![](https://drive.google.com/uc?export=view&id=1jVh8-8QH7QeHwEeq0HuC20mFiMxXeM1q)


Maintenant que nous avons l’objet permettant de créer l’index pour la colonne salary nous allons nous occuper des autres variables catégorielles. La variable string_columns contient la liste du nom des colonnes correspondant aux variables catégorielles de notre dataset. Pour chacune de ces colonnes nous allons créer un objet de type StringIndexer, le nom des colonnes contenant les index des modalités sera le nom original de la colonne avec le suffix Index (par exemple workclass devient workclassIndex). Par soucis de simplicité nous ne parlerons pas du paramètre handleInvalid=”skip” mais nous pourrons évoquer son utilité en classe.


![](https://drive.google.com/uc?export=view&id=18f4GBWaN5WVnmgahAU_r5PQOg_-8QOxo)


Une fois que nous avons pu associer un index pour chaque variable catégorielle il va maintenant falloir créer des indicatrices pour chacune d’entre elle (un vecteur avec un 1 à l’index de la modalité correspondante et des 0 pour tout les autres index). On peut directement passer une liste de colonne à un objet de type OneHotEncoderEstimator. Le nom des colonnes contenant les vecteurs avec les indicatrices sera le nom original de la colonne avec le suffix Vec (par exemple workclass devient workclassVec). Notez que l’on ne doit pas faire cette étape pour la colonne label qui est celle que nous cherchons à prédire.


![](https://drive.google.com/uc?export=view&id=1qaJlBZfUdEJZrUpKLa9JReO09BE-1Aa1)


La dernière étape de pre processing consiste à rassembler toutes les colonnes correspondant à nos prédicteurs dans un seul et même vecteur, la colonne label n’est donc pas concerné. Nous allons donc rassembler dans un vecteur :



*   Les vecteur correspondant aux indicatrices des variables catégorielles
*   Les variables numériques (en l'occurrence age et hours_per_week). Assurez-vous avant que celles-ci soient bien d’un type numérique tel que IntegerType, FloatType, DoubleType …

Nous allons donc fournir au VectorAssembler le nom des colonnes à rassembler et lui indiquer que la nouvelle colonne créée s’appeler features.


![](https://drive.google.com/uc?export=view&id=1l6QrGKQvdj4iNLdPgmxPQIsFWSB1JXgu)


Nous avons maintenant créer toutes les étapes de pre processing de note pipeline. Avant de pouvoir toute les rassembler dans un objet de type Pipeline il nous manque encore une dernière étape: l'algorithme de classification que nous allons utiliser. Nous allons donc créer un objet de type régression logistique (rassurez vous il existe plein d’autres alogrithmes de classification dans la librairie MLLib). Pour cela nous simplement indiquer à la class régression logistique le nom de la colonne contenant la variable à prédire et le nom de la colonne contenant les prédicteurs.


![](https://drive.google.com/uc?export=view&id=1V75ZAWn3voUkrxxMqRabdgFiZs1OYEsQ)


Pour finir nous allons rassembler toutes ces étapes de traitement dans un Pipeline de la façon suivante :


![](https://drive.google.com/uc?export=view&id=1Mzq9IY5vPqPq_M8WQsKli0T0NN9RvIMY)


Voilà ! Vous avez maintenant un objet de type pipeline qui comprend toutes les étapes de traitement que nous avons définies pour aboutir à un modèle de classification.


## Entrainement du modèle

Pour entraîner notre modèle nous allons d’abord splitter notre dataset en ensemble d'entraînement (70% du dataset)  et de test (30%) avec la méthode randomSplit. Nous allons ensuite utiliser la méthode fit de notre pipeline pour entraîner notre modèle sur l’ensemble d'entraînement.


![](https://drive.google.com/uc?export=view&id=1hoE2N9R-gxayrGz6Sc2sfLK_WaezQxct)


La variable pipeline_lr_fitted contient notre regression logistique entrainé. Plus précisément notre régression logistique est en fait la dernière étape de notre pipeline après application de la méthode fit.


![](https://drive.google.com/uc?export=view&id=1RBMf35Ob6wVKLLHZ33ux7IENTyHS5mvb)


On peut directement la récupérer de la façon suivante :


![](https://drive.google.com/uc?export=view&id=19kr1TeVt_pBNi25EuGgzGe_D_-pc7JZK)


## Evaluation et analyse du modèle

Nous allons maintenant évaluer les performances de notre modèle sur les ensemble de test et d'entraînement. Pour cela il faut d’abord appliqué le modèle pour obtenir les prédiction, on utilise donc la méthode transform de pipeline_lr_fitted.

Nous définissons ensuite un évaluateur de classification binaire en renseignant le nom de la colonne avec les probabilités (Spark nomme cette colonne rawPrediction par default) et la métrique d’évaluation que nous souhaitons utiliser, dans notre cas l’AUC.

Nous utilisons enfin la méthode evaluate de notre évaluateur pour obtenir l’AUC sur l'ensemble d'entraînement et de test.

![](https://drive.google.com/uc?export=view&id=1WOIv2Ec2YrXF8OsGTMurUS_-hyNxivLf)


Nous pouvons également afficher les coefficients de notre régression logistique comme ci-dessous. Notez qu’il faut pour cela accéder à l’objet correspondant à notre régression logistique qui est la dernière étape du pipeline.


![](https://drive.google.com/uc?export=view&id=1wiqvanIZJI5o5e4kn0iGwvT-G8zQEUfG)


Vous pouvez manuellement regardez les résultats de votre régression en affichant les colonnes pertinentes d’un dataset sur lequel vous avez appliqué votre modèle.


![](https://drive.google.com/uc?export=view&id=1sPJRPJxbyOVxGpoQf-S3aPREi2230Oo_)


## Cross validation

Nous avons entraîné notre régression logistiques en laissant les paramètres par défaut. Il est bien sur  possible de renseigner des paramètres spécifiques pour son entraînement. Il également possible de tester plusieurs combinaisons de paramètres pour savoir laquelle fonctionne le mieux grâce à la cross validation.

Pour cela il faut d’abord définir une grille de paramètre à l’aide de la classe Param

GridBuilder et de ses méthodes addGrid et build. La méthode addGrid prend en paramètre un pointeur sur le paramètre que l’on souhaite faire varier ainsi que l’ensemble des valeurs qu’il pourra prendre. Par exemple pour le nombre maximum d’itération on utilise le pointeur lr.maxIter (nous avions précédemment stocker notre régression logistique dans une variable nommé lr avant de construire le pipeline) et on indique que l’on veut tester les valeurs 1, 5 et 10 pour ce paramètre.

Une fois la grille construite on fournit au CrossValidator notre pipeline non entraîné, la grille de paramètre, la métrique d'évaluation (c’est sur ce critère que l’on va juger de la meilleurs combinaison de paramètre) et le nombre de fold pour la cross validation.

On peut ensuite utiliser les méthode fit pour déterminer la meilleur combinaison de paramètres puis transform pour appliquer le pipeline avec cette combinaison de paramètres.


![](https://drive.google.com/uc?export=view&id=13Gfr8SjoTwIhkoo9cENAtVIoHsC04YzO)


![](https://drive.google.com/uc?export=view&id=18VS0_yu_ume9O36rPz2q2mj7FYcmjL5o)
