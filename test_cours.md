## Semaine 6 : Machine learning avancé


## Deep learning



1. Réseaux de neurones
    1. Introduction


Les réseaux de neurones artificiels ont fait leur apparition dans les années 1950 dans les travaux des neurologues Warren McCulloch et Walter Pitts, qui furent les premiers à définir un modèle imitant le fonctionnement d’un neurone dans un système nerveux. Ils appelèrent ce modèle _neurone formel_, c’est un modèle mathématiques doté d’une _fonction de transfert_ qui permet de transformer les données qu’il reçoit en entrée en un résultat à sa sortie selon des règles précises définie lors de la spécification du modèle.

Depuis cette première introduction, et en grande partie grâce aux progrès effectués dans les domaine du cloud computing, du calcul distribué et l’amélioration de la vitesse de calcul des ordinateurs, les modèles construits à partir des réseaux de neurones ont permis des avancées phénoménales dans divers domaine comme le traitement du signal, le traitement du langage naturel, l’analyse d’images, l’intelligence artificielle, et bien d’autres encore.



    2. Perceptron simple

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



    3. Neurone formel

Les réseaux de neurones sont composés de neurones, nous allons maintenant le fonctionnement d’un neurone formel inscrit dans une structure de réseau, qui est très similaire au fonctionnement d’un perceptron simple.


![](https://drive.google.com/uc?export=view&id=1nWoIGRG9sT4I4DVFvKRCB2tpjWsQzNqN)


Un neurone inclus dans une structure de réseau fonctionne de la manière exposée ci-dessus :


*   En entrée du neurone, on a un certain nombre de valeurs d’inputs ```i₁, ..., ip```

*   Les inputs rentrent dans le neurone définis par la zone bleutée, chaque entrée et multipliée par un poids ```w₁j, ..., wpj``` déterminé spécifiquement pour ce neurone d’indice ```j```.

*   Les entrées affectées des poids passent par une fonction de combinaison appelée ici ```Σ``` car le plus souvent la fonction de combinaison est une simple somme.
*   A la sortie de la fonction de combinaison, on obtient un scalaire, c’est à dire un nombre réel. On applique à ce nombre réel une fonction d’activation ```Φ```, qui peut être choisie parmi un éventail de fonctions différentes dont nous discuterons ultérieurement.
*   La sortie de la fonction d’activation peut être comparée à un seuil ```θj``` et donner ainsi la sortie du neurone ```o_j``` définie par ```1``` si  ```Φ ( Σ(i₁ w_1j + ... + i_p * w_pj) ) > θj```
et ```0``` sinon.


    4. Structure d’un réseau de neurones

Un réseau de neurones est en général une collection de neurones formels, organisés par couches. Les neurones de la couche d’entrée prennent comme valeurs d’entrée les variables explicatives choisies pour le modèle. Les couches suivantes dans le réseau prennent comme entrées les sorties de la couche précédente. A la sortie du réseau, une couche de sortie produit un output unique que le réseau tente de rendre le plus proche possible de la variable cible ```y```. Pour plus de clarté, nous présentons ci-dessous une figure représentant la structure générale d’un réseau de neurones.


![](https://drive.google.com/uc?export=view&id=1c5Z4MU7tfSVTcWt1ne181aQVfeJ18ae3)


On observe en entrée les variables explicatives, qui sont amenées vers les neurones de la couche d’entrée, puis successivement à travers les autres couches du réseaux, jusqu’à la couche de sortie que l’on compare avec la valeur de la variable cible. La comparaison entre la variable cible et la sortie du réseau de neurones est appelé la fonction de coût, ou loss function, concept que nous avons précédemment abordé lors des cours sur le machine learning supervisé.

Quand on y pense, le réseau de neurones n’est rien d’autre qu’une fonction très compliquée qui transforme les entrée en une sortie ou des sorties et dont les nombreux paramètres sont les poids affectés à chaque neurone. La représentation graphique n’est qu’une manière de formaliser le modèle et de rendre sa compréhension plus simple.



    5. Algorithme de rétropropagation de l’erreur

Nous avons vu comment un réseau de neurones transforme les entrées en sortie. A l’état initial, tous les poids sont choisis aléatoirement, il est donc très peu probable que les réponses que donnent le réseau soient bonnes. C’est pourquoi on procède à des mises à jour successives de ces poids qu’on appelle algorithme de rétropropagation de l’erreur. Cet algorithme sélectionne successivement chaque observation parmi les données d’entraînement et calcule la réponse du réseau, calcule la valeur de la fonction de coût et détermine pour chaque poids dans le réseau la mise à jour souhaitée pour minimiser l’erreur. Les mises à jours effectuées à la fin d’un cycle de l’algorithme est pour chaque poids dans le réseau la moyenne des mises à jour calculées pour chaque observation. Expliquons cela graphiquement pour plus de clarté :


![](https://drive.google.com/uc?export=view&id=1Afe1LZ-8TxZo3NrD96JQQ3kHRDkNFbo7)


Dans la figure ci-dessus, nous sommes à l’étape initiale, les poids ont été initialisé de manière aléatoire, les flèches sont de couleur bleu ou rouge selon si le poids et négatif ou positif, et la flèche est plus ou moins large selon si la valeur absolue du poids est grande ou petite. On a fait entrer une première observation dans le réseau, et calculé la sortie en fonction des poids, on obtient donc une valeur de l’erreur donnée par ```f (n₀ - y)```, on cherche à minimiser cette erreur  en faisant en sorte que ```n₀``` soit plus proche de ```y```, hors on ne peut modifier la valeur de ```n₀``` directement, on peut uniquement modifier les poids associé aux neurones du réseau. On va donc commencer par calculer la modification souhaitée pour les poids du neurone de sortie, comme indiqué par les flèches noires de la figure ci-dessus. Les neurones de la couche cachée sont aussi colorisés en fonction de leur valeur de sortie, bleu pour une valeur positive, rouge pour une valeur négative, et plus ou moins foncé pour une valeur plus ou moins grande en valeur absolue. On a donc la formule suivante :


![](https://drive.google.com/uc?export=view&id=1zu0lA0kPmX8ndkyuDXiFv6bE_Bgh2gbx)


Les poids les plus déterminants pour modifier ```n₀``` sont ceux associés aux valeurs de sortie les plus élevées en valeur absolue. On enregistre les modification souhaitées pour les poids entre la couche cachée et la couche finale et on passe à la couche suivante en s’intéressant cette fois aux modifications que l’on souhaiterait appliquer aux ```n₂,₁ , n₂,₂ , ... , n₂,₅```  :



![](https://drive.google.com/uc?export=view&id=12DRT866aGBwtGptqdzco9TDHN2sr6eJ)


Une fois que l’on sait de combien on souhaite faire varier la valeur de sortie des neurones ```n₂,₁ , n₂,₂ , ... , n₂,₅``` on va pouvoir faire varier les poids ```{w₁,₁|₂,₁ , w₁,₁|₂,₁ , w₁,₃|₂,₁} , ... , {w₁,₁|₂,₅ , w₁,₂|₂,₅ , w₁,₃|₂,₅}``` de manière à produire ces changements. Les corrections sur les poids se propagent ainsi de couches en couches, jusqu’à ce qu’on obtiennent les variations souhaitées pour chaque poids pour la première observation testée. On procède ainsi pour chacune des observations dans la base d’apprentissage, on obtient ainsi une collection de vecteurs de modifications :


![](https://drive.google.com/uc?export=view&id=1cbxam9qmZhvOxyRsfpOMM7fbppBdtVFJ)


Où ```δ⁽ⁱ⁾_j|k``` est la modification souhaitée pour l’observation ```i``` au niveau du poids entre les neurones ```j``` et ```k```. On calcule ensuite la moyenne de tous ces vecteurs de poids et on procède à la mise à jour des poids :

![](https://drive.google.com/uc?export=view&id=1-th19zjvFOKWpQ4xKiRkovYvVtLA2U7U)


On obtient ainsi un nouvel ensemble de poids qui répondra mieux au problème que le réseau tente de résoudre à partir des exemples qui lui sont donnés.


    6. Descente de gradient vs descente de gradient stochastique

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

    7. Conclusion et explications complémentaires

Nous comprenons maintenant le fonctionnement d’un réseau de neurones artificiels dans sa globalité. On appelle souvent ce genre de modèle des modèles boîte noire, car il est en général plutôt difficile de savoir comment le réseau transforme les entrées en sorties après optimisation. Les nombreux poids sont difficiles à interpréter et il est rare en pratique que les neurones dans ce modèles remplissent des rôles qui soient compréhensibles pour notre cerveau ou qui s’apparentent au fonctionnement de nos neurones.

Pour toute explication complémentaire, je vous encourage vivement à regarder cette série de vidéos (en anglais) qui illustrent le fonctionnement d’un réseau de neurones artificiels appliqués à un problème de reconnaissance de chiffres manuscrits.

[https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)





2. Réseaux de neurones convolutifs

Les réseaux de neurones convolutif sont une variante des réseaux de neurones que nous avons vus précédemment et qui sont particulièrement performants pour résoudre des problèmes liés aux images ou autres objets qui ont une dimension spatiale, nous verrons ce que cela signifie en détail dans ce qui suit. Afin d’expliquer au mieux le fonctionnement de ces modèles, utilisés notamment par des entreprises comme Google pour la recherche et la reconnaissance d’image, nous utiliserons l’exemple de la reconnaissance de chiffres manuscrits.



    8. Principe général

Nous avons vu précédemment comment les neurones d’un réseau de neurones prennent comme entrée les variables explicatives qu’on lui soumet dans le cas de la couche d’entrée et les sorties des couches précédentes dans les cas de toutes les couches qui suivent. Ce qui change dans le cas des réseaux de neurones convolutifs, les entrées de chaque neurone est modifiée pour prendre en compte une dimension spatiale. Passons à l’exemple pour illustrer cette idée :


![](https://drive.google.com/uc?export=view&id=1_s27XL6-gMvUdqAZcvBhdHcTvBE4Nsss)


Dans le cas de la reconnaissance de chiffres manuscrit dans des images de 18 par 18 pixels, nous disposons de 324 variables que sont les pixels de l’image. Dans le cas d’un réseau de neurones classique, les entrées de la première couche seraient chacun des pixels affectés d’un poids pour chaque neurone de la couche d’entrée. Dans le cas d’un réseau de neurones convolutif, c’est différent, cette fois les entrées d’un neurone sur la première couche ne seront pas les pixels eux même, mais une combinaison des valeurs d’un pixel et des pixels environnant. Ceci vient de l’idée que lorsque nous identifions des objets par la vision, la propriété essentielle que nous cherchons à trouver sont les délimitations et propriétés spatiales de l’objet dans son ensemble, pas point par point jusqu’à reconstituer une image complète. Le fait de prendre en compte une zone de l’espace comme entrée et non plus un point, vise à communiquer au réseau l’importance de chercher des schémas dans l’espace pour reconnaître des images.

Dans la figure ci-dessus, chaque neurone correspond à la fonction suivante :


![](https://drive.google.com/uc?export=view&id=16VT0OtxmHrQPecpUsw5U9zZqmqdwl_rX)


Où les ```x_i,j``` représente les valeur du pixel en position ```i , j``` sur le filtre (par exemple ```x₃,₁``` est la valeur du pixel en bas à gauche du filtre), les ```w_i,j``` sont les poids ou paramètres du neurone considéré, associé au pixel correspondant, et ```b``` est le paramètre de biai calculé pour chaque neurone.

Le fait de passer ainsi une sorte de calque sur les différent pixel de l’image est ce qu’on entend par convolution lorsque l’on parle de réseau de neurones convolutifs.



    9. Arrangement spatial

Dans le cas des réseaux de neurones simples, les seuls hyper-paramètres que nous devons choisir est le nombre de couches et le nombre de neurones que l’on souhaite placer sur chaque couche. Ici d’autres hyper paramètres doivent être choisis en plus en fonction des objets que l’on souhaite faire analyser par le réseau. Prenons l’exemple des images de chiffres, les hyper paramètres à déterminer sont :



*   Profondeur : Plusieurs neurones peuvent servir à analyser la même zone de l’objet en entrée, le nombre de neurones ainsi dédié à une zone précise est appelé la profondeur d’une couche du réseau de convolution.
*   Pas du filtre : Nous devons choisir de combien de pixels la zone à explorer (ou filtre) doit bouger avant de définir une nouvelle entrée. Dans la figure précédente le pas a été choisi égal à ```i```, car on décalait le filtre d’un pixel à chaque mouvement. Plus le pas du filtre est grand, plus la sortie du neurone sera spatialement petite.
*   Dimensions du filtre : Nous devons définir les dimensions des filtres que nous souhaitons utiliser, dans le cas de notre exemple, nous avons choisi des dimensions de 3 pixels par 3 pixels.
*   Padding : Le padding consiste à rajouter des pixels autour de l’image afin qu’à la sortie d’un filtre, l’objet que l’on obtient fasse la même taille que l’objet en entrée (en l'occurrence l’image de taille 18 par 18 pixels). En effet, avec un filtre de taille 3 pixels par 3 pixels, on ne peut pas sélectionner comme centre du filtre les pixels qui forment la bordure de l’image, ce qui fera qu’à la sortie du filtre on aura non pas ```18x18``` éléments mais ```16x16``` éléments.

Nous montrons dans la figure ci-dessous ce que signifie le padding :


<table>
  <tr>
   <td>


   ![](https://drive.google.com/uc?export=view&id=1GGLejkBqaLedIG4swumHWHuwchuSOkmI)

   </td>
   <td>

   ![](https://drive.google.com/uc?export=view&id=1j_BkYZPSa6ZJjoaxoiAyPJVawlZSAlAN)

   </td>
  </tr>
</table>


Dans la figure de gauche, sans padding, les positions possibles pour le centre du filtre de taille ```3 x 3``` sont indiquées en rouge, et la zone couverte par l'ensemble des filtres est indiquée par les pointillés. A la sortie du filtre, on aura donc ```16 x 16``` éléments de sortie, ce qui donne un objet plus petit que l’image que l’on analyse entrée. Le padding revient à entourer artificiellement l’image d’une couche de pixel, épaisse d’un ou plusieurs pixel d’une valeur ```0``` de façon à ce que la sortie du filtre soit de la même taille que l’image d’entrée. Ici par exemple, la taille de padding nécessaire est de ```1```, les positions possibles des centres des filtres recouvrent maintenant toute l’image et la sortie sera de taille ```18 x 18```



    10. Connectivité locale

e système des filtres permet de réduire le nombre de paramètres que le réseau aura besoin d’optimiser au cours de son apprentissage. Si on connecte l’ensemble des pixels à chaque neurone de la couche d’entrée, alors chaque neurone comprendra ```18 x 18 = 324``` poids plus un éventuel biai à optimiser, alors qu’en utilisant un filtre de taille ```3 x 3```, chaque neurone n’est lié qu’à une petite partie de l’objet qui réduit le nombre de poids à calculer à ```3 x 3 = 9``` plus un éventuel biai.



    11. Partage de paramètre

Un exemple de réseau qui a fait grand bruit dans le monde du machine learning est celui construit par [Krizhevsky](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks) pour la reconnaissance d’image. Ce réseau prend en entrée des images de taille ```227 x 227 x 3```, ```227```pixels en hauteur et largeur et trois valeurs par pixel associées à l’intensité des trois couleurs primaires : rouge, vert et bleu.

Le réseau utilise des filtres de taille ```11 x 11```, un pas de ```4``` et pas de padding. Chaque niveau de profondeur du réseau contient donc ```(227 - 11) / 4 + 1 = 55``` filtre en largeur et le même nombre en hauteur, ce qui fait ```55 x 55``` filtres. De plus, le réseau est d’une profondeur ```K = 96```, chaque zone couverte par un filtre est donc regardé par ```96``` filtres différents.

Chaque filtre a donc ```11 x 11 x 3 = 363``` paramètres et un biai, ce qui fait que chaque couche le long de la profondeur contient ```364 x 55 x 55 = 1 101 100``` poids, ce qui en tout donne ```1 101 100 x 96 = 105 705 600``` poids à optimiser au total. Cette quantité de paramètres n’est pas un choix très judicieux à priori car non seulement le temps de calcul nécessaire pour optimiser le réseau sera très long, mais on risque de tomber rapidement dans une situation de sur-apprentissage.

Pour pallier cette difficulté, on considère l’idée suivante : si une certaine association de poids au niveau d’un filtre (donc une zone déterminée de l’image) est utile pour analyser l’image, alors cette même association de poids peut être utilisée pour analyser d’autres zones de l’image! On va donc contraindre les filtres de chaque couche le long de la profondeur à partager les même paramètres, de manière à n’avoir à déterminer que ```96``` associations de paramètres différents. Cette idée nous permet de réduire la quantité de paramètres à calculer drastiquement puisqu’il suffit d’optimiser ```96``` associations de ```11 x 11 x 3 + 1 = 364``` paramètres, soit l’équivalent d’un seul filtre. Le nombre de paramètres à optimiser devient alors ```96 ( 11 x 11 x 3 + 1) = 34 944``` ce qui est un problème beaucoup plus accessible et raisonnablement proportionné à la tâche de la reconnaissance d’image.




## Reinforcement learning

Le reinforcement learning s’est illustré récemment par la résolution de problèmes jusqu’à envisagés impossibles pour des machines. Par exemple, l’entreprise DeepMind, acquise depuis par Google a créé un modèle intelligent capable de surpasser les meilleurs joueurs de Go de la planète, alors que le jeu était considéré jusqu’alors comme bien trop complexe et vaste dans ses configuration possible pour être compris par un système informatique. La même entreprise a également entraîné un modèle capable de battre les meilleurs score mondiaux sur une collection de jeux d’arcade.

L’idée sous-jacente du reinforcement learning est la suivante : en machine learning supervisé, la machine se trouvant confrontée à des exemples résolus par les humains, voit ses performances limitée par les performances de ces mêmes humains. Par exemple, si on entraîne une machine à jouer au Go en lui donnant des exemples de parties jouées par les humains, elle pourra dans le meilleur des cas jouer aussi bien que le meilleur humain, mais jamais mieux, ses compétences ne dépasseront jamais l’exemple et le système ainsi créé sera incapable d’innover. Le reinforcement learning consiste donc à créer un système capable d’apprendre tout seul à partir des données entrantes et d’un objectif qu’on lui donne.



1. Introduction

Le processus de reinforcement learning s’apparente par bien des aspects à l’apprentissage supervisé. Prenons l’exemple d’un jeu de pong :


![](https://drive.google.com/uc?export=view&id=1pm0biZGeTSQANYyVmwm4w93C6m4aZVQI)


Les données d’entrée sont les pixels de l’image du jeu, on peut donc imaginer construire un réseau de convolution pour analyser les images issues de l’écran du jeu par exemple. La différence principale avec l’apprentissage supervisé, c’est que la réponse (variable cible) qui donne l’action que l’on doit entreprendre pour gagner le jeu (BAS ou HAUT) n’est pas connu à l’avance, on ne dispose pas d’exemples fournis par un dataset basé sur un joueur humain.

Le réseau ainsi construit qui à chaque image du jeu renvoie une probabilité de descendre BAS ou monter HAUT, s’appelle un _policy network._ La manière d’entraîner un policy network pour résoudre un problème tel que gagner le jeu de pong s’appelle le _policy gradient._



2. Policy gradient

On commence de la même manière que pour les réseaux de neurones ou réseaux de convolution avec des poids aléatoire pour chaque neurone dans le réseau. Le réseau reçoit une première image et donne une probabilité de descendre BAS ou monter UP :


![](https://drive.google.com/uc?export=view&id=1vMMl3M1G6LPxbQKMvLl7CK9rKw77QGim)


En fonction des probabilité des actions HAUT et BAS, on fait un tirage aléatoire qui donnera la réponse HAUT avec une probabilité <img src="https://latex.codecogs.com/svg.latex?\Large&space;P_{HAUT}" />
 et BAS avec une probabilité <img src="https://latex.codecogs.com/svg.latex?\Large&space;P_{BAS}" />. Cette action nous amène à un nouvel état du système, c’est à dire une nouvelle image qui sera envoyée comme entrée du réseau, cette action peut aussi entraîner une récompense, ou une punition dans le cas où le score change à l’issu de l’action et qu’une nouvelle manche commence. Nous exposons cette logique dans la figure suivante :


 ![](https://drive.google.com/uc?export=view&id=1bpYtn4u2KlEFrKlaRcSXYDHsx_3IWUjJ)


Le fait que les réponses du réseau consistent en un tirage aléatoire obéissant à une loi de probabilité donne la possibilité au modèle d’explorer de nombreuses possibilités lorsqu’il joue au jeu de Pong.

Le principe du reinforcement learning est de laisser le modèle, aussi appelé _agent,_ d’apprendre par lui-même. De fait le seul indicateur de performance que l’on renvoie au réseau est le tableau des scores de la partie, qui donne à l’agent une récompense lorsque ce dernier marque un point et une punition lorsqu’il perd le point. Le but de l’agent est d’adapter les poids de son policy network de manière à recevoir le plus de récompenses possibles.

On commence l’entraînement par policy gradient en laissant jouer l’agent tout seul, puisque l’agent entame le jeu avec des poids aléatoire, il est probable qu’il perdra la plupart des parties qu’il va jouer, cependant, de temps à autres, l’agent pourra être chanceux, marquer un point et ainsi recevoir une récompense ! L’avantage est qu’à chaque manche jouée, on peut calculer le gradient et modifier les poids en fonction. De fait, les séries d’actions qui mènent à des défaites deviendront de moins en moins probables alors que les séries d’actions qui mènent à la victoire deviendront de plus en plus probables, c’est ainsi que l’agent apprend petit à petit à jouer au jeu de Pong!

Afin d’illustrer la différence subtile entre l’apprentissage supervisé et le reinforcement learning, on peut exposer les figures suivantes :


![](https://drive.google.com/uc?export=view&id=1UOWz01SXDHA-m3W0DnwJ4k300XB89N57)


Dans le cas de l’apprentissage supervisé, à chaque action entreprise par l’agent, on sait à l’avance si c’est une bonne ou une mauvaise action, et on peut calculer le gradient et les mise à jour des poids désirées à chaque étape sans attendre le résultat final de la manche. On regarde ici les log probabilité des actions BAS et HAUT car cela simplifie les mathématiques de calcul de gradient.


![](https://drive.google.com/uc?export=view&id=1PPRRkvGIe5UuO3VY2SiSROmOgPcwOPiZ)


Dans le cas du reinforcement learning, on ne sait pas à l’avance si les actions entreprises sont bonnes ou mauvaises, on laisse donc jouer l’agent et une fois qu’on obtient une récompense (ou punition) on utilise les gradients calculés pour chaque image et on applique les mises à jour en fonction du résultat de la manche.



3. Credit assignment problem

Le credit assignment problem, ou problème d’attribution en français, est une difficulté que l’on rencontre très souvent dans des problèmes de reinforcement learning et intelligence artificielle. Comme on l’a expliqué, le policy gradient, consiste à laisser l’agent jouer au jeu de Pong, à chaque nouvelle image ou état du système on envoie une réponse et ainsi de suite. Cependant on peut voir passer un très grand nombre d’images avant d’avoir la moindre punition ou récompense. Il s’agit alors de savoir quelles actions sont à remettre en cause ou favoriser, quelles actions sont la cause du changement de score? Est ce que ce sont les actions prises juste avant le changement de score, celle prises au début, ou bien les actions choisies à l’image 20 et l’image 48?

Dans le cas du jeu de Pong, sur lequel nous nous concentrons ici, une récompense est due au fait qu’on a envoyé la balle dans une bonne trajectoire compte tenu de la configuration du jeu dans laquelle nous étions au moment de toucher la balle. Cependant la série d’actions menant à la récompense ont eu lieu bien avant le changement de score et toutes les actions prises par la suite n’ont eu aucun effet sur le score. A l’inverse, si on perd le point, on peut penser que ce sont les actions précédant immédiatement le changement de score qui ont mené à l’échec. Les enjeux de ce problème d’attribution sont intimement liés aux performances de notre système.



4. Apprentissage en détail
    1. A partir des gradients (si on écrit notre propre algorithme de rétro-propagation)

Nous allons maintenant présenter comment l’apprentissage va se faire dans le détail. On choisit d’utiliser un réseau de neurones complètement connecté (donc simple, pas de convolution ici) comprenant deux couches.

On initialise le policy network en choisissant au hasard les poids <img src="https://latex.codecogs.com/svg.latex?\Large&space;W_1" /> de la première couche et les poids <img src="https://latex.codecogs.com/svg.latex?\Large&space;W_2" /> de la seconde couche du réseau. On laisse l’agent jouer 100 partie de Pong, en supposant que chaque partie dure 200 images, on obtient au total une collection de 20 000 décisions HAUT ou BAS. Pour chacune de ces décisions on peut calculer le gradient du réseau qui nous donne la manière dont nous devrions modifier les poids dans le réseau si nous voulions encourager ces actions à l’avenir. Tout ce qu’il nous manque est le résultat de la manche qui nous indique si les actions que nous avons entreprises étaient bonnes ou mauvaises. Supposons qu’on aie remporté 12 manches et perdu 88 manches du jeu, on considérera les ```12 x 200 = 2400``` actions qui ont mené à des victoire et leur appliquer un feedback positif, c’est à dire qu’on remplace l’inconnu dans la formule du gradient pour ces actions par ```+1``` et on change les poids dans le réseau en fonction. Pour les autres ``` 88 x 200 = 17 600``` actions qui ont mené à des défaites, on remplace l’inconnue dans les gradients pré calculés par ```-1``` et on applique les changements souhaités aux poids dans le réseau. Et voilà, grâce à cette première série de mises à jour, le réseau sera plus susceptible de reproduire des actions qui ont mené à des victoires et moins susceptible d’effectuer les actions qui ont mené à des défaites.

Si on repense à la manière dont on optimise un réseau de neurone dans le cadre du machine learning supervisé, les principes sont très similaire. En faisant jouer notre agent 100 parties, on a créé des données d’entraînement contenant ``` 200 x 100 = 20 000 ``` observations qu’on a labellisées à posteriori comme bonne ou mauvaise, calculé le gradient pour chaque observation et appliqué les changements grâce à la rétropropagation de l’erreur.

On répète ensuite le même procédé avec 100 nouvelles parties, on adapte les réseau en fonction de ces nouvelles parties et on itère jusqu’à obtenir un modèle capable de gagner le jeu de Pong.

Une question légitime qu’on peut se poser est : si certaines actions d’une partie perdue étaient en réalité de bonnes actions qui ont finalement mené à une défaite car les actions suivantes étaient mauvaises, ne risque t’on pas de diminuer aussi la probabilité de ces bonnes actions? La réponse est oui, cependant, on espère qu’en moyenne sur les très nombreuses partie qu’on aura fait jouer au système, les bonnes actions seront plutôt favorisées et les mauvaises plutôt rejetées.



    2. A partir de la fonction de coût (si on utilise des packages qui gèrent entièrement la rétro-propagation)

Si on utilise des package python comme Theano ou TensorFlow, qui se chargent entièrement de la rétropropagation et pour lesquels il est difficile de modifier les gradients en fonction des résultats d’une manche (car ils ont été construits à l’origine d’un point de vue apprentissage supervisé où l’on connaît les vraies valeurs de la variable cible). Alors on va utiliser la fonction de coût afin d’optimiser notre réseau et non pas modifier le gradient.

En machine learning supervisé, le but est d’optimiser la fonction de coût suivante (de manière schématique) :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(A/B)=\sum_{i}log(p(y_i|x_i))" />

Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i,\;y_i" /> sont les données d’apprentissage, respectivement les variables explicatives et la variable cible. Pour le reinforcement learning, on procède de la manière suivante :



*   On fait comme si la valeur de la variable cible <img src="https://latex.codecogs.com/svg.latex?\Large&space;y_i" /> est l’action entreprise par l’agent lorsqu’on lui fournit l’entrée <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" />.
*   On modifie ensuite la fonction de coût en fonction du résultat de l’expérience (ici une manche de Pong).

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\sum_{i}A_{i}log(p(y_i|x_i))" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;y_i" /> est l’action entreprise par l’agent exposé à l’état du système <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> est img src="https://latex.codecogs.com/svg.latex?\Large&space;A_i" /> est appelé l’avantage. Par exemple <img src="https://latex.codecogs.com/svg.latex?\Large&space;A_i=1" /> lorsque l’action ```i``` a mené finalement à une victoire et <img src="https://latex.codecogs.com/svg.latex?\Large&space;A_i=-1" /> si l’action ***i*** a mené à une défaite.



5. AI vs Intelligence humaine

En première conclusion de cette partie sur le reinforcement learning, qui permet à une machine d’effectuer des tâches complètes à la hauteur voire surpassant parfois l’intelligence ou le talent humains, nous reviendront sur les aspects qui différencient fondamentalement les intelligences artificielles des intelligences humaines.



*   En pratique, lorsque l’on donne une tâche à effectuer à quelqu’un, on l’exprime à travers le langage. Dans le cas du reinforcement learning, nous communiquons la tâche à effectuer via une fonction de récompense.
*   Les êtres humains commencent une partie de Pong armés de beaucoup de connaissances déjà acquise, comme des notions de physique et des idées de stratégie comme “si la balle rebondit de manière à bouger rapidement selon l’axe verticale, alors il est plus difficile d’anticiper ses mouvements”. Au contraire, notre algorithme démarre de zéro, ce qui est à la fois impressionnant car il parvient à apprendre beaucoup par lui-même, mais aussi alarmant car nous n’avons aucune idée de comment lui fournir ces connaissances à priori.
*   Le policy gradient repose sur la force brut, on doit donner au système un très très grand nombre d’exemple afin que le modèle parvienne à une solution satisfaisante. Les humains au contraire, construise une sorte de stratégie après très peu d’exemple et définisse une sorte de cadre logique des possibilités à explorer.
*   Le policy gradient ne peut améliorer le modèle que si il reçoit une récompense positive, sinon les actions continueront à être plus ou moins aléatoires. Alors que les humains peuvent se projeter dans l’avenir et imaginer à partir de leur expérience des manières d’obtenir de manière non aléatoire des récompenses.

Certaines tâches sont très difficile à appréhender avec le reinforcement learning à cause des raisons exprimées au dessus. Dans certains jeux par exemple, il est très improbables de parvenir au hasard à un enchaînement d’actions qui donneront au système une récompense, il est donc quasiment impossible de lui faire apprendre des comportements approprié dans un temps limité.




## Natural Language Processing

Le Natural Language Processing, souvent abrégé par le sigle NLP et traduit en français par traitement automatique du langage naturel, est une discipline au croisement des sciences informatiques et des data science qui consiste à étudier comment interagissent les langages informatiques et celui des humains (langage naturel).



1. Exemples d’applications

Le NLP a connu un très fort essor depuis ses balbutiements dans les années 1950, et aujourd’hui, grâce à l’amélioration rapide des capacités des ordinateurs tant en termes de mémoire, de stockage et de vitesse de calcul et à l’avènement du deep learning, le nombre et la diversité des champs d’application du NLP ne cesse de grandir. Faisons une liste fortement non-exhaustive de quelques applications populaires :



*   Correction orthographique, recherche de mots clés, recherche de synonymes
*   Extraction d’information depuis des sites internets (par exemple, le prix d’un produit, des dates, des noms de personnes, d’entreprises etc…)
*   Classification :
    *   Classer des textes par niveau de difficulté
    *   Classer par sujet traité
    *   Classer en fonction du sentiment général d’un texte (positif/négatif)
*   Traduction automatisée
*   Système commandé par la parole
*   Capacité pour l’ordinateur de répondre à des questions complexes
2. Pourquoi le langage constitue un type de données très particulier ?

La plupart des données sur lesquelles travaillent d’ordinaires les data scientists sont des métriques mesurées dans le monde, comme des cours d’action, des mesures météorologiques, du signal que l’on souhaite transcrire en son. Toutes ces données sur lesquelles nous travaillons, nous espérons leur donner un sens pour en faire quelque chose d’utile, comme aider notre prise de décision quant à l’achat d’une maison, ou d’une action, prédire quel temps il fera demain, si un client serait plutôt une jeune mère ou un homme du troisième âge.

Le langage a cette particularité d’être un système spécifiquement développé par les humains pour véhiculer de l’information et du sens. Le problème n’est plus de donner un sens à des données qui prises hors contexte n’en on pas, il s’agit maintenant pour les data-scientists d’aider la machine à comprendre le sens ou les sens qui existent déjà au sein du langage qu’utilisent les humains. Le système symbolique qu’est le langage humain peut être communiqué de différentes façons, il peut être écrit, exprimé sous forme de sons, de gestes, ce qui entraîne un nouveau niveau de complexité et de richesse pour cette discipline.

Si les données étudiées dans le cadre du Natural Language Processing sont par nature très particulières, elles amènent avec un elle un certains nombre de difficultés elles aussi très particulières.



*   L’expression du langage passe par de nombreux canaux de communications à la fois, lors d’une conversation, par exemple, le langage est exprimé à la fois par les mots, l'intonation et les modulations de la voix, les mouvements du corps qui accompagnent le discours, le regard etc…
*   Le langage est un mode d’expression ambigu. Un même mot, une même phrase ou texte peuvent avoir des interprétations complètement différents, des générations de chercheurs continue de s’intéresser à des oeuvres, des citations, voie même des mots tant la richesse d’interprétation du langage est profonde et dense.
*   L’interprétation du langage dépend d’un contexte situationnel, du monde réel environnant, du sens commun et de normes culturelles et sociales

Toutes ces particularités du langage en font un sujet infiniment intéressant pour les data-scientists qui, malgré les difficultés présentées par ce dernier, ont fait et continue à faire d’immense progrès dans cette discipline.



3. Représentation du langage pour la machine

Afin d’analyser du texte avec python, il est nécessaire de travailler le format des données afin qu’elles puissent facilement être comprises, comptées, analysées par l’ordinateur. Nous allons maintenant présenter rapidement différentes techniques de traitement du texte de manière à ce qu’il puisse être utilisé pour du machine leanring :



*   Lower case (lettres minuscules) :

    Python, comme beaucoup d’autres langages informatiques, fait la distinction entre les majuscules et les minuscules “A”, n’est ainsi pas le même caractère que “a”. Par extension les mots “Apprendre” et “apprendre”, bien que compris de la même manière par nos cerveaux humains ne représentent pas les mêmes chaînes de caractère dans un langage comme python. On va donc généralement remplacer tous les caractères d’un texte par leur équivalent en minuscule avant de commencer des traitements plus avancés.

*   Retirer la ponctuation :

    Il est rare d’analyser la ponctuation en texte mining, on va donc généralement retirer toute la ponctuation afin de n’avoir plus que des mots à analyser.

*   Stop words :

    Les stop words sont tous les mots de liaison, les articles et quantificateurs très utilisés dans une langue mais qui ne sont pas en eux mêmes porteurs de sens, en français il s’agit de : “au” “car” “la” “le” etc… En anglais il s’agit par exemple de : “a” “and” “any” etc…


    On les retire en général car ils sont tellement fréquent dans les textes qu’ils empêchent de manière général les différents modèles qu’on peut utiliser de voir les mots qui caractérisent vraiment un texte.

*   Mots communs :

    Pour certaines analyses, comme lorsque l’on souhaite analyser un vocabulaire très spécifique d’un texte, on va parfois retirer certains mots très communs dans un texte en particulier ou une famille de texte. Si on cherche à classer par thèmes des textes qui décrivent l’italie, on va sans doute retirer de tous ces texte le vocabulaire trop communs afin de pouvoir mettre en valeur les différences entre ces différents textes.

*   Mots rares :

    De la même manière, des mots trop peu fréquents dans des textes peuvent s’avérer inutiles car leur liaison avec d’autres mots dans le texte pourraient s’apparenter à du bruit, on les retire aussi dans certains cas.

*   Correction des fautes de frappes :

    Dans un but d’unifier l’orthographe des mots employés dans les textes que l’on souhaite analyser, on fera souvent appel à des packages python afin de corriger les fautes de frappes et ainsi ramener à l’identiques des mots qui ne l’étaient pas à cause de leur orthographe erroné.

*   Stemming (Racinisation)

    De nombreux mots dans différentes langues sont des variations autour d’une racine commune, le processus de racinisation permet de se débarrasser d’éventuels préfixes et suffixes afin de conserver uniquement les racines communes des mots et ainsi pouvoir faire des analyses jusqu’alors impossibles.

*   Lemmisation

    La lemmisation est un procédé proche de la racinisation mais qui, au lieu de supprimer simplement les suffixes et préfixes courants, possède une connaissance suffisante du vocabulaire d’une langue afin de transformer les mots en leur racine et ainsi ne pas dénaturer le vocabulaire comme peut le faire le stemming. Par exemple, le stemming transformera “president” en “sid” alors que la lemmisation transformera “predident” en “presid”.

    1. N-grams

Souvent on ne représentera pas un texte de manière brut lorsqu’on se lance dans du text mining, ainsi on ne laissera pas l’ordinateur se débrouilla avec une chaîne de caractère de la forme :

“Le chat mange les poissons”

Au lieu de cela on va la plupart du temps représenter le texte sous forme de N-grams. Les N-grams sont une manière de décomposer le texte par groupes de ***N*** mots. Par exemple : les 1-grams ou unigrams du texte précédent sont les suivants :


<table>
  <tr>
   <td>“le”
   </td>
   <td>“chat”
   </td>
   <td>“mange”
   </td>
   <td>“les”
   </td>
   <td>“poissons”
   </td>
  </tr>
</table>


Les 2-grams de ce même texte sont :


<table>
  <tr>
   <td>“le chat”
   </td>
   <td>“chat mange”
   </td>
   <td>“mange les”
   </td>
   <td>“les poissons”
   </td>
  </tr>
</table>


Les N-grams sont des outils très pratiques pour analyser le thème général d’un texte, extraire les mots les plus importants, lier les textes entre eux, les classer.



    2. Parse trees

Les parse trees sont des outils qui permettent de décomposer des phrases simples de manière automatiques comme dans l’exemple suivant :


![](https://drive.google.com/uc?export=view&id=15yqMknQsiaqnubxCQjN4AwnlmcDWRQh1)


En anglais, par exemple, des règles grammaticales existent qui permettent de construire des phrases, par exemple une phrase peut être composée d’un groupe nominal (Noun phrase NP) suivie d’un groupe verbal (Verb phrase). On peut faire la liste de ces règles et il existe une librairie sur python (nltk) qui permet grâce à des algorithme de décomposition d’analyser des phrases simples. C’est grâce à cette technologie que les assistants personnels comme Siri (apple), Alexa (amazon) ou Cortana (microsoft) sont capables de comprendre rapidement des instructions vocales après les avoir converties en texte.

Cependant, lorsque les phrases deviennent trop complexes, ce type d’analyse ne permet d’extraire le sens de manière intelligible pour l’ordinateur, elle est plus adaptée à la compréhension du sens d’instructions courtes, précises et factuelles.



4. Analyses simples

Avant de passer à des méthodes de machine learning avancées pour la compréhension du langage, nous allons commencer par introduire des techniques très fréquemment utilisées en linguistique et en marketing quantitatifs pour extraire de l’information de données textuelles.



    1. Term frequency

La term frequency ou fréquence d’un terme et le ratio du nombre d’occurrences du terme sur le nombre de mots dans la phrase ou le texte. Par exemple dans la phrase suivante : “le chat noir mange les poissons mais ne mange pas les autres chats noirs” la table des fréquences peut s’écrire de la manière suivantes après traitement de lemmisation et suppression des stop words :


<table>
  <tr>
   <td>Term
   </td>
   <td>Occurrences
   </td>
   <td>Term Frequency
   </td>
  </tr>
  <tr>
   <td>“chat”
   </td>
   <td>2
   </td>
   <td>0.25
   </td>
  </tr>
  <tr>
   <td>“noir”
   </td>
   <td>2
   </td>
   <td>0.25
   </td>
  </tr>
  <tr>
   <td>“mange”
   </td>
   <td>2
   </td>
   <td>0.25
   </td>
  </tr>
  <tr>
   <td>“poisson”
   </td>
   <td>1
   </td>
   <td>0.125
   </td>
  </tr>
  <tr>
   <td>“autre”
   </td>
   <td>1
   </td>
   <td>0.125
   </td>
  </tr>
  <tr>
   <td><strong>Total</strong>
   </td>
   <td><strong>8</strong>
   </td>
   <td><strong>1</strong>
   </td>
  </tr>
</table>




    2. Inverse document frequency

L’idée sous-jacente si on pense à un ensemble de documents textuels que l’on souhaite classer, on conclut qu’un terme qui apparaît dans tous les documents du corpus (ou groupe de textes) n’est pas très utile pour différencier ou rapprocher entre eux les documents. La formule général de l’inverse term frequency ou IDF est la suivante :

![](https://drive.google.com/uc?export=view&id=1s5juVZzMugTAE3gcbk-PkpiGG-1eMzUO)



Où ***N*** est le nombre total de documents et ***n*** est le nombre de documents dans lequel le terme apparaît. Par exemple si l’on considère les deux documents suivants : “le chat noir mange les poissons mais ne mange pas les autres chats noirs” et “la girafe mange des feuilles grâce à son long cou, mais ne mange pas de poissons”. Si on calcule l’IDF sur ces exemples on obtient le tableau suivant :


<table>
  <tr>
   <td>Term
   </td>
   <td>Document occurences
   </td>
   <td>Document frequency
   </td>
   <td>IDF
   </td>
  </tr>
  <tr>
   <td>"chat"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
  </tr>
  <tr>
   <td>“noir”
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
  </tr>
  <tr>
   <td>“mange”
   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.3010299957</p>

   </td>
  </tr>
  <tr>
   <td>“poisson”
   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.3010299957</p>

   </td>
  </tr>
  <tr>
   <td>“autre”
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
  </tr>
  <tr>
   <td>"giraffe"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
  </tr>
  <tr>
   <td>"feuille"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
  </tr>
  <tr>
   <td>"long"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
  </tr>
  <tr>
   <td>"cou"
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
  </tr>
</table>


Plus l’IDF d’un mot est élevé, plus le mot est unique et donc représentatif d’une caractéristique particulière du document dans lequel il se trouve par rapport aux autres documents.



    3. Term frequency - Inverse document frequency

La Term frequency - inverse document frequency est la multiplication de TF et IDF, c’est un indicateur très populaire de l’importance d’un mot dans un document relativement à sa présence dans les autres documents. Par exemple si un mot est très fréquent dans un texte mais présent dans tous les autres textes, alors son importance sera moins grande qu’un terme très fréquent dans un seul document et absent des autres. Pour les exemples cités, les tf-idf s’écrivent ainsi.


<table>
  <tr>
   <td>Document
   </td>
   <td>Term
   </td>
   <td>TF
   </td>
   <td>IDF
   </td>
   <td>TF IDF
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>"chat"
   </td>
   <td><p style="text-align: right">
0.25</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1505149978</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>“noir”
   </td>
   <td><p style="text-align: right">
0.25</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1505149978</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>“mange”
   </td>
   <td><p style="text-align: right">
0.25</p>

   </td>
   <td><p style="text-align: right">
0.3010299957</p>

   </td>
   <td><p style="text-align: right">
0.07525749892</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>“poisson”
   </td>
   <td><p style="text-align: right">
0.125</p>

   </td>
   <td><p style="text-align: right">
0.3010299957</p>

   </td>
   <td><p style="text-align: right">
0.03762874946</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
1</p>

   </td>
   <td>“autre”
   </td>
   <td><p style="text-align: right">
0.125</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.07525749892</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"giraffe"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1204119983</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"mange"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.3010299957</p>

   </td>
   <td><p style="text-align: right">
0.06020599913</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"feuille"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1204119983</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"long"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1204119983</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>"cou"
   </td>
   <td><p style="text-align: right">
0.2</p>

   </td>
   <td><p style="text-align: right">
0.6020599913</p>

   </td>
   <td><p style="text-align: right">
0.1204119983</p>

   </td>
  </tr>
</table>


Ainsi on comprend que les mots les plus importants du document 1 qui le démarquent des autres documents du corpus sont “chat” et “noir”, dans les document 2 les mots “giraffe” “feuille” “long” et “cou” sont les termes les plus caractéristiques. Inversement les mots “mange” et “poisson” ont un tf-idf faible dans les deux documents. On peut donc conclure que les deux document parlent du fait de manger du poisson, mais que le document 1 se concentre sur les chats, alors que le document 2 porte sur les giraffes.



    4. Sentiment analysis

Il existe des librairies dans python comme textblob qui contiennent des listes de vocabulaire où chaque mot possède un score associé au sentiment qu’il véhicule, si ce sentiment est plutôt positif, le score sera positif, par contre si le sentiment véhiculé par le mot est négatif alors le score sera lui aussi négatif.



5. NLP avancé

De nombreux problèmes de natural language processing ont pu être résolu grâce aux progrès du deep learning dont nous avons parlé dans les séances précédentes, pour conclure ce cours sur le NLP nous allons nous intéresser à un problème particulier qui est le développement d’une machine capable de traduire automatiquement entre le français et l’anglais.
