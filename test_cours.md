
## Spark SQL


## Les différentes structures de données en Spark

Tout comme dans la librairie pandas ou dans le langage R, il existe une structure de donnée appelé Dataframe en Spark. L’objectif du Dataframe est d’intégrer les données dans un format tabulaire, c’est-à-dire avec une notion de ligne et de colonnes, pour rendre leur manipulation plus simple. Vous verrez que les dataframe Spark sont assez différent de ceux que vous connaissez avec Pandas et vous devrez par conséquent utiliser une syntaxe différente.

Avant d’étudier plus en détail les dataframes Spark nous allons d’abord voir que ce n’est pas la seule structure de données que ce framework permet d’utiliser.


### Les RDD

Le RDD (Resilient Distributed Dataset) est  la première structure de données qui fut disponible en Spark. Dans un RDD il n’y a pas de notion de colonne car il n’y a pas de schéma*, vous ne faites que manipuler des lignes avec des fonctions du type map et reduce. La manipulation des RDD est difficile et plutôt bas niveau, en l’absence de colonne vous devrez en effet parser les lignes manuellement pour en extraire des informations. Comme nous allons le voir après il y a aujourd’hui peu d'intérêt à utiliser le RDD par rapport au Dataframe.


### Les Dataframes

Les Dataframes que nous avons déjà évoqué sont apparu dans la version 1.3 de Spark. Le Dataframe vous permettra d’effectuer des transformations  avec une syntaxe plus simple et surtout avec de meilleurs performances que le RDD (voir ci dessous le temps d'exécution pour les DF versus les RDD).C’est donc sur cette structure de donnée que nous consacrerons nos efforts d’apprentissage.


![](https://drive.google.com/uc?export=view&id=1Kkd0BFyynZrUfDolCU2_IWGY7D7J04U1)


### Les Datasets

Les Datasets sont une évolution des Dataframes. Ils présentent de grands intérêts notamment celui de pouvoir combiner à la fois les traitements haut niveau que l’on peut effectuer sur les Dataframes et les traitements bas niveau sur les RDD. Cela est parfois trè utile. Cependant on ne peut utiliser le Dataset qu’en Scala ou en Java car il requière un typage statique là où python est un langage à typage dynamique (le typage d’une variable s’effectue lors de l'exécution du code alors que pour utiliser les Dataset il est nécessaire qu’il soit connu avant l'exécution)


## Quelques liens pour aller plus loin

https://databricks.com/blog/2015/08/12/from-pandas-to-apache-sparks-dataframe.html


## Prise en main de Spark SQL


## Chargement des données

Nous allons reprendre le même dataset que dans la leçon précédente pour découvrir les principales fonctionnalités de Spark SQL. Celui-ci comporte des informations sur 10 000 applications disponibles sur l’App Store. Les deux cellules ci-dessous vont permettre de déclarer le compte de stockage Azure dans l’objet SparkSession puis de charger les données dans un dataframe enregistré dans une variable appelé apple_store. Notez que nous chargeons ici le fichier au format parquet que nous avons enregistré la dernière fois.


![](https://drive.google.com/uc?export=view&id=1DsVIS02JmL-q2-EKkIe9V9HchryNDaWp)

## Sélection et filtrage

Dans cet exemple nous allons afficher un sous ensemble de nos données à l’aide des fonctions **select** et **filter**. Par rapport à une requête SQL la fonction **filter** joue le rôle du where.

La fonction **select** nous permet ici de sélectionner 4 colonnes et la fonction **filter** de ne retenir que les lignes dont la colonne prime_genre a pour valeur “Games”.

Notez que c’est un objet colonne qui est utilisé dans la fonction **filter** pour former la condition, comme le dataframe s’appel apple_store l’objet colonne de prime_genre est **F.col(“prime_genre”)**.


![](https://drive.google.com/uc?export=view&id=11ChsUB_yi3eLmkNmsBeew5Bm7eMKxuOT)


Il est bien sur possible de filtrer avec des expressions plus complex que nous venons de le faire. Par exemple pour ne garder que les lignes dont le prime_genre est différent de “Games” ou “Weather” on peut procéder comme ci-dessous.

La méthode **isin** sur un objet colonne permet de retenir toute les lignes dont la valeur est inclue dans la liste passée en argument.

L’opérateur **~** permet d’obtenir la réciproque de l'expression qui la suit, autrement dit combiné avec **isin** vous obtenez toute les lignes dont les valeurs ne sont pas comprises dans la liste passée en argument.


![](https://drive.google.com/uc?export=view&id=1-DVnaYuBjJz1ipIZCy9wsrtZPV1pmcLW)



## Opérations simples sur les colonnes

Il est assez simple d’effectuer une opération arithmétique sur uns colonne et de stocker ce résultat dans une nouvelle colonne de dataframe.

Avec la méthode **withColumn** sur le dataframe nous allons ajouter une colonne le prix en euros. **withColumn** prend deux paramètre, le nom de la nouvelle colonne et sa valeur. Pour obtenir sa valeur nous prenons l’objet colonne correspondant au prix en dollar et nous la multiplions par 0.86 pour obtenir le prix en euros.


![](https://drive.google.com/uc?export=view&id=1gVUeYXCQ0OhfvycO_NdXynShj-ZJEmfH)


On pourrait obtenir exactement le même résultat en utilisant la fonction select.

Pour cela on doit passer dans la fonction select toute les colonnes déjà présente dans le dataset, on peut faire cela avec ***[apple_store[col] for col in apple_store.columns]***. On ajoute ensuite la nouvelle colonne à la suite en utilisant la méthode alias pour lui fournir un nom :


![](https://drive.google.com/uc?export=view&id=1oBkrStMc38WHnaVSIwTIoz7p8AuWl3Bz)


Pour ajouter une valeur constante dans une colonnes on doit nécessaire passer par la fonction **lit**. En effet pour ajouter une colonne on doit fournir un objet colonne, dans le cas précédent l’expression **F.col(“price”)*0.86** renvoie un objet colonne. Si l’on souhaite simplement ajouter une colonne contenant la chaîne de caractère “Apple” pour toute les lignes on doit d’abord obtenir un objet colonne avec **lit**(“Apple”) avant de fournir cette valeur en argument dans la fonction **withColumn** ou **select**.


![](https://drive.google.com/uc?export=view&id=1dS72TMzuG11IUmFtPdg9hFcl4rdoC9DW)


On peut également effectuer une opération avec plusieurs colonnes du dataset :


![](https://drive.google.com/uc?export=view&id=1cG9MyvXL3xTl4WDDoWUXLsCl3p3HIgZW)


## Les fonctions Spark prédéfinies

Dans de nombreux cas vous aurez besoin d’effectuer des opérations plus complexe que celles que nous venons de voir. Spark SQL contient de très nombreuses fonction prédéfinies. L’exemple ci-dessous vous offre un aperçu de certaines d’entre elles sur les chaînes de caractères (pour concaténer, splitter ou tester si une chaine contient une valeur) et sur les tableaux (obtenir la taille d’un tableau, le n-ième élément ou tester s’il contient une valeur)


![](https://drive.google.com/uc?export=view&id=19EsbKzhg6y7LL--V7N97OqKwOpK7F-EF)


Pour plus de praticité vous pouvez tout à fait définir vos propre fonction en utilisant des opérations arithmétiques ou des fonctions Spark prédéfinies comme ci-dessous.

Notez que la fonction get_type renvoie un type pour la colonne tout entière ou non pas pour chaque ligne, par conséquent le type de retour est une chaîne de caractère, il faut donc l’enrobé avec la fonction **lit** pour pouvoir l’insérer dans une colonne du dataframe.


![](https://drive.google.com/uc?export=view&id=1Tih1JL03lREUOHZqUWwU57esf8eMkCej)


## Les UDF

Les fonctions que nous venons de voir s’appliquent sur des objets colonnes de Spark. Ce sont donc des fonctions différentes de celles que vous utiliseriez pour manipuler directement des objets en python. Les fonctions Spark prédéfinies permettent de faire de nombreuses choses et dans la plupart des cas il faut privilégier leur utilisation. Mais il arrive parfois que ces fonctions soient insuffisantes pour votre besoin ou que leur utilisation paraissent trop complexe.

Dans ce cas il est possible de créer des UDF (user defined fonctions) qui sont des fonctions que vous allez définir vous mêmes et qui manipule directement des objet python au lieu colonnes Spark. Cela se fait toujours en deux étapes, vous allez d’abord créer une fonction python classique puis vous allez créer l’UDF à l’aide de la fonction **udf **en passant en paramètre votre fonction python et le type de retour Spark de votre fonction, par exemple **udf(maFonctionPython, StringType())** si la fonction renvoie une chaîne de caractère.

Dans l’exemple ci-dessous nous allons simplement calculer le nombre de caractère du nom de chaque application. En python pour calculer la taille d’une chaine de caractère on utilise la fonction **len**. On va donc faire une fonction python qui va simplement renvoyer la longueur d’une chaine de caractère puis créer une UDF à partir de cette fonction :


![](https://drive.google.com/uc?export=view&id=1yogqdgOfkbyIa8KSkCWgZQK-h13cIpQl)


Notez que la fonction length ne fait rien d’autre que d'appeler **len**, on aurait donc tout aussi bien pu faire :


![](https://drive.google.com/uc?export=view&id=1Sa7HHDvpLKrlRFMOohG-_OieQVq8SevF)


Voyons maintenant une UDF qui permettrait de remplacer tout les caractères espaces par des _ dans le nom de l’application :


![](https://drive.google.com/uc?export=view&id=1lWkzGZx4YwbDYlLckMrHf1P4g77X2ZmO)


Cependant cela manque cruellement de généricité, il serait sans doute souhaitable de pouvoir passer en paramètre le caractère que nous souhaitons remplacer et son remplaçant. Cela devient un peu plus compliqué et il faut alors faire appel à une méthode appelé le currying. Sans entrer dans les détails cela va ici consister à faire une fonction que renverra elle même une autre fonction. La première fonction va prendre en paramètre le caractère que l’on souhaite remplacer et son remplaçant puis va nous renvoyer une UDF similaire à celle que venons d'utiliser, sauf que celle-ci aura été paramétré par la première fonction. Voici un exemple :


![](https://drive.google.com/uc?export=view&id=1iCBpHdUBkLd_po-7aMOK3DfuIuuBFm2u)


## Les Agrégations

Les agrégations en Spark suivent une syntaxe semblable aux agrégations avec Pandas. Dans les l’exemple ci-dessous on va agréger les données des applications par genre et calculer un ensemble de métrique à l’aide de fonctions Spark dont les noms cont assez explicites :


![](https://drive.google.com/uc?export=view&id=1QEvTrETRXy0ZvKQ1QuHb-mA55TFzlyUg)


Il est parfois utile d'agréger un ensemble d’item à l’intérieur d’une liste. Dans l’exemple suivant on va pour chaque genre construire une liste des noms d’applications qui en font partie à l’aide de la fonction d'agrégation Spark **collect_list**. Notez qu’il existe également **collect_set** qui supprime les doublons contrairement à **collect_list**.


![](https://drive.google.com/uc?export=view&id=1rtNSLe8elkqo3M4d0lT57ijLUrvsKqyn)


L’opération inverse du collect_list est une fonction appelé explode. Pour comprendre un peu mieux imaginez que l’on split le nom des applications sur le caractère espace. On obtiendrait alors pour chaque app une liste avec les mots contenus dans son nom (la colonne “words”). La fonction explode va nous permettre de créer une ligne pour chacun des mots qui se trouvent dans la liste.

Dans l'exemple ci dessous vous pouvez voir deux lignes pour l’application PAC-MAN Premium, dans la colonne “word” de la première il y a le premier mot du titre (PAC-MAN)  et sur la seconde ligne il y a le second mot du titre (Premium) :


![](https://drive.google.com/uc?export=view&id=1nz3sx3ZfxvL2vN2KLHuW7U2toPdkWwr3)


Avec les fonctions **explode** et **collect_set** nous allons par exemple très facilement pouvoir recueillir l’ensemble des mots utilisés dans les titres pour chaque genre d’application.


![](https://drive.google.com/uc?export=view&id=1XsxoCJK2RmjfWUa6KNdGHdZUoZzq_FOF)



## Les Window fonction

Les window fonction en Spark ont une syntaxe similaire au SQL. L’exemple ci-dessous permet de ranker les applications selon leur poid pour chaque genre. Autrement dit pour chaque genre l'application avec le rang 1 est celle qui est la plus lourde.

Comme en SQL il faut d’abord préciser le nom de la window fonction et fournir dans la clause over les informations de partitionnement ainsi que l’ordre. On a donc ici utilisé la fonction rank, en partitionnant le genre de l’application à l’aide de **Window.partitionBy**(“prime_rank”) et en ordonnant de façon décroissante de la taille en byte avec **orderBy**(“size_bytes”) :

![](https://drive.google.com/uc?export=view&id=1LisEYAnvShLRU6qaA42trm7QyFne9Lv3)
