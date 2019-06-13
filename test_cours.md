## Machine learning supervisé


### Régressions linéaires régularisées


[TOC]



##


## Qu’est ce que vous apprendrez dans ce cours

Ce cours a pour but de vous enseigner deux modèles de régressions linéaires dites régularisées. La régularisation est un principe très utilisé en statistique qui permet de contraindre les modèles à adopter certains comportements, dans le cas présent cela permet de réduire l’importance ou de supprimer des variables explicatives qui n’apportent pas d’information pertinente pour le modèle ou de faire face à des problèmes où les variables explicatives sont beaucoup plus nombreuses que le nombre d’observations dont on dispose.

Les modèles linéaires sont populaires pour estimer une variable cible continue ***Y*** qui dépend de variables explicatives <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1,X_2,...X_p" />. En général le volume d’observation (souvent noté ***n***) est grandement supérieur au nombres de variables explicatives ***p***, cependant, dans certains cas on se retrouve dans la situation inverse. On dispose d’un nombre de variables explicatives bien supérieur au nombre d’observations, c’est souvent le cas, par exemple dans le domaine des statistiques génétiques, où les ressources de temps et d’argent ne permettent pas de séquencer l’ADN de plus d’un millier d’individus en général, tandis que le nombre de gènes que compte notre ADN pour produire une protéine est d’environ 20 000! Les modèles linéaires classiques ne sont pas bien adaptés pour ce type de problème à la dimensionnalité très élevée. C’est pourquoi nous aborderons dans ce cours de nouveaux modèles linéaires qui contournent cette difficulté.


### Modèle Ridge



1. Pourquoi le modèle linéaire échoue?

Comme on l’a vu précédemment, le modèle linéaire s’écrit de la manière suivante :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_i=\beta_{0}+X_{i,1}\beta_1+...+X_{i,p}\beta_p+\epsilon_i\forall{i}\in[[1,n]]" />


Ou sous forme matricielle :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y=X^{t}\beta+\epsilon" />



Si nous avons ***p > n***, dans la première représentation il s’agit de résoudre ***n*** équations à l’aide de ***p + 1*** paramètres que sont les <img src="https://latex.codecogs.com/svg.latex?\Large&space;\beta_0,\beta_1,...,\beta_p" />, or un système d’équations avec un nombre plus élevé de paramètres que d’équations indépendantes est non déterminé et possède une infinité de solutions.

En vision matricielle, <img src="https://latex.codecogs.com/svg.latex?\Large&space;X^{t}X" /> est une matrice de dimensions ***pxp*** alors que ses lignes et colonnes sont des combinaisons linéaires issues de ***n*** vecteurs, le rang de cette matrice est donc inférieur ou égal à ***n***, elle est donc non inversible et la résolution matricielle que nous avons montré plus haut n’est plus valide.



2. Quelle solution pour palier cette difficulté ?
    1. Qu’est ce qu’une fonction de coût ?

Une **fonction de coût** est un concept qui servira énormément par la suite puisqu’il est omniprésent dans l’univers du machine learning. La fonction de coût est la quantité mathématique que l’on souhaite minimiser lors de l’optimisation d’un modèle statistique. Dans le cadre d’une régression linéaire multiple, la fonction de coût est :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;||y-X^{t}\beta||^{2}_{2}" />


qui est la norme euclidienne pour les vecteurs (c’est à dire la racine carré de la somme de ses composants au carré) au carré. De fait l’estimateur <img src="https://latex.codecogs.com/svg.latex?\Large&space;\beta" /> qui donne les coefficients du modèle est le vecteur qui minimise la fonction de coût, ce qui s’écrit mathématiquement :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\beta=arg\min_{\beta}||y-X^{t}\beta||^{2}_{2}" />


 Cette fonction de coût permet d’obtenir un estimateur peu biaisé, mais dans le cas présent et le nombre de variables explicatives, la variance est très élevée car beaucoup de paramètre ne seront pas pertinents pour l’estimation du modèle.

C’est pourquoi on introduit la notion de **pénalité, **c’est une modification qu’on apporte à la fonction de coût afin de maîtriser l’arbitrage entre **biais vs variance**.



    2. Biais vs Variance

Le biais et la variance sont deux notions omniprésentes en statistiques et particulièrement en machine learning lorsqu’on cherche à faire de l’estimation ou de la prédiction.

Considérons un problème où ***Y*** est la variable cible, ***X*** la matrice des variables explicatives et ε le terme d’erreur de moyenne 0 et de variance <img src="https://latex.codecogs.com/svg.latex?\Large&space;\Sigma" />.

On souhaite modéliser ***Y*** à l’aide des variables explicatives ***X*** et on suppose qu’il existe une fonction ***f***  qui représente la vraie relation entre ***Y*** et ***X*** telle que :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y=f(X)+\epsilon" />


A l’issue de notre travail de data scientist, nous aurons obtenu une estimation <img src="https://latex.codecogs.com/svg.latex?\Large&space;\widehat{f}" /> de la fonction ***f***. Dans ce cas l’erreur au carré moyenne (souvent notée MSE pour Mean Square Error en anglais) peut se décomposer en un terme de biais (ou écart moyen à la vrai fonction) et un terme de variance (dispersion de l’estimateur par rapport à sa moyenne). Cette décomposition s’écrit ainsi :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;E[(Y-\widehat{f})^2]=E[f-\widehat{f}]^2+E[\hat{f}^2]-E[\widehat{f}]^2+\Sigma" />


<img src="https://latex.codecogs.com/svg.latex?\Large&space;E[(Y-\widehat{f})^2]=biais^2+variance+\Sigma" />



    3. Pénalité du modèle Ridge

Le modèle Ridge est une version pénalisée du modèle linéaire multiple dont la fonction de coût est :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;||y-X^{t}\beta||^{2}_{2}+\lambda||\beta||^{2}_{2},\lambda\in\mathbb{R^{+*}}" />



Cette pénalité entraîne que toute variation des paramètres β peut avoir un impact bénéfique sur la qualité de l’estimation (au niveau du premier terme) mais participe à l’augmentation du second terme. Cela force le modèle à favoriser les paramètres associés aux variables explicatives qui contiennent réellement une information pertinente pour décrire la variable cible et à maintenir à des valeurs plus proches de zéros des paramètres associés aux variables explicatives peu pertinentes.

En terme d’arbitrage biais vs variance, le modèle Ridge se comporte de la manière suivante :



*   λ = 0 correspond au modèle linéaire, qui est non biaisé
*   Le biais augmente lorsque λ augmente
*   La variance diminue lorsque λ augmente
*   λ = ∞ correspond au modèle où tous les paramètres sont à zéros, d’où β = 0 et l’estimateur vaut 0 ou

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\underline{Y}" /> (la moyenne des valeurs de ***Y***) si on a inclus un intercept dans le modèle.


    4. Cas particulier de l’intercept

L’intercept est le paramètre <img src="https://latex.codecogs.com/svg.latex?\beta_0" /> du modèle, il n’est associé à aucune variable explicative, il représente l’estimation du niveau moyen de ***Y*** lorsque les autres variables explicatives valent 0. C’est pourquoi on ne le pénalise pas en pratique. La fonction de coût du modèle Ridge avec intercept est donc :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;||y-\beta_0-X^{t}\beta||^{2}_{2}+\lambda||\beta||^{2}_{2},\lambda\in\mathbb{R^{+*}}" />



### Modèle Lasso



1. Problème de sélection de variables en grande dimension

Le modèle Ridge, on l’a vu, est bien adapté lorsqu’une partie des variables explicatives n’est pas très informative dans le modèle, car il contracte les coefficients associés à ces variables. Cependant, dans le cas où la vraie valeur de nombreux coefficients est 0, c’est à dire que les variables explicatives auxquelles ils sont associés n’ont aucune influence sur la variable cible, le modèle Ridge donnera des résultats d’estimation corrects, mais l’interprétation du modèle est rendue plus compliquée car on ne fera pas la différence entre un coefficient qui représente une influence réelle mais faible sur la variable cible et un coefficient faible mais qui devrait être nul. C’est à dire que le modèle Ridge ne sélectionne pas les variables pertinentes.

C’est pourquoi un modèle du nom de Lasso existe, qui sélectionne les variables pertinentes et fixe à zéro les coefficients des variables parasites.



2. Le modèle Lasso
    1. Intuition

L’intuition fondamentale pour utiliser un modèle Lasso est qu’un certain nombre de variables explicatives à notre disposition n’a aucune influence sur la variable cible, et donc que les coefficients associés auraient pour vraie valeur 0 dans le modèle linéaire.

Cette intuition est caractérisée mathématiquement de la manière suivante : soit ***n*** le nombre d’observations, ***p*** le nombre de variables explicatives et ***s*** le nombres de variables explicatives pertinentes. Alors l’intuition (qu’on appelle hypothèse de **sparsité**) s’écrit de la manière suivante.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;s<<n<<p" />

On espère en sélectionnant les ***s*** variables pertinentes de se ramener dans une situation où le modèle linéaire peut s’appliquer sans difficulté.

Idéalement on souhaite trouver β tel que:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\widehat{\beta_n}=arg\min_{\beta:||\beta||_{0}\leq{s}}||Y-X^{t}\beta||^{2}_{2}" />


Cette equation signifie que <img src="https://latex.codecogs.com/svg.latex?\Large&space;\widehat{\beta_n}" /> est le vecteur qui minimise la valeur <img src="https://latex.codecogs.com/svg.latex?\Large&space;||Y-X^{t}\beta||^{2}_{2}" /> sous la contrainte que le nombre d'éléments non-nuls dans β soit au maximum ***s***.

Avec <img src="https://latex.codecogs.com/svg.latex?\Large&space;||\ ||_{0}" /> est la “norme zéro” qui compte le nombre d’éléments non nuls dans β.

Hors cette contrainte ne permet pas de faire de l’optimisation car elle ne définit pas un espace convexe. A la place, nous sommes dans l’obligation de choisir une contrainte moins forte qui permette d’obtenir une fonction de coût convexe qui reposera sur la “norme 1” <img src="https://latex.codecogs.com/svg.latex?\Large&space;||||_{1}" /> qui est défini comme la somme des valeurs absolues des composants d’un vecteur.  



    2. Estimateur Lasso

Nous introduisons ici le _Least Absolute Shrinkage and Selection Operator_ (LASSO), défini par la fonction de coût suivante :



<img src="https://latex.codecogs.com/svg.latex?\Large&space;||Y-X^{t}\beta||^{2}_{2}+\lambda||\beta||_{1}" />



Les choses importante à connaître sur le modèle LASSO sont les suivantes :



*   λ la constante de pénalisation doit être soigneusement choisie, en général les algorithme de résolution du LASSO procède à une cross-validation (dont la théorie est développée dans ce qui suit)  et calcule l’estimateur pour de nombreuses valeur de λ afin d’identifier les valeurs les plus pertinentes.
*   Plus λ est élevé, plus la solution <img src="https://latex.codecogs.com/svg.latex?\Large&space;\hat{\beta}_{LASSO}" /> sera sparse (c’est à dire contiendra peu d’élément non nuls), on augmente le biais et on diminue la variance.
*   Plus λ sera petit, plus le nombre de coefficients augmente, ceci diminue le biais du modèle mais peut augmenter dramatiquement la variance (c’est ce qu’on appelle une situation de sur-apprentissage).
*   En pratique vous découvrirez bientôt que le biais introduit par l’estimation LASSO peut être important. En fonction de vos contraintes de précision des résultats, il est possible d’utiliser LASSO pour sélectionner les meilleurs variables et ensuite estimer un modèle linéaire en conservant uniquement ces variables pour ôter le biais.
    3. Underfitting et Overfitting (sous-apprentissage et sur-apprentissage)

On a mentionné au-dessus deux notions qui s’expliquent ainsi :



*   Le sous-apprentissage est le fait qu’un modèle soit trop simple pour être une bonne estimation de la variable cible.
*   Le sur-apprentissage est le phénomène inverse, lorsqu’on construit un modèle très complexe qui adhère parfaitement aux données d’apprentissage, mais inutile en pratique car il est très improbable qu’il se généralise bien à de nouvelles données inconnues.


![under_over_fitting](https://drive.google.com/uc?export=view&id=1W3Y-X__zrkB-fOBGnVmLb0_IheOEAt05)


La figure ci-dessus représente de gauche à droite, une situation de sous-apprentissage, une situation de bonne estimation, et une situation de sur-apprentissage.
