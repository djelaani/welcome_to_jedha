## Machine learning avancé


### Réseau de neurones convolutif


## Ce que vous apprendrez dans ce cours

Les réseaux de neurones convolutifs sont une généralisation des réseaux de neurones simples qui sont devenus très populaires car ils sont particulièrement adapté à l’analyse des images. Nous verrons aujourd’hui de quoi ils sont fait et comment les utiliser.


### Réseaux de neurones convolutifs

Les réseaux de neurones convolutif sont une variante des réseaux de neurones que nous avons vus précédemment et qui sont particulièrement performants pour résoudre des problèmes liés aux images ou autres objets qui ont une dimension spatiale, nous verrons ce que cela signifie en détail dans ce qui suit. Afin d’expliquer au mieux le fonctionnement de ces modèles, utilisés notamment par des entreprises comme Google pour la recherche et la reconnaissance d’image, nous utiliserons l’exemple de la reconnaissance de chiffres manuscrits.



    1. Principe général

Nous avons vu précédemment comment les neurones d’un réseau de neurones prennent comme entrée les variables explicatives qu’on lui soumet dans le cas de la couche d’entrée et les sorties des couches précédentes dans les cas de toutes les couches qui suivent. Ce qui change dans le cas des réseaux de neurones convolutifs, les entrées de chaque neurone est modifiée pour prendre en compte une dimension spatiale. Passons à l’exemple pour illustrer cette idée :

![](https://drive.google.com/uc?export=view&id=1_s27XL6-gMvUdqAZcvBhdHcTvBE4Nsss)


Dans le cas de la reconnaissance de chiffres manuscrit dans des images de 18 par 18 pixels, nous disposons de 324 variables que sont les pixels de l’image. Dans le cas d’un réseau de neurones classique, les entrées de la première couche seraient chacun des pixels affectés d’un poids pour chaque neurone de la couche d’entrée. Dans le cas d’un réseau de neurones convolutif, c’est différent, cette fois les entrées d’un neurone sur la première couche ne seront pas les pixels eux même, mais une combinaison des valeurs d’un pixel et des pixels environnant. Ceci vient de l’idée que lorsque nous identifions des objets par la vision, la propriété essentielle que nous cherchons à trouver sont les délimitations et propriétés spatiales de l’objet dans son ensemble, pas point par point jusqu’à reconstituer une image complète. Le fait de prendre en compte une zone de l’espace comme entrée et non plus un point, vise à communiquer au réseau l’importance de chercher des schémas dans l’espace pour reconnaître des images.

Dans la figure ci-dessus, chaque neurone correspond à la fonction suivante :


![](https://drive.google.com/uc?export=view&id=16VT0OtxmHrQPecpUsw5U9zZqmqdwl_rX)




Où les ```x_i,j``` représente les valeur du pixel en position ```i , j``` sur le filtre (par exemple ```x₃,₁``` est la valeur du pixel en bas à gauche du filtre), les ```w_i,j``` sont les poids ou paramètres du neurone considéré, associé au pixel correspondant, et ```b``` est le paramètre de biai calculé pour chaque neurone.

Le fait de passer ainsi une sorte de calque sur les différent pixel de l’image est ce qu’on entend par convolution lorsque l’on parle de réseau de neurones convolutifs.



    2. Arrangement spatial

Dans le cas des réseaux de neurones simples, les seuls hyper-paramètres que nous devons choisir est le nombre de couches et le nombre de neurones que l’on souhaite placer sur chaque couche. Ici d’autres hyper paramètres doivent être choisis en plus en fonction des objets que l’on souhaite faire analyser par le réseau. Prenons l’exemple des images de chiffres, les hyper paramètres à déterminer sont :



*   Profondeur : Plusieurs neurones peuvent servir à analyser la même zone de l’objet en entrée, le nombre de neurones ainsi dédié à une zone précise est appelé la profondeur d’une couche du réseau de convolution.
*   Pas du filtre : Nous devons choisir de combien de pixels la zone à explorer (ou filtre) doit bouger avant de définir une nouvelle entrée. Dans la figure précédente le pas a été choisi égal à ```1```, car on décalait le filtre d’un pixel à chaque mouvement. Plus le pas du filtre est grand, plus la sortie du neurone sera spatialement petite.
*   Dimensions du filtre : Nous devons définir les dimensions des filtres que nous souhaitons utiliser, dans le cas de notre exemple, nous avons choisi des dimensions de 3 pixels par 3 pixels.
*   Padding : Le padding consiste à rajouter des pixels autour de l’image afin qu’à la sortie d’un filtre, l’objet que l’on obtient fasse la même taille que l’objet en entrée (en l'occurrence l’image de taille 18 par 18 pixels). En effet, avec un filtre de taille 3 pixels par 3 pixels, on ne peut pas sélectionner comme centre du filtre les pixels qui forment la bordure de l’image, ce qui fera qu’à la sortie du filtre on aura non pas ```18x18 ``` éléments mais ```16x16 ``` éléments.

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





    3. Connectivité locale

Le système des filtres permet de réduire le nombre de paramètres que le réseau aura besoin d’optimiser au cours de son apprentissage. Si on connecte l’ensemble des pixels à chaque neurone de la couche d’entrée, alors chaque neurone comprendra ```18 x 18 = 324``` poids plus un éventuel biai à optimiser, alors qu’en utilisant un filtre de taille ```3 x 3```, chaque neurone n’est lié qu’à une petite partie de l’objet qui réduit le nombre de poids à calculer à ```3 x 3 = 9``` plus un éventuel biai.



    4. Partage de paramètre

Un exemple de réseau qui a fait grand bruit dans le monde du machine learning est celui construit par [Krizhevsky](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks) pour la reconnaissance d’image. Ce réseau prend en entrée des images de taille ```227 x 227 x 3```, ```227```pixels en hauteur et largeur et trois valeurs par pixel associées à l’intensité des trois couleurs primaires : rouge, vert et bleu.

Le réseau utilise des filtres de taille ```11 x 11```, un pas de ```4``` et pas de padding. Chaque niveau de profondeur du réseau contient donc ```(227 - 11) / 4 + 1 = 55``` filtre en largeur et le même nombre en hauteur, ce qui fait ```55 x 55``` filtres. De plus, le réseau est d’une profondeur ```K = 96```, chaque zone couverte par un filtre est donc regardé par ```96``` filtres différents.

Chaque filtre a donc ```11 x 11 x 3 = 363``` paramètres et un biai, ce qui fait que chaque couche le long de la profondeur contient ```364 x 55 x 55 = 1 101 100``` poids, ce qui en tout donne ```1 101 100 x 96 = 105 705 600``` poids à optimiser au total. Cette quantité de paramètres n’est pas un choix très judicieux à priori car non seulement le temps de calcul nécessaire pour optimiser le réseau sera très long, mais on risque de tomber rapidement dans une situation de sur-apprentissage.

Pour pallier cette difficulté, on considère l’idée suivante : si une certaine association de poids au niveau d’un filtre (donc une zone déterminée de l’image) est utile pour analyser l’image, alors cette même association de poids peut être utilisée pour analyser d’autres zones de l’image! On va donc contraindre les filtres de chaque couche le long de la profondeur à partager les même paramètres, de manière à n’avoir à déterminer que ```96``` associations de paramètres différents. Cette idée nous permet de réduire la quantité de paramètres à calculer drastiquement puisqu’il suffit d’optimiser ```96``` associations de ```11 x 11 x 3 + 1 = 364``` paramètres, soit l’équivalent d’un seul filtre. Le nombre de paramètres à optimiser devient alors ```96 ( 11 x 11 x 3 + 1) = 34 944``` ce qui est un problème beaucoup plus accessible et raisonnablement proportionné à la tâche de la reconnaissance d’image.
