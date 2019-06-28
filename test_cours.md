# Deep Learning - Introduction aux réseaux de neurones


## Ce que vous apprendrez dans ce cours

Ce cours introduit le machine learning avancé, aujourd’hui nous apprendrons ce que sont les réseaux de neurones simples, et puisque ces modèles de cette famille sont souvent voilés de mystère et d’incompréhension, nous coderons ensemble de A à Z notre premier réseau de neurones !


## Réseaux de neurones

### Introduction

Les réseaux de neurones artificiels ont fait leur apparition dans les années 1950 dans les travaux des neurologues Warren McCulloch et Walter Pitts, qui furent les premiers à définir un modèle imitant le fonctionnement d’un neurone dans un système nerveux. Ils appelèrent ce modèle _neurone formel_, c’est un modèle mathématiques doté d’une _fonction de transfert_ qui permet de transformer les données qu’il reçoit en entrée en un résultat à sa sortie selon des règles précises définie lors de la spécification du modèle.

Depuis cette première introduction, et en grande partie grâce aux progrès effectués dans les domaine du cloud computing, du calcul distribué et l’amélioration de la vitesse de calcul des ordinateurs, les modèles construits à partir des réseaux de neurones ont permis des avancées phénoménales dans divers domaine comme le traitement du signal, le traitement du langage naturel, l’analyse d’images, l’intelligence artificielle, et bien d’autres encore.



### Perceptron simple

Commençons par un définition formelle : le perceptron est un modèle d’apprentissage supervisé linéaire de classification binaire. C’est à dire que c’est un modèle qui apprend à partir d’exemples déjà résolu, qui utilise une combinaison linéaire des variables explicatives qu’il reçoit en entrée pour apporter une réponse binaire au problème donnée (0 ou 1, ou encore VRAI ou FAUX). C’est une définition très proche en somme de la définition de la régression logistique qui est aussi un modèle linéaire de classification binaire.

Le perceptron est donc définit par une fonction de la forme suivante :

![](https://drive.google.com/uc?export=view&id=1Pcaa8ysT7RbVk1NaUTYRu9-EUD-6TYe3)



Dans cette formule, ```x = (x1, ..., xp)``` l’ensemble des variables explicatives fournies pour apprendre le modèle, ```w = (w1, ..., wp)``` sont les poids attribués à chaque variable explicative que l’on doit optimiser pour répondre le mieux possible au problème de classification binaire et ```b``` est le seuil à partir duquel la réponse du modèle doit être ```1``` ou ```0```.

Pour illustrer le fonctionnement du perceptron, nous présentons la figure suivante :


![](https://drive.google.com/uc?export=view&id=1OHYMYC5vcLSWhwlxNUcnttyA5iHTbw5G)



A chaque itération de l’algorithme du perceptron, on sélectionne la première observation et ainsi de suite, on multiplie la valeur de chaque variable explicative pour cette observation par les poids initialisés comme de petits nombres réels aléatoires, on les additionne pour former une combinaison linéaire des variables explicatives. On applique ensuite la fonction ```f``` qui compare la combinaison linéaire avec la valeur de ```b```. On compare ensuite la sortie ```o``` ainsi obtenue avec la véritable valeur de la variable cible ```y``` et on met à jour la valeur des poids grâce à la formule suivante :


![](https://drive.google.com/uc?export=view&id=1p_dZw8BcM4DVC4yY6AOTFhqzwqE7VZ1V)



Où ```r``` est le taux d’apprentissage du perceptron, qui permet la mise à jour des poids. On choisit en général le taux d’apprentissage relativement petit par rapport aux valeurs des variables explicatives afin de se rapprocher de la valeur optimale du poids sans toutefois la dépasser. Si on choisit un taux d’apprentissage trop élevé, on risque de dépasser la valeur optimale du poids qui va osciller indéfiniment autour de sa valeur optimale.

Notez qu’on met à jour les poids à chaque observation, non pas comme dans d’autres algorithme en prenant en compte l’erreur globale du modèle. A chaque fois que l’ensemble des observations est passé par le perceptron, on calcule l’erreur globale du modèle, et on arrête si l’erreur est descendue en dessous d’une valeur qu’on a défini à l’avance.



### Neurone formel

Les réseaux de neurones sont composés de neurones, nous allons maintenant le fonctionnement d’un neurone formel inscrit dans une structure de réseau, qui est très similaire au fonctionnement d’un perceptron simple.


![](https://drive.google.com/uc?export=view&id=1nWoIGRG9sT4I4DVFvKRCB2tpjWsQzNqN)



Un neurone inclus dans une structure de réseau fonctionne de la manière exposée ci-dessus :



*   En entrée du neurone, on a un certain nombre de valeurs d’inputs ```i₁, ..., ip```


*   Les inputs rentrent dans le neurone définis par la zone bleutée, chaque entrée et multipliée par un poids ```w₁j, ..., wpj``` déterminé spécifiquement pour ce neurone d’indice ```j```.

*   Les entrées affectées des poids passent par une fonction de combinaison appelée ici ```Σ``` car le plus souvent la fonction de combinaison est une simple somme.
*   A la sortie de la fonction de combinaison, on obtient un scalaire, c’est à dire un nombre réel. On applique à ce nombre réel une fonction d’activation ```Φ```, qui peut être choisie parmi un éventail de fonctions différentes dont nous discuterons ultérieurement.
*   La sortie de la fonction d’activation peut être comparée à un seuil ```θj``` et donner ainsi la sortie du neurone ```o_j``` définie par ```1``` si  ```Φ ( Σ(i₁ w_1j + ... + i_p * w_pj) ) > θj```
 et ```0``` sinon.

### Structure d’un réseau de neurones

Un réseau de neurones est en général une collection de neurones formels, organisés par couches. Les neurones de la couche d’entrée prennent comme valeurs d’entrée les variables explicatives choisies pour le modèle. Les couches suivantes dans le réseau prennent comme entrées les sorties de la couche précédente. A la sortie du réseau, une couche de sortie produit un output unique que le réseau tente de rendre le plus proche possible de la variable cible ```y```. Pour plus de clarté, nous présentons ci-dessous une figure représentant la structure générale d’un réseau de neurones.

![](https://drive.google.com/uc?export=view&id=1c5Z4MU7tfSVTcWt1ne181aQVfeJ18ae3)



On observe en entrée les variables explicatives, qui sont amenées vers les neurones de la couche d’entrée, puis successivement à travers les autres couches du réseaux, jusqu’à la couche de sortie que l’on compare avec la valeur de la variable cible. La comparaison entre la variable cible et la sortie du réseau de neurones est appelé la fonction de coût, ou loss function, concept que nous avons précédemment abordé lors des cours sur le machine learning supervisé.

Quand on y pense, le réseau de neurones n’est rien d’autre qu’une fonction très compliquée qui transforme les entrée en une sortie ou des sorties et dont les nombreux paramètres sont les poids affectés à chaque neurone. La représentation graphique n’est qu’une manière de formaliser le modèle et de rendre sa compréhension plus simple.


### Algorithme de rétropropagation de l’erreur

Nous avons vu comment un réseau de neurones transforme les entrées en sortie. A l’état initial, tous les poids sont choisis aléatoirement, il est donc très peu probable que les réponses que donnent le réseau soient bonnes. C’est pourquoi on procède à des mises à jour successives de ces poids qu’on appelle algorithme de rétropropagation de l’erreur. Cet algorithme sélectionne successivement chaque observation parmi les données d’entraînement et calcule la réponse du réseau, calcule la valeur de la fonction de coût et détermine pour chaque poids dans le réseau la mise à jour souhaitée pour minimiser l’erreur. Les mises à jours effectuées à la fin d’un cycle de l’algorithme est pour chaque poids dans le réseau la moyenne des mises à jour calculées pour chaque observation. Expliquons cela graphiquement pour plus de clarté :


![](https://drive.google.com/uc?export=view&id=1Afe1LZ-8TxZo3NrD96JQQ3kHRDkNFbo7)


Dans la figure ci-dessus, nous sommes à l’étape initiale, les poids ont été initialisé de manière aléatoire, les flèches sont de couleur bleu ou rouge selon si le poids et négatif ou positif, et la flèche est plus ou moins large selon si la valeur absolue du poids est grande ou petite. On a fait entrer une première observation dans le réseau, et calculé la sortie en fonction des poids, on obtient donc une valeur de l’erreur donnée par ```f (n₀ - y)```, on cherche à minimiser cette erreur  en faisant en sorte que ```n₀``` soit plus proche de ```y```, hors on ne peut modifier la valeur de ```n₀``` directement, on peut uniquement modifier les poids associé aux neurones du réseau. On va donc commencer par calculer la modification souhaitée pour les poids du neurone de sortie, comme indiqué par les flèches noires de la figure ci-dessus. Les neurones de la couche cachée sont aussi colorisés en fonction de leur valeur de sortie, bleu pour une valeur positive, rouge pour une valeur négative, et plus ou moins foncé pour une valeur plus ou moins grande en valeur absolue. On a donc la formule suivante :



![](https://drive.google.com/uc?export=view&id=1zu0lA0kPmX8ndkyuDXiFv6bE_Bgh2gbx)



Les poids les plus déterminants pour modifier ```n₀``` sont ceux associés aux valeurs de sortie les plus élevées en valeur absolue. On enregistre les modification souhaitées pour les poids entre la couche cachée et la couche finale et on passe à la couche suivante en s’intéressant cette fois aux modifications que l’on souhaiterait appliquer aux ```n₂,₁ , n₂,₂ , ... , n₂,₅```  :



![](https://drive.google.com/uc?export=view&id=12DRT866aGBwtGptqdzco9TDHN2sr6eJ)


Une fois que l’on sait de combien on souhaite faire varier la valeur de sortie des neurones ```n₂,₁ , n₂,₂ , ... , n₂,₅``` on va pouvoir faire varier les poids ```{w₁,₁|₂,₁ , w₁,₁|₂,₁ , w₁,₃|₂,₁} , ... , {w₁,₁|₂,₅ , w₁,₂|₂,₅ , w₁,₃|₂,₅}```

de manière à produire ces changements. Les corrections sur les poids se propagent ainsi de couches en couches, jusqu’à ce qu’on obtiennent les variations souhaitées pour chaque poids pour la première observation testée. On procède ainsi pour chacune des observations dans la base d’apprentissage, on obtient ainsi une collection de vecteurs de modifications :


![](https://drive.google.com/uc?export=view&id=1cbxam9qmZhvOxyRsfpOMM7fbppBdtVFJ)


Où ```δ⁽ⁱ⁾_j|k``` est la modification souhaitée pour l’observation ```i``` au niveau du poids entre les neurones ```j``` et ```k```. On calcule ensuite la moyenne de tous ces vecteurs de poids et on procède à la mise à jour des poids :

![](https://drive.google.com/uc?export=view&id=1-th19zjvFOKWpQ4xKiRkovYvVtLA2U7U)



On obtient ainsi un nouvel ensemble de poids qui répondra mieux au problème que le réseau tente de résoudre à partir des exemples qui lui sont donnés.


### Descente de gradient vs descente de gradient stochastique

Les étapes de la rétropropagation de l’erreur est en fait une manière d’expliquer couche par couche que l’on calcule en réalité le gradient de la fonction complexe qui transforme les entrées du réseau en sortie pour chaque observation et qu’on soustrait aux poids dans le réseau le gradient moyen ainsi calculé :

![](https://drive.google.com/uc?export=view&id=1PAj9KEkzJh8ebr5n8MYRtMahZGeXWuQb)

Où ```W^(t)``` est le vecteur des poids du réseau à l’étape ```t```,```n```, le nombre d’observations dans la base d’apprentissage, ```vecteur( ∆_w )``` est l’opérateur qui indique qu’on calcule le gradient en fonction des poids contenus dans ```W```, ```F``` est la fonction de coût complexe qui transforme les entrées du réseau en sorties et calcule l’erreur commise (c’est une fonction qui somme les contribution de chaque couche du réseau et compose ensuite par les fonctions de transfert de la couche suivante et ainsi de suite), et les ```x⁽ⁱ⁾₁, ..., x⁽ⁱ⁾p``` sont les valeurs des variables explicatives de ```1``` à ```p``` pour l’observation ```i```. Le gradient ainsi calculé est un vecteur qui possède autant de composantes que de poids dans ```W``` et qui indique la direction selon laquelle la fonction ```F``` augmente le plus en moyenne en modifiant ```W```. L’opposé du gradient moyen ![](https://drive.google.com/uc?export=view&id=1qoenJsg5iUgduIq-gIGxA9hK_xifjTyN) représente donc la direction selon laquelle ```F``` va diminuer le plus. On modifie donc le vecteur des poids en lui soustrayant le gradient, on arrive donc à une nouvelle valeur de l’erreur et une nouvelle collection de poids pour lesquels on peut calculer un nouveau gradient et ainsi de suite. Cette procédure s’appelle la descente du gradient et peut s’illustrer de la manière suivante :


![](https://drive.google.com/uc?export=view&id=14uLcXDw003AW-MO-oeNRzyx-9iMbblxQ)


La surface en trois dimension représente la valeur de la fonction de coût (selon l’axe z) en fonction des valeurs des poids (pour des raisons de représentations graphique on ne visualise que deux poids selon l’axe x et l’axe y). La première flèche blanche démarre au niveau des coordonnées des poids initiaux, elle représente l’opposé du gradient de la fonction de coût en ce point. La descente de gradient nous amène au point suivant, où l’on calcule un nouveau gradient à soustraire et on poursuit ainsi jusqu’à atteindre un point de l’espace des poids où ces derniers ne sont plus modifiés. Cette méthode permet de façon certaine de faire diminuer la valeur de la fonction de coût à chaque étape jusqu’à atteindre un minimum. Cette méthode présente cependant deux inconvénients majeurs :



*   Si la fonction de coût n’est pas convexe (c’est à dire qu’elle ne ressemble pas à une sorte de bol) et qu’elle possède des minima locaux d’une valeur supérieure au minimum global, il est possible que la descente de gradient fasse converger les poids vers un point minimum local ! Une fois arrivé à un minimum local ou global, le gradient s’annule, il n’est donc plus possible de sortir de ce point par la méthode de descente du gradient. Le choix initial des poids est donc important car il va définir la trajectoire empruntée par ces derniers dans leur espace et donc les valeurs vers lesquelle ils convergeront. Cet inconvénient est appelé l’instabilité de la méthode de descente de gradient (le fait que tous les points initiaux ne mènent pas au même point final).
*   Un autre inconvénient de cette méthode est son temps de calcul très long. En effet si on dispose de 10 variables explicatives, 20 neurones sur la couche d’entrée, 10 neurones sur la première couche cachée, 10 neurones sur la deuxième couche cachée et qu’on cherche à classer des images de chiffres manuscrits de 1 à 10 on a encore 10 neurones sur la couche de sortie. Ce qui fait que pour chaque observation on doit calculer pas moins de ```10 x 20 x 10 x 10 x 10 = 200 000``` mises à jour des poids, plus ```20 + 10 + 10 + 10 = 50``` constantes si les fonctions de transfert des neurones en utilisent. Ca n’est tout simplement pas raisonnable si l’on souhaite entraîner le modèle sur de nombreux exemples.

Heureusement, il existe une méthode qui permet de profiter des avantages de la descente de gradient, sans charger trop l’ordinateur en calculs qui ne lui permettraient pas d’avancer suffisamment vite. Cette méthode s’appelle la descente de gradient stochastique.

La descente de gradient stochastique s’apparente à une descente de gradient classique, sauf qu’au lieu de prendre les contributions de toutes les observations, on ne prendra en compte à chaque étape que les contribution d’un échantillon d’observations choisies aléatoirement. Cela permet de calculer une estimation du gradient véritable en économisant beaucoup de temps. Les poids de seront pas toujours mis à jour de manière optimale, cependant cela est compensé par le fait qu’on fera beaucoup plus de mises à jour, beaucoup plus rapidement, qui nous emmèneront en moyenne dans la bonne direction. Nous représentons schématiquement le processus de descente de gradient stochastique dans la figure ci-dessous :


![](https://drive.google.com/uc?export=view&id=1xlhxkJ2zpJHBOTXAngSKu83eN3m6RAn4)

Afin de comprendre clairement la différence entre la descente de gradient classique et la descente de gradient stochastique, on peut faire l’analogie suivante :



*   La descente de gradient classique correspond à une situation où on cherche à descendre d’une montagne et s’assurant bien précautionneusement que chaque pas que l’on prend est le pas qui nous emmènera le plus bas possible sur la montagne, ce qui prendrait un temps fou.
*   La descente de gradient stochastique correspond à la situation ou nous cherchons à descendre d’une montagne après quelques verres d’alcools, on ne marche pas très droit, il nous arrive de nous tromper de direction, ou de remonter légèrement la pente, mais en moyenne on a plutôt tendance à descendre rapidement de la montagne.

### Conclusion et explications complémentaires

Nous comprenons maintenant le fonctionnement d’un réseau de neurones artificiels dans sa globalité. On appelle souvent ce genre de modèle des modèles boîte noire, car il est en général plutôt difficile de savoir comment le réseau transforme les entrées en sorties après optimisation. Les nombreux poids sont difficiles à interpréter et il est rare en pratique que les neurones dans ce modèles remplissent des rôles qui soient compréhensibles pour notre cerveau ou qui s’apparentent au fonctionnement de nos neurones.

Pour toute explication complémentaire, je vous encourage vivement à regarder cette série de vidéos (en anglais) qui illustrent le fonctionnement d’un réseau de neurones artificiels appliqués à un problème de reconnaissance de chiffres manuscrits.

[https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
