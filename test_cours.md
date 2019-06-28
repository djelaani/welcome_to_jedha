## Traitement des valeurs manquantes et Feature engineering


1. Traitement des valeurs manquantes

Un des problèmes les plus courants que l’on rencontre lors de la phase de nettoyage des données et leur analyse est le traitement des valeurs manquantes, c’est à dire lorsqu’une des variables n’est pas renseignée pour une observation donnée.

Il n’existe pas vraiment de bonne manière d’appréhender les valeurs manquantes, déterminer la valeur de remplacement idéal serait un problème de prédiction à part entière, cependant plusieurs techniques existent en fonction du type de problème - séries temporelles, machine learning, régression… Il est donc délicat de proposer une solution générale. On fera un résumé ici des principales méthodes et nous proposerons une solution structurée.



    1. Pourquoi a-t-on des valeurs manquantes

Avant de nous plonger dans les différentes techniques de traitement, nous nous demanderons d’abord pourquoi observe t’on des valeurs manquantes ?



*   **Donnée manquante complètement aléatoirement (Missing Value Completely at Random):** c’est la situation dans laquelle la vraie valeur de la donnée manquante ne dépend pas de la vraie valeur ni des valeurs des autres variables décrivant l’individu.
*   **Donnée manquante aléatoirement (Missing Value at Random):** La probabilité qu’une valeur soit manquante ne dépend pas de la vraie valeur mais des autres variables décrivant l’individu. Par exemple les français ont tendance à ne pas vouloir parler de leurs revenus, contrairement aux américains, sans que cette préférence soit liée nécessairement au niveau de revennu.
*   **Donnée manquante non aléatoirement (Missing Value Not at Random):** C’est lorsque la probabilité qu’une donnée soit manquante est liée directement à la valeur de cette dernière. Par exemple, lors d’une étude sur l’obésité, on constate que si les participants remarquent une prise de poids ils ont tendance à quitter l’étude et générer des valeurs manquantes.

Dans les deux premiers cas on peut retirer les observations concernées du dataset sans que cela est un impact trop important sur les distributions des variables. Dans le dernier cas on ne peut retirer les observations sans risquer d’introduire un biais dans notre jeu de données. En effet, si les personnes riches par exemple, ont tendance à ne pas vouloir révéler leur patrimoine ou leur revenu, alors on risque de sous représenter ces individus dans le dataset.



    2. Interpolation vs Suppression

Dans la situation où l’on ne souhaite pas retirer les observations présentant des valeurs manquantes, on peut procéder à ce qu’on appelle l’interpolation. C’est à dire qu’on remplace les valeurs manquantes par une valeur qui dépend des valeurs déjà renseignées. Le tableau ci-dessous offre un résumé simple des différentes situations dans lesquelles ont peut se trouver et les stratégies que l’on peut adopter :


![](https://drive.google.com/uc?export=view&id=1v1EZxk4Ox1QOQG6rL6IGaGIRWv9NQjzN)


*   **Listwise**

    Listwise suppression (étude des observations complètes) consiste à retirer du dataset toutes les observations qui contiennent au moins une valeur manquante. Si le nombre de telles observation est petit comparativement à la taille du dataset il est très commode de simplement les retirer. Cependant les situations où les valeurs manquantes sont complètement aléatoires sont rares et le fait d’éliminer ces observations introduit un biais.


    ```
# In python
mydata.dropna(inplace=True)
```


*   **Pairwise**

    La suppression pairwise s’intéresse à toutes les observations pour lesquelles les variables d’intérêt sont renseignées et maximise donc le nombre d’observations utilisables pour l’analyse. Un avantage de cette approche est qu’il augmente la qualité de l’analyse mais présente bien des désavantages. Cette technique part du principe que toutes les valeurs manquantes sont complètement aléatoires. On se retrouve avec un nombre d’observations différent qui entre en jeu pour la contribution des différentes variables dans l’analyse, ce qui peut rendre l’interprétation difficile.

    ![](https://drive.google.com/uc?export=view&id=1UWL4Z05tFRIyojNtS82yEAPH3MhtfGQb)


*   **Dropping Variables**

    Il est souvent plus avantageux de conserver la données plutôt que de l'ignorer, cependant dans certains cas une variable peut présenter de forts taux de non renseignement comme 60%, dans ce cas on peut retirer cette variable du dataset à condition qu’elle n’apporte pas d’information dans notre analyse. L’interpolation est très souvent une meilleure solution que l’abandon d’une variable.


    ```
del mydata.column_name
mydata.drop('column_name', axis=1, inplace=True)
```


        1. Méthodes spécifique aux Séries temporelles
*   **Last observation carried forward (LOCF) & Next Observation Carried Backward (NOCB) \
**C’est une approche classique pour analyser des études longitudinale lorsque certaines données de suivi sont manquantes. Ces deux méthodes consistent pour la première à répéter la dernière valeur renseignée précédente et la deuxième à remplacer les valeurs manquantes par la première données renseignée suivante. Ces deux méthodes peuvent toutefois introduire des biais si la série temporelle présente une tendance.
*   **Interpolation linéaire**

    Cette méthode consiste à estimer la tendance de la série temporelle et remplacer les valeurs manquantes comme si elles suivaient exactement cette tendance.

*   **Seasonal Adjustment + Linear Interpolation**

    Cette méthode consiste à prendre en compte la tendance et la composante saisonnière lors du remplacement des valeurs manquante. ** \
**

![](https://drive.google.com/uc?export=view&id=1JVYgXZZgJNaPB7hH5Ane3Bl4zCgU3eZn)


![](https://drive.google.com/uc?export=view&id=10ZyuNyCg1gJVlQeKw1DnAdtdEFt-E9hZ)

![](https://drive.google.com/uc?export=view&id=1sN0r-3Xgaq7FC8s4EdsaHF9zOgR8gjlS)

![](https://drive.google.com/uc?export=view&id=11EIWTiQYmGM12mIGh0XuVlrGAxSgF5zB)




        2. Mean (Moyenne), Median (Médiane) and Mode

L’interpolation par la moyenne, la médiane ou le mode sont trois méthodes très simples, ce sont les seules qui ne prennent pas en compte les caractéristique des séries temporelles ou l’information venant des autres variables. Ces méthodes sont très rapide mais présentent un inconvénient majeur qui est de réduire la variance du dataset puisque toutes les observation présentant des valeurs manquantes vont se ressembler un peu plus.


```
from sklearn.preprocessing import Imputer
values = mydata.values
imputer = Imputer(missing_values='NaN', strategy='mean')
transformed_values = imputer.fit_transform(values)
# strategy can be changed to "median" and "most_frequent"
```




        3. Régression linéaire

Pour commencer, de nombreux prédicteurs des variables contenant des valeurs manquantes sont calculés en utilisant une matrice de corrélation. Les variables les plus liée à la variable qu’on cherche à interpoler sont sélectionnées et utilisées dans un modèle de régression linéaire. Les cas ou la variable interpolée est renseignée sont utilisés pour apprendre le modèle qu’on utilise ensuite pour prédire les valeurs les plus probables pour remplacer les valeurs manquantes. On peut ensuite répéter la manoeuvre en utilisant cette fois toutes les observations pour l’apprentissage, prédire de nouvelles valeurs de remplacement et ainsi de suite jusqu’à convergence des valeurs d’interpolation.

Cette méthode produit en théorie de bons estimateurs pour les valeurs manquantes des variables. Cependant, cette méthode présente les inconvénients suivants, qui tendent à prendre le dessus sur ses avantages : premièrement les valeurs ainsi trouvées reflètent la logique générale du dataset et réduisent la variance du dataset et tend également à renforcer la corrélation entre les variables du dataset alors qu’il n’ existe pas nécessairement de lien linéaire entre elles et qu’on préfère en tout cas que non.



        4. Interpolation multiple
*   **Interpolation :** On interpole _m_ fois  les valeurs manquantes à partir d’une loi de probabilité, ce qui donne _m_ datasets sans valeurs manquantes.
*   **Analyse :** On analyse chacun des datasets
*   **Pooling :** On utilise les _m_ analyses afin de former un résultat final.



![](https://drive.google.com/uc?export=view&id=1SF0Uo5-enRqQDrMK9WW5nryzQ2Unblf6)



        5. Interpolation des variables qualitatives
*   L’interpolation par le mode est très simple à mettre en place mais peut introduire un fort biais.
*   Les valeurs manquantes peuvent être traitées comme une catégorie à part entière.
*   On peut tenter de prédire les valeurs des données manquantes à partir des autres variables, grâce à des modèles comme naive bayes ou decision tree etc…
*   On peut procéder à une interpolation multiple.
        6. KNN (K Nearest Neighbours)

Dans cette méthode, les _K_ voisins les plus proches selon une distance préalablement choisie sont utilisés pour calculer la valeur de remplacement, qui sera la moyenne pour une variable quantitative ou le mode pour une variable qualitative.

Le choix de la distance dépend du type de variables dont on dispose dans le dataset.



*   Pour les variables quantitatives on utilise la distance euclidienne pour calculer leur contribution à la distance.
*   Pour les variables qualitatives la distance vaut un si les modalités sont différentes et zéro si elles sont égales.

On somme toutes les composantes de la distance afin de calculer la distance entre deux observations.

L’avantage principale de KNN est que cette méthode est très simple à comprendre et à mettre en place. La nature non paramétrique de KNN (contrairement aux régressions par exemple) lui donne un plus dans certaines situations dans lesquelles les données sont fortement contrastées.

L’un des inconvénients principaux de KNN est qu’il peut prendre beaucoup de temps dans le cas de datasets très grands car il est nécessaire de calculer les distances entre toutes les observations, de plus la méthode peut ne pas fonctionner très bien lorsqu’on dispose de nombreuses variables car les différences entre les distances deviennent plus faibles.


```
from fancyimpute import KNN   

# Use 5 nearest rows which have a feature to fill in each row's missing features
knnOutput = KNN(k=5).complete(mydata)
```


Parmi toutes les méthodes décrites plus haut, l’interpolation multiple et KNN sont souvent utilisées. L’interpolation multiple est souvent privilégiée car plus simple.

**Resources: \
1. [https://www.bu.edu/sph/files/2014/05/Marina-tech-report.pdf \
](https://www.bu.edu/sph/files/2014/05/Marina-tech-report.pdf)2. [https://arxiv.org/pdf/1710.01011.pdf \
](https://arxiv.org/pdf/1710.01011.pdf)3. [https://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/ \
](https://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/)4. [https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/ \
](https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/)5. Time-Series Lecture at University of San Francisco by Nathaniel Stevens**



2. Feature engineering

Le feature engineering est l’exercice de création de nouveau features (nouvelle variable) afin d’améliorer la clarté d’une analyse, trouver de nouvelles corrélations ou d’augmenter les performance d’un modèle de prédiction à partir des données déjà à notre disposition (dans la plupart des cas).

C’est une composante essentielle des data science car elle permet de vraiment faire la différence entre l’application pure et simple d’un modèle et la véritable réflexion. Comme le dit Andrew Ng, professeur de machine learning à l’université de Stanford

_“Coming up with features is difficult, time-consuming, requires expert knowledge, “Applied Machine Learning” is basically feature engineering.” (La création de variable est difficile, chronophage, et nécessite de l’expertise, le “Machine Learning Appliqué” peut se résumer à la création de variables)_.

A travers le feature engineering, il est possible d’isoler de l’information essentielle, mettre en valeur des modèles comportementaux, et d’apporter le l’expertise sur certains domaine.

Sans surprise, il est facile de se sentir coincé lorsqu’on se lance dans le feature engineering car les possibilités sont quasiment infinies, c’est pourquoi nous allons aborder ici une vingtaine de méthodes qui permettent de vous orienter dans ce travail.



    3. Qu’est ce que le feature engineering

Le feature engineering est une discipline informelle dont les définitions sont multiples. Le processus de construction d’un projet de machine learning est fluide, itératif et non-linéaire ce qui rend difficile de construire une définition inébranlable et unique.

En résumé le feature engineering pourrait se décrire grossièrement comme : **la construction de nouvelles variables à partir de variables existantes afin d’améliorer les performances d’un modèle.**

Le processus typique de construction d’un projet de data science peut se décomposer ainsi :



*   Evaluation / Définition du problème et récolte des données
*   Analyse descriptive et exploratoire (ce qu’on a fait en début de semaine)
*   Nettoyage des données (ce qu’on a fait aujourd’hui) Data cleaning en anglais.
*   Feature engineering
*   Modélisation, model training en anglais. (que l’on verra la semaine prochaine)
*   Rendu du projet, mise en forme des conclusions, mise en production du modèle
    4. Qu’est ce qui n’est pas du feature engineering

Certaines étapes de construction d’un projet de data science ne s’apparentent pas au feature engineering, par exemple :



*   La récolte de données initiales n’est pas considérée comme du feature engineering
*   De la même manière l’identification et la création de la variable cible
*   La suppression d’observation dupliquées, la gestion des données manquantes ou la rectification de données aberrante est considérée plutôt comme du data cleaning.
*   On ne considère pas non plus que la normalisation fait partie du feature engineering.
*   Enfin, les méthodes de réduction de dimension que nous verrons en semaine 4 n’entre pas non plus dans le cadre du feature engineering.

C’est une catégorisation purement arbitraire, certains data scientist considèrent peut être un autre agencement comme étant le bon et cela ne pose aucun problème, l’important est que nous nous mettions d’accord à ce stade sur une définition des termes.

Passons maintenant à l’exposé des méthodes de feature engineering!



    5. Variables indicatrices

La première technique de feature engineering que nous aborderons consiste à isoler l’information clé. On pourrait légitimement se demander si ce n’est pas le rôle du modèle de comprendre quelle information est importante. En pratique cela n’est si simple, cela dépend de la quantité d’information dont on dispose et de la présence de signaux contraires qui empêchent le modèle d’établir des règles de prédictions simples.

Il est très facile en pratique d’aider le modèle à se concentrer sur certaines informations en les mettant en valeur dans les données elles même. Cette technique repose sur la construction de variable indicatrices (dont la valeur est 0 ou 1 selon un critère), nous exposons ici quelques exemples :



*   **Indicatrice de seuil (threshold indicator)**: Mettons que l’on étudie les préférences des consommateurs américains en termes de boissons alcoolisées et qu’on dispose d’une variable donnant l’âge des individus. On peut créer une variable indicatrice qui vaut 0 si un individu a moins de 21 ans et 1 si l’individu est plus âgé que 21 ans qui est l’âge légal de consommation d’alcool aux Etats Unis.
*   **Indicatrices de plusieurs critères (multiple feature indicator) :** Si on cherche à prédire le prix de l’immobilier dans une certaines régions et qu’on mesure le nombre de chambres et de salles de bain, on peut construire une indicatrice qui vaut 1 lorsqu’une maison comprend 2 chambres et 2 salles de bain car on sait que ce type de bien a une valeur bien supérieure sur le marché.
*   **Indicatrice d’événements spéciaux (special events indicator) :** Imaginons qu’on modélise les ventes d’un magasin chaque jour dans l’année, il peut être intéressant de créer des variables indicatrices qui valent 1 pendant le Black Friday, les soldes ou la période de Noël, afin que le modèle comprennent que ces périodes sont marquées par des comportements de consommation particuliers.
*   **Indicatrice de groupes de classes :** Imaginez que vous analysiez le traffic sur un site internet et que vous possédiez une variable appelée traffic_source qui vous indique la source de laquelle est issue votre traffic. Vous pourriez créer une variable indicatrice qui vous précise lorsque les visiteurs du site sont issus d’une source payante comme “facebook ads” ou “google adwords”.
    6. Variables composées

Ce type de features correspond à l’association de plusieurs variables existante ensemble grâce à des opérations comme la somme, la différence, le produit ou le quotient. Souvent en data science l’union fait la force et le fait de créer de nouvelles variables qui sont composée ainsi de variables existante peut permettre à un modèle de prédiction de prendre en compte de l’information qu’il ne parvenait pas à comprendre jusqu’alors.

_*NB : Cela dit, il n’est pas recommandé de créer ainsi des variables de manière automatique grâce à une boucle pour toutes les variables disponibles dans votre dataset, cela fera exploser le nombres de features et nombre d’entre eux ne seront pas nécessairement très utiles pour votre modèle._



*   **Somme de deux variables :** Mettons que vous souhaitiez prédire le revenu à partir de données de ventes historique. Si vous avez à votre disposition les ventes de stylos bleus et noirs (sales_blue_pens, sales_black_pens) vous pourriez les sommer afin de créer une variable représentant les ventes totales (sales_pens)
*   **Différence de deux variables :** Imaginons que vous vous intéressiez à l’immobilier et que vous disposiez de la date de construction (house_built_date) d’une maison ainsi que de sa date de vente (house_sales_date). On peut calculer la différence de ces deux dates afin d’obtenir l’âge de la maison lors de sa vente (house_age_at_sales).
*   **Produit de deux variables :** Si vous testez un nouveau prix sur un site marchand, vous pouvez par exemple multiplier ce prix par une variable qui indique le statut de conversion d’une visite de la page produit en achat et ainsi obtenir une variable de revenu.
*   **Quotient de deux variables :** Si vous avez en votre possession un dataset concernant des campagnes marketing avec des variables donnant le nombre de clicks n_clisks et le nombre d’impressions de la campagne n_impressions. Vous pouvez diviser le nombre de clicks par le nombre d’impressions afin de pouvoir comparer le click_through_rate pour l’ensemble des campagnes.
*   **Utilisez les fonctions usuelles :** Il arrive régulièrement que le lien entre votre variables cibles et vos variables explicatives ne soit pas linéaire, il est donc souvent intéressant de visualiser ensemble dans un graphe la variable cible ainsi que les variables explicatives afin de découvrir quelle fonction usuelle (polynômes, log, exp etc…) est susceptible de représenter le mieux possible le lien qui existe potentiellement entre les deux.
    7. Représentation des variables

Cette nouvelle méthode peut sembler simple mais peut s’avérer très utile, elle consiste à observer la même variable sous différentes formes afin d’en extraire le maximum d’information.

Vos données ne seront pas toujours présentées sous leur forme idéale. Certaines d’entre elles peuvent apporter de l’information très utile en revêtant une forme différente :



*   **Les dates et les Temps :** Mettons que vous ayez à votre disposition une variable purchase_datetime. Il est fort probable que le fait de traduire cette variable en terme de jour de la semaine permette d’apporter une information pertinente étant donné que certains commerces marchent mieux certains jours de la semaine.
*   **Transformez les variables quantitatives en variables qualitatives :** Il est parfois très utile de transformer certaines variables quantitatives en variables qualitatives ordinales, par exemple on peut transformer l’âge en catégories comme ‘0-18’, ‘19-25’, ‘26-35’ etc… qui correspondent à différentes période clés de la vie d’individus, ou bien de regrouper les revenus par tranches d’imposition.
*   **Regrouper les classes peu représentées :** Il arrive régulièrement que certaines modalités d’une variable qualitative soit très peu représentées dans le dataset, lorsque cela se produit il peut être utile de regrouper ces modalités ensemble sous le label générique “other”. La logique derrière ceci est qu’il n’est pas très utile pour la modélisation et l’analyse que tous les individus se trouvent dans la même classes, il n’est pas utile non plus que certaines classes contiennent trop peu d’individus.
*   **Création de dummy variables :** Il est parfois nécessaire pour utiliser certains algorithme de machine learning (comme les Bernouillis Naive Bayes) de transformer une variable catégorique en une collection de dummy variables représentant chacune des modalités de la dite variable. (Pensez à grouper les modalités très peu représentées sous un label ‘other’ avant de faire ceci).
    8. Données externes

L’apport de données issues d’une source extérieure peut mener aux meilleurs résultats en termes de performance, par exemple, une des stratégies adoptées par les fonds d’investissements afin de prédire la valeur de certains titres financiers est d’utiliser plusieurs sources de données financières.

De nombreux problèmes de machine learning peuvent hautement bénéficier d’un apport de données externes, voici quelques examples:



*   **Séries temporelles :** L’avantage principale des séries temporelles est qu’on a besoin uniquement de la date associée à chaque observation afin d’apporter une source secondaire de données.
*   **External API’s :** De nombreuses API peuvent vous aider à des nouveaux features, par exemple, l’API [Microsoft Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) permet de trouver le nombre de visages présents dans une image.
*   **Geolocalisation :** Lorsqu’on possède des données géolocalisées, ou qu’on dispose d’une adresse postale, il est commode de trouver des données qui caractérisent ce lieu et d’en faire des variables à l’aide d’un autre [dataset](http://www.pitneybowes.com/us/data/demographic-data.html).
*   **Source annexe des même données :** Il arrive que certaines données puissent être récoltées de plusieurs manières, par exemple une campagne de publicité sur Facebook peut être suivie grâce à l’outil d’analyse de Facebook, mais aussi Google Analytics ou d’autres logiciels tiers. Chaque source peut potentiellement remonter une information qu’une autre ne montre pas et elles pourraient être, à ce titre, complémentaires.
    9. Error Analysis (Post-modélisation)

La dernière technique de création de variables que nous verrons ensemble s’appelle l’analyse de l’erreur (error analysis). Cette technique ne peut s’appliquer qu’une fois qu’on a entraîné un premier modèle.

Ce terme fait référence à l’analyse des observations que les modèle n’a pas réussi à bien classer (dans le cadre d’un modèle de classification) ou des observations pour lesquelles l’erreur de prédiction est très grande (dans le cas d’une régression).

Les conclusions possible de cette analyse peuvent vous mener à tenter de collecter plus de données car vous vous rendez compte que des informations essentielles manquent, vous pouvez être amenés à séparer le problème en plusieurs sous-problèmes car vous vous rendez compte que certains groupes d’observations ont des comportement trop différents pour être efficacement modélisés ensemble. Vous pouvez tenter de créer de nouvelles variables afin de réduire les erreurs que vous observez, dans ce cas une analyse poussée des observations à fortes erreurs est nécessaire afin de comprendre pourquoi votre modèle échoue. Voilà une méthodologie afin d'appréhender l’analyse de l'erreur :



*   **Commencez par analyser les grandes erreurs :** L’analyse de l’erreur est un processus manuel. Vous n’aurez cependant pas le temps d’analyser chaque observation. C’est pour cette raison qu’il est recommandé d’analyser en priorité les observations pour lesquelles votre modèle commet les erreurs les plus importantes.
*   **Segmentez par classes :** Une autre technique est de segmenter les observations grâce à une variable ou un groupe de variables bien choisis et des critères souvent dictés par l’expérience métier que vous aurez acquis ou qu’on vous donnera dans un secteur précis.
*   **Apprentissage non supervisé :** Si vous n’avez pas les connaissances métier ou l’expertise nécessaire pour segmenter les observations efficacement, vous pouvez faire appel à des techniques d’apprentissage non-supervisé afin de mettre en lumière certains schémas dans les données. Il n’est pas recommandé d’utiliser les clusters ainsi créés comme variable explicative pour entraîner le prochain modèle, mais il vous faciliteront la tâche pour différencier certains groupes d’observations similaires. Souvenez-vous que le but est de comprendre pourquoi le modèle n’a pas réussi à comprendre ces obsevrations.
*   **Demandez à des collègues ou des experts du domaine d’étude :** Il est très fréquent que les data scientists travaillent dans des industries ou des domaines d’expertises dans lesquels leur expérience est limité, c’est de plus en plus le cas étant donné que la collecte, le traitement, l’analyse et la modélisation des données devient monnaie courante dans tous les domaines. C’est pourquoi il est toujours utile de demander à des collègues data scientists ou des experts d’un domaine précis de vous orienter dans vos recherches.


## Conclusion

Comme  vous pouvez le constater, il existe de nombreuses manière de créer de nouvelles variables, nous en avons abordé quelques unes, mais les possibilités sont quasiment infinies!

Si vous deviez retenir l’essentiel, de bonnes variables :



*   Peuvent être calculées pour de nouvelles observations ajoutées à votre base
*   Peuvent être expliquées simplement
*   Doivent potentiellement posséder un pouvoir de prédiction pour la variable cible, ne soyez pas tentés de créer des variables par obligation
*   Sont fondées sur une expertise du domaine d’étude ou une analyse descriptive du dataset
*   Ne touchez jamais à la variable cible, si cette dernière intervient de quelque façon dans vos nouvelles variables, c’est de la triche et de toute manière vous ne pourrez pas les variables ainsi créée pour prédire à partir de nouvelles observations pour lesquelles la variable cible ne serait pas renseignée.

Pour terminer, ne vous inquiétez pas si tout ceci semble démesuré pour le moment, vous deviendrez meilleur à ce jeu de création de variables avec le temps, la pratique, l’expérience et avec l’aide de vos paires!
