## Machine learning supervisé


### Arbre aléatoire et Random Forest



## Qu’est ce que vous apprendrez dans ce cours ?

Ce cours va être très orienté pratique, le but est de vous faire comprendre les principes théoriques des arbres de décision, qui permettent d’établir des règles successives permettant de classer des observations ou de faire des régressions. Et vous allez pour la première fois dans ce cours apprendre à coder un algorithme de machine learning du début à la fin afin que vous puissiez voir et comprendre se qui se cache derrière les fonctions bien pratiques de python.

Dans un second temps vous apprendrez le principe du bagging qu’on illustrera grâce à la mise en pratique d’un modèle de forêt aléatoire ou random forest.


## Random Forest (régression et classification)

Les random forest (en français, forêts d’arbres aléatoires) s’inscrivent dans le champ des méthodes de partitionnement récursif, qu’on connait plutôt sous l’acronyme CART (Classification And Regression Tree). On parle de classification lorsque la variable cible est qualitative (catégorielle), cas que nous traiterons dans un second temps. Ici nous nous intéressons au Regression Trees qui interviennent dans le cas d’une variable cible quantitative. Leur avantage réside dans leur représentation graphique aisément lisible. L’arbre est composé de trois types d’éléments :



*   La racine, où réside l’ensemble des données d’apprentissage.
*   Les noeuds/branches, qui représente les points à partir de la racine où les données sont séparées en deux groupes selon un critère lié aux variables explicatives.
*   Les feuilles, qui sont les noeuds terminaux de l’arbre et auxquels sont associés un valeur dans le cas où ***Y*** est quantitative et une classe lorsque ***Y*** est qualitative.

Ainsi à partir de la racine on défini un noeud qui divise l’ensemble des données selon un critère lié à une variable explicative, pour chacune des deux branches ainsi créées on répète le même procédé, et ainsi de suite jusqu’à ce qu’aucune division ne satisfasse le critère de construction d’un noeud et on définit alors un noeud terminal ou feuille.


![decision_tree](https://drive.google.com/uc?export=view&id=1TRyOAoMAkQ7kq1Hx3Zn7H66RqX2W0sGr)

Voilà un exemple d’arbre aléatoire avec en haut la racine et la première division et l’enchaînement des branches, jusqu’aux feuilles. On constate d’ailleurs immédiatement l’aspect très clair et visuel des arbres aléatoires.



1. Construction d’un arbre aléatoire
    1. Principe général

L’algorithme de construction de l’arbre aléatoire se structure de la façon suivante :



*   Initialisation : On considère la racine comme l’ensemble des données de la base d’apprentissage.
*   Pour chaque ensemble/sous-ensemble, on définit un noeud :
    *   On sélectionne une variable explicative ***X*** et on définit un critère de coupure, un seuil si ***X*** est quantitative, ou un partage en groupes de modalités si ***X*** est qualitative.
    *   On marque le noeud comme terminal si aucun critère de division n’est satisfaisant, et on lui associe une valeur ou une classe selon la nature de ***Y***.
*   On interrompt la construction de l’arbre lorsque tous les noeuds sont terminaux.

Afin de mener à son terme cet algorithme, nous avons besoin de plusieurs choses :



1. Un critère de sélection de la meilleure division
2. Une règle pour définir si un noeud est terminal
3. Une méthode pour assigner à chaque feuille une valeur ou une classe
    2. Critère de division
        1. Admissibilité

Un noeud est **admissible** si les branches qui en découlent portent des noeuds non vide (c’est à dire qu’au moins une observation appartient à chacun des noeuds enfant). Pour un noeud parent contenant ***M*** observations il existe ***M - 1*** divisions admissibles si la variables sélectionnée pour la division est quantitative ou qualitative ordinale, et <img src="https://latex.codecogs.com/svg.latex?\Large&space;2^{m-1}-1" /> divisions admissibles si la variable selectionnée est nominale.

Afin de sélectionner la meilleure division admissible, on construit une fonction **d’hétérogénéité** qui présente deux propriétés remarquables :



*   Elle vaut zéro lorsque tous les individus appartiennent à la même modalité ou présentent la même valeur de ***Y***.
*   Elle est maximale lorsque les valeurs de ***Y*** sont équiréparties dans le noeud.

On cherche donc la division qui minimise la somme des hétérogénéités des noeuds enfants.



        2. Critère d’arrêt

Un noeud donné sera terminal lorsqu’il est homogène, c’est à dire que toutes les observations dans le noeud présente la même valeur ou la même modalité de ***Y***, lorsqu’il n’existe plus de divisions admissibles, ou bien lorsque le nombre d’observations dans le noeud est inférieur à une valeur définie à l’avance, en général de l’ordre de quelques unités.



        3. Y quantitative

Dans le cas de la régression, l’hétérogénéité du noeud ***k*** s’écrit de la manière suivante :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;H_k=\frac{1}{Card(k)}\cdot\sum_{i\in{k}}(y_i-\underline{y_k})^2" />


Card(k) parfois aussi noté ***#(k)*** ou encore ***|k|*** est le nombre d’éléments dans le noeud ***k***, et <img src="https://latex.codecogs.com/svg.latex?\Large&space;\underline{y_k}" /> est la moyenne des valeurs de ***Y*** parmi les observations du noeud ***k***. Ce qui fait la variance du noeud ***k***. La division retenue est celle pour laquelle : <img src="https://latex.codecogs.com/svg.latex?\Large&space;H_{kG}+H_{kD}" /> la somme de l’hétérogénéité de la branche gauche et de la branche droite.



        4. Y qualitative

Soit ***Y*** une variable qualitative à ***m*** modalités ou catégories numérotées de 1 à m. La fonction d’hétérogénéité privilégiée la plupart du temps est la concentration de GINI:



<img src="https://latex.codecogs.com/svg.latex?\Large&space;H_k=\sum_{i=1}^{m}p_{k}^{i}\cdot(1-p_{k}^{i})" />



Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;p_{k}^{i}" /> est la proportion de la classe i de ***Y*** dans le noeud ***k***.



    3. Elagage de l’arbre

On a vu précédemment avec les modèles LASSO et RIDGE qu’un risque important dans tout problème d’apprentissage supervisé est celui du sur-apprentissage. Le critère d’arrêt défini pour la construction de l’arbre est souvent propice au sur-apprentissage puisqu’il est très probables que la plupart des feuilles de l’arbre ne contiennent que quelques observations. Ainsi l’arbre de décision tel quel sera très instable, son biais est quasi-nul voir nul par définition, il dépend très fortement des observations de la base d’apprentissage et sera potentiellement peu généralisable aux données de la base de test.

Le problème est donc de trouver un arbre intermédiaire qui vérifie un compromis biais variance intéressant pour les besoins de l’estimation de ***Y***. Le nombre de sous-arbres malheureusement est souvent très élevé c’est pourquoi on suit en général la méthode de Breiman, qui consiste à construire une suite emboîtée de sous-arbres (chaque arbre de la suite est un un sous-arbre de l’arbre précédent). Et de choisir parmi cette suite, l’arbre optimal selon un critère de généralisation.



        5. Construction 	de la suite emboîtée d’arbres

Soit ***A*** un arbre, <img src="https://latex.codecogs.com/svg.latex?\Large&space;K_{A}" /> le nombres de ses feuilles ou noeuds terminaux, qu’on appellera la complexité de l’arbre ***A***.

La **qualité d’ajustement** de l’arbre est mesurée par :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;H(A)=\sum_{k=1}^{k_A}H_{k}" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;H_k" /> est l’hétérogénéité du noeud ***k***.

La construction repose sur une pénalisation de l’arbre indexée sur sa complexité :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;C(A)=H(A)+\gamma\cdot{k_A}" />



Pour γ = 0, <img src="https://latex.codecogs.com/svg.latex?\Large&space;A_{max}=A_{K_A}" /> minimise ***C(A)***. En faisant croître γ la division de <img src="https://latex.codecogs.com/svg.latex?\Large&space;A_{K_A}" /> qui améliore le moins ***H(A)*** devra être supprimée afin d’optimiser ***C(A)***, car <img src="https://latex.codecogs.com/svg.latex?\Large&space;C(A_{K_{A}-1})-C(A_{K_{A}})=H_{K_A}-\gamma>0" />. Ce procédé permet bien de créer une suite emboîtée d’arbres puisque pour construire l’arbre suivant on lui retire un noeud.

Une fois la suite construite, on peut sélectionner celui qui minimise l’erreur de prédiction sur la **base de validation** (base de test).



    4. Remarques générales
*   L’algorithme a tendance à favoriser la sélection de variables explicatives avec beaucoup de modalités, il convient donc de transformer les variables explicatives qualitatives en fusionnant les modalités par groupes cohérents pour éviter le sur-apprentissage.
*   Les arbres de décision ne requièrent pas d’hypothèses particulières sur les distributions des variables et sont bien adaptés aux situations où les variables explicatives sont nombreuses puisque la sélection des variables fait partie de l’algorithme d’optimisation.
*   La recherche d’une division dépendant uniquement de la position relative des valeurs des variables explicatives quantitatives, l’algorithme résiste donc aux valeurs atypiques et au distributions de valeurs asymétriques.
*   La structure hiérarchique de l’arbre (les divisions se font une par une) favorise la propagation de l’erreur engendrée par une division à tous les noeuds enfants. Les arbres de décisions peuvent donc passer à côté d’un optimum global et donc de la vraie fonction de classification ou de régression qui lie les variables explicatives à la variable cible.
*   Dans le cas de la régression, le résultat de l’arbre est une fonction étagée, toutes les observations d’une même feuille prendront la même valeur estimée de ***Y***

. Si la vraie fonction présente des propriété de régularité (par exemple un polynôme ou une droite affine), ces propriétés ne seront pas conservées par le modèle d’arbre aléatoire.
2. Random Forest (Forêt d’arbres aléatoire) plutôt à inclure dans le chapitre sur le boosting?

Comme son nom l’indique, la random forest n’est rien de plus qu’un ensemble d’arbres aléatoire qu’on va faire coopérer afin d’obtenir de meilleurs résultats de régression ou de classification.



    5. Principe du Bagging

Le principe du Bagging est très simple. Soit ***Y*** la variable cible, liée aux variables explicatives <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,...,X_p" /> par une fonction ***f*** telle que <img src="https://latex.codecogs.com/svg.latex?\Large&space;Y=f(X)+\epsilon" /> et ***n*** le nombre d’observations. En tirant ***B*** échantillons indépendants <img src="https://latex.codecogs.com/svg.latex?\Large&space;\{Z_b\}_{b\in[[1,B]]}" /> à partir de l’ensemble des observations, la prévision agrégée donnée par les ***B*** modèles qui découlent des ***B*** échantillons s’écrit :



*   ***Y*** quantitative : le modèle agrégé est la moyenne des fonctions estimées par les modèles, la moyenne des valeurs de ***Y*** pour une observation donnée..



<img src="https://latex.codecogs.com/svg.latex?\Large&space;\hat{f}_B(.)=\frac{1}{B}\sum_{b=1}^{B}\hat{f}_{z_b}(.)" />





*   ***Y*** qualitative : le modèle agrégé est le vote majoritaire parmi les fonctions estimées par les modèles, la modalité de ***Y*** la plus représentée parmi les réponses des différents modèles à une observation donnée.



<img src="https://latex.codecogs.com/svg.latex?\Large&space;\hat{f}_B(.)=arg\max_{i}Card\{b|\hat{f}_B(.)=j\}" />



La principale difficulté du bagging réside dans le fait de construire ***B***

 échantillons indépendants, en effet, à moins de disposer d’une base de données contenant un très grand nombre d’observations, il est difficile de respecter cette contrainte dans la plupart des cas.



    6. Bootstrap

Le Bootstrapping est un procédé qui permet d’augmenter artificiellement le nombre d’observation d’un échantillon de données sans pour autant modifier la distribution des variables présentes dans le jeu de données. Le principe est simple, on dispose d’un jeu de données contenant ***n*** observations, pour créer un échantillon de taille ***m*** on tire avec remise ***m*** observations parmi le jeu de données original, et chaque observation du jeu de données original a <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{1}{n}" /> chance d’être tiré (c’est un tirage avec remise équiprobable). L’équiprobabilité du tirage est essentielle afin que la loi de distribution de l’échantillon soit la même que celle de la base initiale.



    7. Random Forest

La première idée derrière les random forest est d’effectuer un bagging de plusieurs arbres aléatoires. Plusieurs élagages des arbres ainsi construits sont possible :



*   On peut conserver les arbres complets et éventuellement limiter le nombre minimum d’observations au niveau des noeuds terminaux.
*   Conserver au plus ***q*** feuilles ou limiter la profondeur de l’arbre à ***q*** niveaux de noeuds.
*   Adopter la méthode vue plus haut pour un arbre seul, c’est à dire construire l’arbre complet puis élaguer par validation croisée.

En général on retiendra la première stratégie, car elle représente un bon compromis entre qualité d’estimation et quantité de calculs. Chaque arbre ainsi construit aura un biais très faible et une grande variance, cependant le fait d’agréger les modèles entre eux participe justement à réduire cette variance. Cet algorithme est très simple à mettre en place, ce qui est un grand avantage, cependant le nombre de modèles à calculer avant que l’erreur de test (appelée aussi erreur de validation) se stabilise peut être très important. Le modèle final sera volumineux en terme d’espace disque car il est nécessaire de stocker la structure complète de tous les arbres pour pouvoir faire des prévisions. Enfin la multiplication du nombre d’arbres participants au modèle rend plus difficile, voir impossible l’interprétation du modèle comme cela était possible avec un seul arbre.

La seconde idée consiste à améliorer la méthode du bagging afin de créer des random forest s’appuyant sur des échantillons de données les plus “indépendants” possible. Non seulement le hasard intervient lors de la sélection des observations lors de la construction des échantillons d’apprentissage, mais on fera également intervenir le hasard dans le choix des variables explicatives retenues pour chaque échantillon sur lequel on construira un arbre aléatoire.

Ce double hasard de sélection des observations et des variables explicatives a plusieurs avantages : il permet de s’approcher de l’hypothèse d’indépendance des échantillons, il réduit le nombre de calculs à effectuer pour le construction de chaque arbre et il réduit les risques d’erreurs liés à d’éventuelles corrélations entre variables explicatives.

Dernière remarque, soit ***Y*** la variable cible et <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,...X_p" /> les ***p*** variables explicatives à notre disposition, en général le nombre de variables que l’on conservera par arbre pour une classification est <img src="https://latex.codecogs.com/svg.latex?\Large&space;\sqrt{p}" /> et ***p/3*** pour une régression.



    8. Interprétation

Le fait d’agréger les modèles pour produire la prédiction finale rend difficile l’interprétation directe du modèle, cependant deux méthodes sont utilisées en pratique afin d’évaluer l’importance de chacune des variables pour la prédiction.



        6. Mean decrease Accuracy

Cette méthode consiste à permuter de manière aléatoire les valeurs d’une variables explicatives, on mesure ensuite la différence entre l’erreur de validation pré et post-permutation, plus elle est élevée, plus on considère la variable en question importante pour la prévision de la variable cible.



        7. Mean decrease Gini

Cette méthode permet d’évaluer l’importance d’une variable au niveau d’un noeud, elle mesure la décroissance de la fonction d’hétérogénéité si on utilise la variables explicative utilisée pour le noeud par celle que l’on souhaite évaluer. L’importance générale de la variable est alors une sommes des décroissance d’hétérogénéité mesurées, pondérée par le nombres d’observation à chaque noeud.
