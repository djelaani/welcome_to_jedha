
## Big data et calcul distribué


## Qu’est ce le Big Data ?

Le Big Data est un phénomène qui découle de la digitalisation progressive de notre société. Cette digitalisation est liée à l’omniprésence des appareils électroniques connectés à internet, que ce soit les ordinateurs, les smartphones ou les autres objets connectés. A travers leur usage nous créons en permanence de la donnée de façon volontaire, par exemple en publiant sur les réseaux sociaux, ou involontaire, car en effet tout ce que nous faisons sur un site web est inscrit dans des fichiers appelés logs (des fichiers retraçant l’ensemble des événements qui ont eu lieu comme le fait d’arriver sur une page, de cliquer, de scroller ...).

L’accroissement rapide de la quantité de données que l’on peut posséder sur les utilisateurs amène à réfléchir à la fois aux nouveaux usages que l’on peut faire de cette donnée et aux nouveaux problèmes que ces usages vont engendrer d’un point de vue technique. C’est tout cela que le Big Data désigne, de nouvelles opportunités mais aussi de nouveaux obstacles.

Pour rendre ce terme un peu plus concret  nous pouvons reprendre la définition du Big Data faite par Gartner, une entreprise spécialisé dans le conseil et la recherche. Gartner défini le Big Data avec les 3V: Volume, Variété et Vélocité.


## Les framework de calcul distribué

Les frameworks de calcul distribué sont essentiels dans l’exploitation du Big Data. Ils apportent une solution au problème de volumétrie de la donnée en rendant les traitements scalables, notion que nous allons expliciter dans un instant. Par ailleurs, même si ce n’est pas leur utilité première, ils offrent aussi pour la plupart des outils permettant de traiter des données en temps réel et dans différents formats, pour résoudre le problème de la vélocité et de variété que nous avons évoqué précédemment.


### Comprendre l’utilité des frameworks distribués

Les frameworks de calculs distribués vous permettent de créer des programmes qui peuvent s’exécuter sur un cluster. Un cluster est un ensemble de machines qui exécutent plusieurs taches en parallèle pour effectuer un traitement. Cela vous permet de ne plus être limité par la puissance de calcul d’une seule machine et donc de vous assurer que votre programme sera scalable. La scalabilité, ou le passage à l’échelle, signifie simplement que quelle que soit la volumétrie de vos données à l’avenir votre programme sera toujours en mesure de les traiter à condition qu’il y ait suffisamment de machines dans votre cluster.

C’est en effet assez différent lorsque vous faites un programme basé sur python et pandas. Pandas ne permet de faire du calcul distribué, donc si vos la volumétrie de vos données augmente et que votre machine ne permet plus d’exécuter votre programme vous devrez nécessairement en prendre une plus puissante. A un moment donné vous risquez sans doute de ne plus trouver de machines suffisamment puissantes et votre programme ne sera donc plus en mesure de s’exécuter correctement.

Le calcul distribué sur un cluster va finalement permettre de lever l’obstacle de la volumétrie dans vos traitements de données. Afin de mieux comprendre le fonctionnement du calcul distribué vous pouvez voir cela comme une forme de division du travail entre plusieurs machine. Comme vous pouvez le voir sur le schéma ci-dessous il y a une machine maître qui se charge de découper un traitement en plusieurs taches qui vont s’exécuter en parallèle sur des machines esclaves. La machine maître va ensuite récupérer et combiner les résultats de ces taches pour finaliser le traitement.



![](https://drive.google.com/uc?export=view&id=15uLJQxzxlGB5ODV_lBU2oM7TvPGxde7G)



### Les principaux frameworks de calcul distribué

Il existe aujourd’hui plusieurs frameworks de calcul distribués parmi lesquels Hadoop, Spark, Storm et Flink.

Historiquement Hadoop est le premier framework de ce type à avoir été créée, le projet démarre en 2004 et c’est seulement en 2011 que sort la première version stable. Le fonctionnement d’Hadoop repose principalement sur l’utilisation d’un algorithme appelé MapReduce pour effectuer des traitements distribué ainsi que sur un ensemble de composants logiciels nécessaires pour gérer un cluster de machine et un système stockage adaptée aux systèmes distribué (HDFS). Au moment où la première version stable d’Hadoop est annoncée c’est une véritable révolution qui laisse entrevoir de nombreuse possibilité dans l’usage de données volumineuses. Cependant il demeure encore de nombreuse barrière dans son utilisation, l’utilisation de MapReduce est extrêmement complexe car elle requiert d’écrire les programmes d’une façon totalement nouvelle et peu intuitive pour les développeurs. Par ailleurs, si le framework permet de traiter d’énorme volume, son fonctionnement souffre d’importantes latence ce qui le rend très lent en comparaison des autres frameworks que nous allons évoquer.

C’est justement pour pallier les principaux problèmes d’Hadoop que Spark a était créé en 2009 par un étudiant de Berkeley qui poursuivait son doctorat. Spark permet d’écrire des programmes qui sont à la fois plus simple à concevoir qu’avec MapReduce mais surtout bien plus rapide à exécuter (dans certains cas plus de 100 fois plus rapide, voir le graphique ci-contre pour l'exécution d’une régression logistique). La première version stable de Spark sort en 2014 et à partir de là il devient le framework que l’on choisit de façon quasi systématique pour traiter de gros volume de données.

Plus récemment d’autres frameworks de calculs distribués ont vu le jour, notamment Storm et Flink dont les premières versions stables sont respectivement apparues en 2017 et 2018. Ces deux solutions sont encore peu utilisées et n’apportent pour l’instant pas d’améliorations majeures comme ce fut le cas de Spark par rapport à Hadoop.

Le graphique ci-dessus vous aidera à vous faire une idée de la popularité actuelle de chacun des quatre frameworks que nous avons évoqués. On y voit clairement que c’est Spark qui domine, alors qu’Hadoop et Storm sont plutôt sur le déclin. Quant à Flink, il reste encore très en retrait mais cela est principalement dû à sa jeunesse.


![](https://drive.google.com/uc?export=view&id=1b4pAD7qOKkOqXQxA9Gg0PiJJWdgyGNg5)


Il faut cependant garder à l’esprit que ces frameworks n’ont pas tout réinventé, ils ont remplacé Hadoop mais ont la plupart du temps gardé les autres éléments de son écosystème, c’est à dire son système de fichier HDFS et les briques logiciels permettant de gérer des clusters de machines.

Etant donnée la domination de Spark nous ne pouvons que vous conseiller de focaliser votre apprentissage sur ce framework si vous souhaitez pouvoir travailler sur des problématiques Big Data, et c’est d’ailleurs celui que nous allons apprendre à utiliser dans ce cours.


## Présentation de Spark

Nous allons maintenant faire une rapide présentation de ce framework pour vous puissiez clairement savoir ce qu’il vous permettra de faire.

Comme le montre le schéma ci-dessous, Spark est composé de plusieurs briques et c’est d’ailleurs pour cela qu’il s’agit d’un framework et non d’une librairie.


![](https://drive.google.com/uc?export=view&id=1R0lbJD4fOev1OmVTxmn_vYaDuJBYd-3g)


Chacune de ces briques est une librairie à part entière qui vous apportera des outils pour faire des choses spécifiques :



*   Spark SQL est ce qui vous permet d’effectuer des transformations similaires à celles que vous feriez en SQL, en réalité elle remplit essentiellement la même fonction que la librairie Pandas dans un contexte distribué. Attention le fait que la librairie s’appelle Spark SQL ne signifie pas que vous allez forcément taper du code SQL pour effectuer des transformations sur vos données. En réalités vous pourrez au choix manipuler vos données avec un code pseudo SQL ou bien manipuler des Dataframe et appliquer des fonctions dessus comme vous le feriez avec Pandas. Les dataframes spark sont bien évidemment assez différents de ceux que vous connaissez avec Pandas.
*   MLlib est la librairie qui vous permet d’utiliser des algorithmes de machine learning sur des dataframes Spark. Vous pouvez également faire l’analogie entre Spark ML et scikit-learn. Malheureusement Spark ML est une librairie moins complète que cette dernière mais vous y trouverez tout de même la grande majorité des algorithmes que vous connaissez.
*   Spark streaming est une librairie permettant de traiter des flux de données alimenté en continu, notamment pour des traitements en temps réel.
*   GraphX est une librairie permettant d’effectuer des opérations de graphes de façon distribuée. L’usage de cet API est rare mais elle peut être très intéressante dans un contexte où il est nécessaire de modéliser des relations complexes entre différentes entités, par exemple les relations entre individus sur des réseaux sociaux.

Dans ce cours nous nous focaliserons sur le fonctionnement de Spark dans son ensemble et sur les librairies Spark SQL et MLlib. Bien que Spark streaming et GraphX soient également des solutions très utiles pour certains cas d’usage, ces derniers sont encore peu répandus. Il est donc préférable de reporter leur apprentissage à plus tard pour privilégier la maîtrise des composants incontournable de Spark pour un Data scientist.


## Les concepts essentiels de Spark

Avant de commencer à utiliser Spark il est important de comprendre certains concepts.


### Le partitionnement

Le partitionnement est un concept inhérent à tous les systèmes distribués.

En effet dans un système distribué plusieurs machine se répartissent le travail et par là on entend que chaque machine effectue exactement la même tâche mais sur des données différentes. Cela signifie donc que lorsque l’on charge les données à l’aide d’un framework de calcul distribué, celui-ci va d’abord commencé par découper les données en différents paquets, que l’on appel partition, puis distribuer ces paquets entre les différentes machines du cluster.

Si le principe est assez simple à comprendre c’est en réalité un problème qui peut parfois devenir complexe à gérer. En effet la plupart de temps vous n’allez trop vous soucier du partitionnement, Spark s’occupera du découpage des données et de leur distribution sur le cluster. Mais lorsque les données deviennent volumineuse il se peut que les traitements soit trop long voire même qu’ils échouent par manque de mémoire. Un mauvais partitionnement est souvent à l’origine de ce type de problème.

Pour en comprendre la raison il suffit d’imaginer une situation dans laquelle les partitions sont de tailles très déséquilibrées. Certaines machines devront traiter de petites partitions de données tandis que d’autres en traiteront de plus grosse. Bien évidemment les machines ayant de petites partitions auront finies leur traitement bien avant les autres. Le temps de traitement globale va donc ici être essentiellement déterminer par le temps nécessaire pour traiter les plus grosses partitions. Une meilleur équilibre des partitions aura sans aucun doute accéléré le traitement et évité que des machines soit inutilisée le temps que d’autres finissent leur traitement. Il est également possible qu’une partition soit de taille trop importante pour que la machine qui la traite puisse disposer de suffisamment de mémoire, dans ce cas il y aura une erreure qui empêchera le traitement global de finir.


### Les transformations et les actions

Une autre concept essentiellement en Spark est le mode d’évaluation des commandes que vous utilisez. \


Concrètement il y a deux types de choses que vous pouvez faire en Spark : Les transformations et les actions. Avant de voir plus en détail ce que sont les transformations et les actions il faut comprendre pourquoi on cherche à les différencier.

Les transformations sont toutes les opérations que vous allez effectuer sur vos données mais Spark ne va pas réellement exécuter que vous exécuterez votre code. Si nous prenons un exemple concret: Vous avez un dataset avec des informations sur différents individus venus de différents pays. Vous souhaitez simplement filtrer ce dataset pour ne garder que les individus français et enregistrer le résultat dans une variable. Pour Spark le filtrage est une transformation, donc au moment où vous allez exécuter le code permettant de filtrer le dataset et de stocker le résultat dans une variable, Spark ne va en réalité rien filtrer. Il ne fera rien d’autre que de garder en mémoire le fait que cette variable contient le produit du chargement du dataset puis de son filtrage. C’est ce qu’on appel une évaluation paresseuse (on dit plus souvent évaluation lazy), le framework à bien compris ce que vous souhaitez faire et il effectuera le filtrage du dataset uniquement quand cela sera vraiment nécessaire.

Les transformations sont en réalité évaluée au moment ou vous produisez une action. Pour reprendre notre exemple si vous souhaitez afficher le résultat du dataset filtré il faudra bien que Spark le filtre. L’affichage de la donnée est une action et il en va de même pour l’écriture du résultat dans un fichier. Autrement dit:



*   Je filtre mon dataset et je stocke le résultat dans une variable que j’appel X : Spark ne fait rien que de garder en mémoire que X correspond à mon Dataframe filtré.
*   J’affiche X : Spark filtre mon dataset et affiche X
*   J’enregistre X dans un fichier : Spark filtre à nouveau mon dataset et enregistre X

Vous devriez maintenant vous demander pourquoi on a dû filtrer le dataset deux fois. En réalité le dataset stocké dans la variable X n’a jamais été conservé en mémoire par Spark. A chaque fois que je ferais une action utilisant X l’ensemble des transformations qui ont été nécessaire pour le produire seront réévaluées. Dans notre cas il n’y a qu’un filtrage mais il y aurait aussi pu y avoir tout un tas d’autres transformations. Bien évidemment cela peut paraître très inefficient et il heureusement possible dans Spark de garder en mémoire les données que l’on va réutiliser à de multiple reprise. On pourrait alors adapter notre exemple de la façon suivante:



*   Je filtre mon dataset, je stocke le résultat dans une variable que j’appel X et je demande à Spark de garder X en mémoire : Spark ne fait rien que de garder en mémoire que X correspond à mon Dataframe filtré et qu’il devra le garder en mémoire
*   J’affiche X: Spark filtre mon dataset, l’enregistre en mémoire et affiche X
*   J’enregistre X: Spark va chercher X en mémoire et enregistre X

Certes, vous avez maintenant compris comment contourner le problème de l'évaluation paresseuse qui peut vous amener à refaire plusieurs fois les mêmes opérations inutilement. Mais il est important de comprendre que c’est en réalité une bonne chose de gérer soit même le fait de garder ou non les résultats de vos transformations en mémoire. Cela est principalement utile pour les raisons suivantes :



*   Éviter de saturer la mémoire car dans un contexte big data les traitements intermédiaire sont parfois très volumineux. Il est donc parfois nécessaire d’effectuer plusieurs fois les mêmes calculs quand l’espace disponible n’est pas suffisant pour stocker ces derniers.
*   L’évaluation partielle est parfois suffisante. Si vous filtrez le dataset mais souhaitez afficher que les dix premières lignes, Spark va effectuer le filtrage des lignes au fur et à mesure et s'arrêtera quand il pourra afficher 10 lignes correctement filtrées
*   L’optimisation des traitements. Spark va ajouter les transformations que vous faites au fur et à mesure dans un DAG (en français un Graphe Orienté Acyclique). Ce graphe va simplement représenté pour Spark l’ensemble des étapes qu’il devra effectuer en partant des données brutes pour arriver au résultat qui découle de l’ensemble des transformations que vous avez effectués. L'intérêt est ici que Spark ne va pas naïvement exécuter le code qu’on lui fournit, il va au contraire chercher à l'exécuter d’une façon optimisée en agençant comme il le pourra des opérations bas niveau qui correspondent à votre code.

Pour rester simple on peut dire que tout ce qui concerne l’affichage et l’enregistrement de la données (que ce soit dans un fichier ou une base) est une action. Quasiment tout le reste entre dans la catégorie des transformations. Vous apprendrez très rapidement dans un cadre pratique à distinguer les deux. Ce qui est difficile en revanche c’est de bien juger quelles données vous devrez garder en mémoire lorsque le programme devient complexe. Vous aurez en effet souvent trop de résultats intermédiaires pour tous les conserver, il faudra alors faire des choix avec discernement et surtout ne pas hésiter à effectuer des tests.


## Premier pas avec Spark


[TOC]



## L’objet SparkSession

L'objet SparkSession est le point d'entré de votre programme. Dans la plateforme Databricks cet objet est directement créé pour vous lors de l'utilisation d'un notebook. Vous n’aurez donc pas besoin de le créer vous-même et à ce stade il n’est pas utile d’entrer plus dans les détails, dites vous simplement que cet objet est nécessaire pour pouvoir exécuter du code sur un cluster Spark.

Vous pouvez d’ailleurs constater que cet objet est stocké dans une variable qui s'appel "spark".


![](https://drive.google.com/uc?export=view&id=1AsUnxc8Q1O5DZIZxo0vh5IjH3y3p9qHp)


Si vous vous souhaitez interagir avec un compte de stockage Azure pour pouvoir lire ou écrire des données dans un container vous devez systématiquement le déclarer dans l’objet SparkSession. Voici comment vous pouvez faire cela :


![](https://drive.google.com/uc?export=view&id=1Gd-tFRx93is1f02VHptkXfFZUww8R109)


Nous allons voir que vous aurez également besoin de cet objet pour le chargement de données.


## Chargement de données

La chargement de données est sans doute la première chose que aurez à faire dans votre programme.


### Depuis Azure

Nous allons commencer par charger des données depuis un compte de stockage Azure. Pour cela vous devrez fournir un chemin d’accès à la SparkSession qui sera toujours de la forme :

wasbs://**container**@**compte_de_stockage**.blob.core.windows.net/**chemin_relatif**

Le wasbs:// indique simplement le protocole d’accès aux données de la même manière que le https:// dans votre navigateur. Vous devrez également ajouter le suffixe .blob.core.windows.net au nom du compte de stockage.

Voyons cela avec un exemple concret. Nous allons charger des données relative à des applications disponible sur l’App Store. Ces données se situent dans le compte de stockage **jedha **(que nous avons déclaré précédemment), à l’intérieur que container **test. **Son chemin relatif à l’intérieur du container est **app-store-apple-data-set-10k-apps/AppleStore.csv**.

Voici le chemin d’accès dont la SparkSession a besoin pour pouvoir accéder aux données :

wasbs://**test**@**[jedha.blob.core.windows.net/app-store-apple-data-set-10k-apps/AppleStore.csv](http://jedha.blob.core.windows.net/app-store-apple-data-set-10k-apps/AppleStore.csv)**

Le code ci-dessous va charger ce fichier dans un DataFrame Spark qui sera stocké dans une variable “df” :


![](https://drive.google.com/uc?export=view&id=1s4zgDv5t2vAcLcbmco2qaf94HORdR2TG)


En plus de fournir le chemin d’accès vous remarquerez que nous avons également indiqué que ce fichier est au format csv, séparé par des virgules et qu’il contient le nom des colonnes à la première ligne.

Par ailleurs vous pouvez voir que le notebook Databricks affiche en dessous des cellules le nom des variables qui y ont été déclarées, en l'occurrence il n’y a ici que la variable “df”. Quand la variable est un DataFrame le notebook affiche également le nom des colonnes ainsi que leur type.


## Affichage des donnés

Pour afficher le contenu du dataframe (df) que nous venons de créer, vous pourriez être tenté de simplement taper le nom de la variable dans une cellule puis de l’exécuter. Avec Pandas cela vous aurait permis d’afficher les données mais avec Spark on obtient le résultat suivant :


![](https://drive.google.com/uc?export=view&id=1IrX6Gao4qhSCE9SJLzQDWfKyHkiMl1Os)


Ce qui s’affiche ici vous indique juste le nom et le type des colonnes du dataframe df. Cela est dû au fait que le chargement des données est une transformation et non une action, par conséquent vous n’avez donc pas réellement chargé les données et il n’est donc pas possible de les afficher.

Pour pouvoir afficher les données d’un DataFrame vous devez utiliser la méthode **show** de ce dernier :


![](https://drive.google.com/uc?export=view&id=13kbudJDTPmumlgEVA1Yo6KSHhksh58jl)


La méthode **show** est une action, elle va donc occasionnée l'exécution réelle du chargement des données nécessaires pour effectuer l’action. Notez bien que seules les premières lignes qui sont affichées dans le notebook seront réellement chargées.

Pour avoir un affichage des données plus clair vous pouvez également utiliser la fonction **display** qui est uniquement disponible dans un notebook Databricks.


![](https://drive.google.com/uc?export=view&id=1VO1A-oLqx5fR-JtQKTZOmlu7NsyB7LbR)


Il existe une méthode **describe** qui permet d’obtenir des statistiques de bases sur vos colonnes. Celle-ci vous renvoie un DataFrame, il ne s’agit donc pas d’une action. Si vous exécutez simplement **df.describe()** vous obtiendrez le résultat suivant :


![](https://drive.google.com/uc?export=view&id=1H4Hm7uf47Z88v2W1S5zQtOFpZSyxeAnh)



Faites donc plutôt :



![](https://drive.google.com/uc?export=view&id=1zhtJEWYNeEjqWApFrtqc7_--VAAEe9em)


## Sélection des colonnes

Pour afficher les colonnes du DataFrame utilisez l’attribut **columns:**


![](https://drive.google.com/uc?export=view&id=10GdAI0jUXD-IzzYXX1yEeObLcmDJOX6q)


Pour afficher les colonnes et leur types utilisez **printSchema** :


![](https://drive.google.com/uc?export=view&id=1O886kELTBBQyjU0ksSh91AtmEcZfafV-)


Pour sélectionner des colonnes utilisez la méthode **select** avant le nom des colonnes en argument :


![](https://drive.google.com/uc?export=view&id=1RDuA0qbSLug51qfta0Wql5grK0cN-1we)


Alternativement vous pouvez passer en argument les objets colonnes comme ci-dessous avec la fonction **col. **Notez que la fonction **col** se trouve dans le package **pyspark.sql.functions** auquel nous avons donné l’alias F.

![](https://drive.google.com/uc?export=view&id=1UR2D_TB8g1qJSj4-juR0jz9mq7Spq1Ea)


Cela vous sera utile quand vous aurez besoin d’effectuer des opérations sur des colonnes directement dans la fonction select, nous verrons de  nombreux exemples dans le cours suivant. Par exemple pour convertir le type d’une colonne on peut utiliser la méthode **cast** directement sur l'objet colonne. Dans le cas présent la colonne price est considérée comme étant de type String, le code ci-dessous permet de la convertir en type Double :

![](https://drive.google.com/uc?export=view&id=1gQt-zHewOZl5MHkc_yqapB1blmc69-BE)


Parmi les autres types Spark couramment utilisé il y a StringType, IntegerType, LongType, FloatType, BooleanType, DateType, ArrayType, MapType.

Encore une fois n’oubliez pas d’utiliser la fonction **display** ou la méthode **show** pour afficher le contenu du DataFrame :


![](https://drive.google.com/uc?export=view&id=1TKUd5ojezTcPPcOlmIT-XCDaxWZTplvW)


La méthode **drop** vous permettra de supprimer des colonnes :


![](https://drive.google.com/uc?export=view&id=1OmnIaJXltHQXCtxnYdzfnmepv9YhF8iw)


## Enregistrement des données


### Dans un compte Azure

L’enregistrement dans un compte s’effectue de façon similaire au chargement au chargement. Vous devez obligatoirement indiquer le chemin avec le protocole wasb. Dans cet exemple les données sont stockées au format parquet, il n’y a donc pas besoin de préciser le séparateur comme pour le csv. Il n’y a pas non plus besoin d’indiquer que l’on souhaite enregistrer le nom des colonnes car cela est obligatoire en parquet. Le mode d’enregistrement overwrite indique que l’on souhaite écrasé le fichier AppleStore.parquet s’il existe (le mode append combine les deux fichiers et le mode error lève une exception si le fichier existe).


![](https://drive.google.com/uc?export=view&id=1_vjwIFumterBcqlMesAxW3_KA3dztedm)


## Quelques liens pour aller plus loin

**Hadoop is dead, long live hadoop !**

https://blogs.gartner.com/svetlana-sicular/hadoop-is-dead-long-live-hadoop/
