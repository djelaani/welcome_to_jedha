
## Moteurs de recommandations

## Les moteurs de recommandations

Tout comme les moteurs de recherche, les moteurs de recommandation font partie de la famille des algorithmes de filtrage d’informations. Le filtrage d’informations consiste à utiliser des données d’interaction entre des utilisateurs et des items pour produire un modèle capable d’ordonner ces items selon l'intérêt qu’ils peuvent avoir pour un utilisateur donné. Dans le cas plus spécifique des moteurs de recommandation, il s’agit de proposer à un utilisateur les produits qu’il est le plus susceptible de consommer ou d’apprécier.

La création d’un moteur de recommandation est l’un des cas d’usage les plus courant du machine learning. Cependant, en terme de business, il n’a d'intérêt que pour un certains type d’entreprises. En effet, celles-ci doivent effectuer leur activité au moins en partie sur internet, et elles doivent par ailleurs disposer de suffisamment de produits et d’utilisateurs pour que la recommandation soit utile et pertinente. C’est donc principalement des entreprises présentent dans les secteurs du commerces en ligne et des médias qui font usage de la recommandation. L'intérêt pour ces dernières est principalement d'accroître la consommation de produits sur leur plateforme et d’améliorer l’expérience utilisateur.

Pour prendre quelques exemple dans le cas du commerce en ligne on peut citer Amazon, Ebay et Rakuten dont les moteurs de recommandation peuvent parfois vous inciter à acheter des produits supplémentaire mais aussi vous aider dans vos recherches. Si vous allez sur la page d’un produit sur Amazon vous verrez un peu plus bas plusieurs bandeaux proposant des recommandation se basant sur des moteurs différents. Sur la page de l’Iphone 8 on peut peut trouver entre autre :



*   Un bandeau de recommandation reposant sur un moteur qui propose les produits qui ont souvent été acheté avec l’iphone 8. Celui-ci à pour but de vous faire ajouter dans votre panier un ou des accessoires qui ont souvents été considéré comme complémentaire par les acheteur de l’iphone 8.


![](https://drive.google.com/uc?export=view&id=1kSwOhwG7c_eKurlrZC59q6Y-EXDrJx49)


*   Un bandeau de recommandation reposant sur un moteur qui propose les produits qui ont souvent été vu par les utilisateurs qui ont vu la page de l’iphone 8. Comme vous pouvez l’imaginer ce moteurs est moins sélectif que le précédent car le fait de voir la page d’un produit est un événement moins rare que le fait d’en acheter un. Ceux qui ont vu la page de l’iphone 8 ont pu ensuite allez sur les pages de produits complémentaires ou bien les pages de produits concurrents. Ce moteur vous permettra donc également de faciliter votre recherche en vous proposant des alternatives auxquelles vous seriez susceptible de vous intéresser.


![](https://drive.google.com/uc?export=view&id=1VHYhDfVk-iPJNk70uUNJ1noNIonYZ_Fq)


Dans le secteur des médias, de nombreuses plateformes de diffusion de contenu écrit, de musique et de vidéos font usage d’un moteur de recommandations, parfois même de plusieurs à l'instar d’Amazon.


## Les principales méthodes

Il existe principalement deux types de méthodes qui permettent d’élaborer des moteurs de recommandation, le filtrage basé sur le contenu et le filtrage collaboratif. Chacune des ces méthodes à ses avantages et ses inconvénients et il n’est pas rare qu’un moteur repose sur une combinaison des ces deux dernières.


### Le filtrage basé sur le contenu

Le filtrage basé sur le contenu est une forme de recommandation qui s’appui sur les caractéristiques intrinsèques des items consommés. Autrement dit, pour un utilisateur donné, on va recommander des produits dont les caractéristiques sont similaires à ceux qu’il consomme d’habitude.

Si l’on prend l’exemple d’une plateforme de musique en streaming comme Deezer, un moteur de recommandation basé sur le contenu va vous recommander du contenu proches de ceux que vous consommez habituellement en terme de genre, d’année de production, de longueur et sans doute de nombreux autres attributs. Durant la phase d’entraînement, l’algorithme va pondérer l’importance de ces différents attributs pour s’assurer d'effectuer une recommandation pertinente.

Ce type de recommandation ne peut fonctionner que dans la mesure où l’on dispose d’un minimum d’informations sur les produits que l’on cherche à recommander.


### Le filtrage collaboratif

Le filtrage collaboratif repose sur une approche totalement différente du filtrage basé sur le contenu. En effet la recommandation ne va plus s’appuyer sur les caractéristiques des produits mais plutôt sur qui les consomme. Pour un utilisateur donné on va donc recommander les contenus qui ont été consommés par des personnes qui lui ressemble. La notion de ressemblance se base ici sur l’historique de consommation des utilisateurs.

Pour reprendre l’exemple de Deezer, un moteur comme celui que nous venons de décrire vous proposera des musiques qu’écoutent ceux qui ont les mêmes goût que vous. L’idée est que si ces derniers apprécient une musique que vous n’avez jamais écouté alors  vous l'apprécierez aussi en l’écoutant.

Contrairement au filtrage basé sur le contenu cette méthode ne nécessite pas de disposer d'informations sur les caractéristiques des produits recommandés, seul l’historique des interactions entre utilisateurs et produit sert de base à l'entraînement de l'algorithme.


## Les principes de l’Alternating Least Square (ALS)

Nous allons maintenant nous intéresser à un algorithme de filtrage collaboratif très couramment utilisé, l’Alternanting Least Square. Avant de comprendre comment cet algorithme fonctionne revenons sur la formulation du problème que nous cherchons à résoudre.


### Formulation du problème

Le filtrage collaboratif va toujours s’appuyer sur un matrice d'interaction entres les utilisateurs et les produits. Ces interactions peuvent représenter des choses différentes selon les choix vous aurez fais, il pourrait s’agir de la visite d’une page, d’un achat ou bien de la notation d’un produit. Dans tous les cas le principe reste le même.

Voici ceux à quoi pourrait ressembler une matrice d'interaction utilisateur / produit pour une plateforme comme Netflix.


![](https://drive.google.com/uc?export=view&id=1sogsultG5MqqGHmPC5BWSk_UiJbKp2WT)


Comme vous pouvez le constater une interaction entre un film et un utilisateur peut prendre trois valeurs différentes  :



*   1 signifie que le film a été proposé à l’utilisateur et qu’il a cliqué dessus pour le visionner
*   0 signifie que le film a été proposé à l’utilisateur et qu’il n’a pas cliqué dessus
*   ? signifie que le film n’a jamais été proposé à l’utilisateur et donc on ne sait pas s’il aurait cliqué dessus

Le principe du filtrage collaboratif est d’utiliser les informations sur les interactions qui ont eu lieu (les 0 et les 1) pour combler les trous de cette matrice, c’est à dire remplacer chaque ? par la probabilité que l’utilisateur clique sur la vidéo pour la visionner si elle lui était proposée. Grâce à cela le moteur peut associer pour tout utilisateur la liste des vidéos que ne lui ont jamais été proposées et qu’il aurait le plus de chance de vouloir regarder.

De façon similaire on pourrait, comme cela a été évoqué, s'intéresser à un autre type d’interaction tel que la notation d’un film. On aurait dans ce cas une matrice similaire à celle-ci.


![](https://drive.google.com/uc?export=view&id=1dlfsi4LixcWLKr7Si9E84LKzVx-bVROm)


Cette fois-ci il y a davantage de valeurs possibles:



*   Soit une note comprise entre 0 et 5
*   Soit un ? pour un film que l’utilisateur n’a pas noté

Le mécanique restera ici la même que dans le cas précédent, sauf qu’au lieu d’estimer la probabilité que l’utilisateur clique sur le film si on lui recommande, on estime la note qu’il serait susceptible de mettre s’il l’avais visionné. Le moteur pourra ensuite proposer à l’utilisateur une liste de film ordonnée selon l'estimation de cette note (dans un cas réel on aurait très certainement retiré de cette liste les films qu’il aurait éventuellement vu sans attribuer de note).


### Fonctionnement de l’algorithme

L’ALS est un algorithme de filtrage collaboratif qui offre une solution relativement simple pour construire un moteur de recommandation en estimant la valeur probable que pourrait prendre une interaction qui n’a pas encore eu lieu.

Pour estimer ces valeurs, qui permettent de compléter la matrice d’interaction (I), on va décomposer cette dernière en 2 matrices de taille plus petite. L’une sera associé aux profils des utilisateurs (U), et l’autre aux profils des produits (P). Les matrices U et P ont un hyper paramètre en commun (k) qui détermine le nombre de variables latentes qu’elles possèdent.

Les variables latente correspondent à un encodage de l’information qui résulte des interactions entre utilisateur et produit. Vous pouvez faire l’analogie avec certaines méthodes de réduction de dimensions tel que l’ACP, les variables latente joue ici un rôle similaire aux composantes. Ici k est égale à 3, la matrice U offre ainsi une représentation de chaque utilisateur à l’aide de trois variables numériques, la matrice P joue le même rôle pour les produits.


![](https://drive.google.com/uc?export=view&id=1XT-Rn1rF8IYHubudIDajL6NPNs8WgAoc)


Bien entendu nous ne connaissons pas les matrices U et P et nous allons donc devoir les estimer. Pour cela rappelons que l’équation que nous cherchons à résoudre est la suivante :


![](https://drive.google.com/uc?export=view&id=1IqbdAJRrEbSxOtYrukQf5h1MXWKIWvX5)


La multiplication de U et P va nous permettre de reconstruire la matrice I en attribuant une valeur à chacune des interactions, y compris celles qui n’ont jamais eu lieu (les ?). Comme dans tout problème de machine learning supervisé on va estimer les paramètres du modèle (les matrices U et P) en cherchant à minimiser une fonction de coût qui sera égale à la somme des écarts entre la valeur d’une interaction connue et le produit des vecteurs utilisateur et produit associés à cette interaction.



Par exemple l’interaction User 1 / Film 1 a pour valeur 1, le coût pour cette interaction sera donc calculé comme ceci :



![](https://drive.google.com/uc?export=view&id=1PkRi8fTCKv3HZrHeIFSvbZK7b2fXMknp)

![](https://drive.google.com/open?id=1PkRi8fTCKv3HZrHeIFSvbZK7b2fXMknp)


soit


![](https://drive.google.com/uc?export=view&id=1HMKNRA_i8tYOsYVIcifPTB2aIM4ZFUep)



De façon globale la fonction le coût peut être formulé de la façon suivante :



![](https://drive.google.com/uc?export=view&id=1ayAQKZ_nKlU8ojrWoC63cIkMydK-9zhR)


ou plus simplement


![](https://drive.google.com/uc?export=view&id=1dkrP9_Ssm6xcXj-YMowbxdr2eviouV2G)



La somme s’effectue sur les ***(i,j) observés***, c’est à dire les interactions de la matrice I dont on connaît la valeur.

Vous pourriez faire l’analogie avec la fonction de coût d’une régression linéaire qui s’y apparente fortement. On va de la même manière rechercher les valeurs des matrices U et P qui minimisent cette fonction de coût. Cependant le problème est en réalité ici bien plus complexe que dans le cas de la régression linéaire. En effet dans une régression linéaire on cherche à résoudre une équation de la forme AX = Y où seul le vecteur de coefficient A doit être estimé, X et Y étant des valeurs connues. Dans le cas de l’ALS on ne connaît que la matrice I et on doit estimer U et P.


![](https://drive.google.com/uc?export=view&id=1oldFTTwErZzseOyoW5w9IAHjmcRiyXGX)


De ce fait la fonction de coût que nous cherchons à optimiser (I - UP), est non convexe. Bien qu’il soit possible d’effectuer une descente de gradient pour trouver une solution approximative cela nécessiterait un grand nombre d’itération et l'entraînement du modèle pourrait donc s’avérer extrêmement lent.

En revanche, si après avoir initialisé aléatoirement les valeurs de U et P, nous traitons les valeurs de P comme des constantes (de façon analogue au X dans la régression linéaire) alors la fonction de coût, qui ne dépend plus que de U, devient convexe. On peut alors aisément trouver les valeurs de U qui minimise la fonction de coût étant donné les matrices P et I. On va ensuite à nouveau effectuer une optimisation de la fonction de coût en considérant cette fois-ci les valeurs de U comme constantes et en cherchant les valeurs de P qui minimise cette dernière étant donné les matrices U et I.

Au lieu d’estimer simultanément U et P on procède donc en deux temps, on fixe P et on estime U puis on fixe U et on estime P. On répète ce processus jusqu’à ce que les valeurs de U et P finissent par converger. C’est cette approche qui est communément appelé Alternating Least Square.

Voici une description plus formelle de l’algorithme:



1. Initialisation aléatoire de U et P
2. Répéter jusqu'à convergence :
    1. Pour tous les utilisateurs

<img src="https://latex.codecogs.com/svg.latex?\Large&space;u_i" />:

![](https://drive.google.com/uc?export=view&id=1A1alel8fcFoYACbPFHa3JjsNbKB4zLXq)

    2. Pour tous les produits

<img src="https://latex.codecogs.com/svg.latex?\Large&space;p_i" /> :


![](https://drive.google.com/uc?export=view&id=1u1J1vx3wDjisejhjB5j0jHWPuMUtmQns)


## Quelques liens pour aller plus loin

**How do you build a “People who bought this also bought that”-style recommendation engine**

[https://datasciencemadesimpler.wordpress.com/tag/alternating-least-squares/](https://datasciencemadesimpler.wordpress.com/tag/alternating-least-squares/)

**Stanford CME 323: Distributed Algorithms and Optimization, Spring 2015**

[http://stanford.edu/~rezab/classes/cme323/S15/notes/lec14.pdf](http://stanford.edu/~rezab/classes/cme323/S15/notes/lec14.pdf)



## L'ALS dans Spark


[TOC]



## Chargement des données

Afin de découvrir comment effectuer une ALS dans Spark, nous allons charger un jeu de données avec des notations d’utilisateur sur différentes catégories de produits. Nous allons donc nous baser sur ces notes pour recommander des catégories de produits aux utilisateurs.


![](https://drive.google.com/uc?export=view&id=1fw7P8tJP-ancYnxKgLvimhimB7bnO2wO)


## Preprocessing

Comme vous avez pu le constater sur le screenshot précédent, Spark a par défaut considéré que vos column sont de type String. Or, comme pour tous les autres algorithme de MLLib il est nécessaire que vos données soient de type numérique, il va donc falloir les convertir.

Par ailleurs, pour faire une ALS nous avons uniquement besoin d’un identifiant d’utilisateurs, d’un identifiant d’item (ici l’item est une catégorie de produit)  et d’une notation de l’item par l’utilisateur. Nous pouvons donc nous séparer de la colonne reviews.


![](https://drive.google.com/uc?export=view&id=12RjQb7Qh006HwbmRgneGFgyr3Tc3-27Q)


## Entrainement du modèle

Dans le cas présent nous n’avons davantage de pré processing et l’utilisation d’un pipeline se révèle donc inutile. Vous allez donc voir que l'entraînement de l’ALS est relativement simple et ressemble fortement à ce que nous avons vu dans le cours précédent. Voici les différentes étapes que réalise le code ci-dessous :



*   Séparation des données en ensemble d'entraînement et de test
*   Création d’un objet de type ALS en renseignant les colonnes d’identifiants de users, d’items et les notations. Le pramètre coldStartStrategy=”drop” permet tout simplement de ne pas faire de prédictions pour des users ou des items sur lequel le modèle n’aurait pas été entraîné, dans le cas contraire cela fausserait le calcul de l’erreur.
*   Création d’un objet de type evaluator pour avoir une mesure de l’erreur de notre modèle (ici le RMSE). On doit également renseigner la colonne avec la notation (stars) et celle avec les prédictions (par défaut Spark nomme cette colonne prediction)
*   Création d’un objet de ParamGridBuilder pour construire les combinaisons de paramètres que nous allons tester durant la cross validation


![](https://drive.google.com/uc?export=view&id=1C6esXkh-5lbDZBdKV6lVi6_1qUsxacGJ)


Maintenant que tous les objets nécessaires ont été défini on peut faire la cross validation de la façon suivante :


![](https://drive.google.com/uc?export=view&id=1Dxb3-W2yXu3-5toIokkn-D6YR1gMZZoW)


La méthode fit de l’objet CrossValidator va nous renvoyer le modèle entraîné avec la meilleure combinaison de paramètres.


## Evaluation

Pour évaluer le modèle sur l’ensemble de test, il faut dans un premier temps générer les prédiction sur celui-ci puis utiliser la méthode evaluate de l’objet evaluator en passant les prédictions en paramètre.


![](https://drive.google.com/uc?export=view&id=1cvxVXyyHlWtWGzuFIIhTaq5GhBNzveTY)


![](https://drive.google.com/uc?export=view&id=1JjQAFL5bRBMetwofCUDSryI6U4NVufxB)


## Utilisation du modèle

L’ALS dans Spark offre certaine fonction très pratique pour pouvoir utiliser le moteur de recommandation.

Cependant notre objet model n’implement pas ces fonctionnalités lui-même car il est de type CrossValidator et il peut donc être utilisé pour entraîner n’importe quel type de modèle supervisé.  

Pour utiliser ces fonctionnalités il faut d’abord accéder à l’attribut bestModel de notre objet model. En faisant model.bestModel on obtient donc un objet de type ALS qui implémente deux fonctions intéressantes : recommendForAllUsers et recommendForAllItems.

Pour recommander pour chaque users les 10 catégories de produit qu’il est le plus susceptible d’apprécier on peut faire :


![](https://drive.google.com/uc?export=view&id=18e_Twm_yZFOwObsP1d3NUS4zg1UsFslS)


Pour recommander pour chaque catégorie les 10 users qui sont le plus susceptible de l’apprécier on peut faire :

<![](https://drive.google.com/uc?export=view&id=1twI3gaRcWw2-iAYzDoIJ003UPI7O4ayv)
