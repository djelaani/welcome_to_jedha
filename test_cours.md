## Machine learning avancé


### Réseaux Long Short Term Memory (LSTM)


## Ce que vous apprendrez dans ce cours ?

Dans ce cours nous nous concentrerons sur l’apprentissage d’un modèle de deep learning qui peut s’utiliser dans toutes les situations où l’on s’intéresse à l’analyse de données dont la chronologie est importante et porteuse d’informations. C’est le cas bien évidemment des séries temporelles, mais aussi de l’analyse du langage où l’ordre des mots est très important.

L’idée générale derrière les réseaux LTSM est que les informations précédentes pourront conserver une influence sur les informations qui suivent immédiatement ou à plus long terme. Nous appliquerons ici ce modèle à la construction d’un traducteur automatique de l’anglais vers le français.


## Introduction

Les être humains ne réinitialisent pas le cours de leur pensée à chaque seconde qui passe, même si on dit que certaines personnes ont des mémoires de poisson rouge ! En effet, au fur et à mesure que vous lisez ce cours, les informations que vous avez lues précédemment vous sont utiles et sont mise à contribution par votre cerveau pour comprendre la suite de ce qui est expliqué. Vous n’oubliez pas instantanément à chaque mot que vous lisez le mot que vous avez lu juste avant. Vos pensées ont une certaine durée de vie.

Le problème est que les réseaux de neurones simples ne possèdent pas cette capacité de mémoire, ils traitent chaque information (image, mot, variable explicative) de manière séparée pour chaque observation, peut importe l'observation qu’ils ont traité juste avant. Imaginez que vous tentez de traduire un texte de l’anglais vers le français, un réseau de neurone classique pourra traduire les mots un à un littéralement, mais ne pourra pas utiliser le contexte pour aider la traduction du terme suivant.

Par exemple, la phrase :


<table>
  <tr>
   <td>I
   </td>
   <td>rose
   </td>
   <td>from
   </td>
   <td>the
   </td>
   <td>ashes
   </td>
  </tr>
</table>


Est traduite par “je me levais de mes cendres”, cependant sans le contexte certains mots ont plusieurs traductions possibles.


<table>
  <tr>
   <td>I
   </td>
   <td>rose
   </td>
   <td>from
   </td>
   <td>the
   </td>
   <td>ashes
   </td>
  </tr>
  <tr>
   <td>je
   </td>
   <td>rose
   </td>
   <td>de
   </td>
   <td>les
   </td>
   <td>cendres
   </td>
  </tr>
  <tr>
   <td>moi
   </td>
   <td>Me levais
   </td>
   <td>À partir de
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>


Ce n’est qu’en prenant en compte la totalité de la phrase que le mot “rose” est un verbe et doit être traduit par “me levais” et non pas un nom qui serait traduit par “rose”. Hors les réseaux de neurones simples sont incapable de prendre en compte ce contexte.

Les réseaux de neurones qui permettent de résoudre ce problème, ce sont des réseaux composés de neurones qui contiennent des boucles qui leur permette de prendre en compte les informations précédentes.



1.  Réseaux de neurones récurrents
    1. Neurones récurrents

Nous allons expliquer le principe d’un neurone récurrent à l’aide du diagramme suivant :






![](https://drive.google.com/uc?export=view&id=13XkLQCR0eZMA5QMGh7y6WrEC9kpLw61E)




Le neurone représenté dans le diagramme ci dessus par la case A, prend comme entrée ```x_t``` qui correspond à l’information qui entre dans le neurone (en général c'est un vecteur contenant les variables explicatives ou les sorties d’autres neurones du réseau), et qui génère une sortie ```h_t``` par sa fonction de combinaison et d’activation et une boucle permet à l’information d’être utilisée pour compléter l’information donnée par l’observation suivante.

Ces boucles rendent les réseaux récurrent quelques peu intrigants, mais quand on y réfléchit ils ne sont pas si différent des réseaux de neurones simples. On peut les imaginer comme plusieurs copies d’un même réseau qui donnent chacunes un message au réseau suivant. Graphiquement, cela peut se visualiser de la manière suivante :







![](https://drive.google.com/uc?export=view&id=13eq5WJVh2cjf811z0FPZ5U2b2EZMxlQg)









Les réseaux récurrents créent une chaîne d’information qui persiste d’observation en observation, cette structure de chaîne est intimement liées à des notions de listes ou de séquences. C’est pourquoi ces réseaux sont particulièrement adaptés pour analyser des données du type série temporelle ou texte.

Et ils sont très utilisés ! Ces dernières années, les réseaux de neurones récurrents ont montré leur efficacité pour traiter de nombreux problèmes : reconnaissance vocale, modélisation du langage, traduction, légendes d’images etc… Si vous souhaitez vous pencher sur les nombreuses applications possibles des réseaux de neurones récurrent, je vous encourage à vous diriger vers ce blog qui en fait l’exposé détaillé : [The unreasonnable effectiveness of recurrent neural networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/).

Une partie essentielle du succès rencontré par les réseaux de neurones récurrents viennent de l’utilisation des réseaux LSTM, une variété très particulière de modèles récurrents qui sont dans bien des cas beaucoup plus performants que la version standard.



    2. Problèmes des liaisons de long terme

L’avantage principal des réseaux de neurones récurrents est qu’ils sont capable d’utiliser l’information précédente pour résoudre la tâche présente, comme la connaissance du dernier mot traduit dans une phrase peut aider à traduire le mot suivant. Si les réseaux récurrents pouvaient faire cela de manière pertinente, ils seraient extrêmement utiles, mais le peuvent ils vraiment ?

Parfois, il suffit de prendre en compte l’information très récente pour résoudre la tâche présente. Par exemple, imaginons un modèle qui tente de prédire le mot suivant à partir du mot précédent. Si on essaie de prédire le dernier mot de la phrase “les nuages sont dans le _ciel” _on a pas besoin de plus d’information, il est assez évident que le dernier mot de la phrase sera _ciel. _Dans ce genre de situation où la tâche à effectuer et l’information utile pour nous assister dans cette tâche ne sont pas trop éloignés les réseaux de neurones peuvent apprendre à utiliser l’information précédente pour résoudre les problèmes présents._















![](https://drive.google.com/uc?export=view&id=1ztVRKSPdL0PuqvbFBTP29xvKSId-0e9a)







Mais il existe aussi des situations dans lesquels on a besoin d’un contexte plus riche ou plus ancien afin de mener à bien les tâches présentes. Imaginez le problème où l’on doit deviner le dernier mot du texte suivant : “J’ai grandi en France, près de Paris, dans une petite ville appelée Fontenay-sous-Bois, où j’ai passé onze an de ma vie, c’est pourquoi je parle couramment le _français.” _Dans cet exemple, l’information récente suggère que le dernier est certainement le nom d’une langue, mais si l’on souhaite deviner de quelle langue il s’agit exactement, on a besoin du contexte du début de la phrase qui parle de la France. Il arrive fréquemment que la distance entre l’information pertinente et le point où on en a besoin pour résoudre un problème devienne très grande._

Malheureusement, plus cette distance augmente, moins les réseaux de neurones récurrents sont capables de faire la connection entre les tâches courante et les informations pertinentes.









![](https://drive.google.com/uc?export=view&id=1b_jQnCNZpfvQC3nmAqLGswNe_VwHl3FD)







En théorie, les réseaux de neurones récurrents sont capables de gérer ce genre de “relations de long terme”. Un être humain pourrait sélectionner soigneusement les paramètres adaptés pour résoudre ce genre de problèmes. Malheureusement en pratique les réseaux de neurones récurrents classiques ne semblent pas capable de trouver eux mêmes ces paramètres lors de l’apprentissage. C’est pourquoi un modèle légèrement plus complexe et beaucoup plus utile a été développé, il s’agit des réseaux Long Short Term Memory!



2.  Réseaux LSTM

Les réseaux LSTM sont des réseaux de neurones récurrents capable de gérer et comprendre ces fameuses relations de long terme tout en conservant la capacité de comprendre les connections de court terme. Ils ont été inventés par [Hochreiter & Schmidhuber (1997)](http://www.bioinf.jku.at/publications/older/2604.pdf) et ont été améliorés et popularisés par de nombreux autres chercheurs par la suite. Ils fonctionnent de manière performante pour résoudre de nombreux problèmes et sont maintenant très utilisés.

Les LSTM ont été développé expressément afin d’éviter les difficultés liées au relations de long terme. Leur fonctionnement par défaut est précisément de conserver l’information sur le long terme et pas quelque chose qui doit être appris au cours de l’apprentissage des paramètres.

Tous les réseaux récurrents ont une structure de chaîne très similaire de plusieurs réseaux identiques qui donnent de l’information au réseau suivant. Pour les réseaux récurrents standards ces modules répétés adopteront une structure très simple comme une couche unique de ```tanh```.









![](https://drive.google.com/uc?export=view&id=1uQUEUTGNPSExO_x8tENy7tjmoysTSrnZ)








Ici, l’information actuelle et l’information donnée par le réseau précédent (qui traite l’observation précédente) sont sommées et envoyées dans une fonction ```tanh``` avant que le neurone en question produise une sortie ```h_t```.

Les réseaux LSTM ont une structure similaire en forme de chaîne, mais la liaison entre deux maillons de la chaîne est différente, au lieu d’une seule couche de réseau de neurones, il y en a quatre qui interagissent de manière précise :









![](https://drive.google.com/uc?export=view&id=1BZHPdgevIHRWK4qi7Os4XPIZ3r1-WlM5)















Ne vous inquiétez pas en constatant la complexité apparente de ce diagramme, nous expliquerons le fonctionnement en détail de ce modèle dans ce qui suit. Pour le moment, introduisons la charte visuelle utilisée :








![](https://drive.google.com/uc?export=view&id=1tlofNiMnCGZnAjzSauTcqum2TQKskEHy)








Dans le diagramme ci dessus, chaque ligne porte un vecteur entier qui correspond à la sortie d’un neurone qui est envoyée comme entrée d’un autre neurone. Les cercles rose représentent des opérations appliquées aux vecteurs élément par élément, comme l’addition de deux vecteurs, tandis que les rectangles jaunes sont des couches que le réseau va devoir optimiser (avec des poids etc…). Les lignes qui se rejoignent dénotent la concaténation de deux vecteurs, tandis qu’une ligne qui sépare en deux ligne signifie que le vecteur en question est dupliqué et chaque copie identique se dirige vers différentes destinations dans le réseau.



    3.  Idée centrales des LSTM

La clé des LSTM est l’état de la cellule, la ligne horizontale qui parcourt le diagramme de gauche à droite.

Cet état peut être vu comme le tapis roulant d’une chaîne de montage. Cet état parcourt toute la chaîne en subissant uniquement quelques transformation linéaire mineures, l’information traverse généralement la cellule sans être drastiquement modifiée.










![](https://drive.google.com/uc?export=view&id=1C38xfW-AJiwjEZg7erl-Luif5xdBAr3G)







Les LSTM ont la capacité de modifier l’état de la cellule en retirant ou ajoutant de l’information, ils peuvent le faire de manière soigneusement régulée par des structures appelées _portes._

Les portes sont des moyens de laisser passer des informations de manière optionnelle dans l’état du système. Elles se composent d’une couche neuronale comprenant une sigmoïde suivie d’une multiplication élément par élément.










![](https://drive.google.com/uc?export=view&id=1fdrNDGLEp9NIpDLwkflTJKuwdGYCQO76)














La couche sigmoïde produit un vecteur de nombres compris entre 0 et 1 qui décrit quelle proportion de chaque élément de l’état doivent être conservée à la suite de l’opération de multiplication élément par élément. Une valeur de zéro à la position ```i``` signifie, supprimer toute l’information issue de l’élément ```i``` du vecteur d’état, une valeur de un à la position ```i``` à la sortie de la sigmoïde signifie laisser toute l’information passer. On peut illustrer cette opération par le tableau suivant :


<table>
  <tr>
   <td>Position dans le vecteur d’état
   </td>
   <td>Valeur de l’état
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>1.05
   </td>
   <td rowspan="6" >






![](https://drive.google.com/uc?export=view&id=1fdrNDGLEp9NIpDLwkflTJKuwdGYCQO76)











   </td>
   <td>0.21
   </td>
  </tr>
  <tr>
   <td>...
   </td>
   <td>...
   </td>
   <td>...
   </td>
  </tr>
  <tr>
   <td>i
   </td>
   <td>3.76
   </td>
   <td>3.76
   </td>
  </tr>
  <tr>
   <td>i+1
   </td>
   <td>-2.37
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>...
   </td>
   <td>
   </td>
   <td>...
   </td>
  </tr>
  <tr>
   <td>n
   </td>
   <td>0.44
   </td>
   <td>0.22
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Position dans la couche sigmoïde
   </td>
   <td>Valeur dans la couche sigmoïde
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>1
   </td>
   <td>0.2
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>...
   </td>
   <td>...
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>i
   </td>
   <td>1
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>i+1
   </td>
   <td>0
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>...
   </td>
   <td>...
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>n
   </td>
   <td>0.5
   </td>
   <td>
   </td>
  </tr>
</table>


Les LSTM présentent trois portes qui permettent de contrôler et protéger l’état de la cellule.



    4.  Explication étape par étape des LSTM

La première étape des LSTM est de décider quelle information va t’on conserver ou défausser de l’état de la cellule. Cette décision est prise par une couche sigmoïde dont nous venons de discuter qu’on appelle la “porte de l’oubli” ou “forget gate layer”. Cette porte observe la sortie d’un neurone du réseau précédent (qui traitait l’observation précédente)
 ```h_(t-1)``` et l’observation en cours ```x_t``` (ou le cas échéant la sortie de la couche précédente si le neurone en question est sur une couche intermédiaire du réseau qui prend en entrée la sortie d’autres neurones du même réseau). Cette porte a pour sortie un vecteur de nombres compris entre 0 et 1 de la même taille que l’état de la cellule ```C_(t-1)```, un 1 représente “conserver complètement l’information”, 0 représente “supprimer complètement l’information”.

Revenons à notre exemple où l’on tente de prédire le prochain mot de la phrase en se basant sur les mots précédents. Dans un tel problème, l’état de la cellule peut par exemple contenir le genre du sujet de la phrase, de manière à utiliser les bons pronoms. Lorsqu’on rencontre un nouveau sujet, on souhaite oublier le genre du sujet précédent afin de le remplacer par le genre du sujet actuel.







![](https://drive.google.com/uc?export=view&id=1Vyoa4hWSOY2e7FQE91X21dhCx_yoOsR9)













Où Wf est le vecteur des poids utilisés par la couche sigmoïde, ```σ``` est la fonction sigmoïde, ```h_(t-1)``` est la sortie du neurone correspondant au neurone actuel dans le réseau traitant l’observation précédente, ```x_t``` est l’observation courante ou la sortie courante d’une couche précédente du réseau courant, ```b_f``` est le biais de la couche sigmoïde.

L’étape suivante consiste à décider quelles nouvelles informations vont être ajoutées à l’état de la cellule. D’abord nous avons une couche sigmoïde appelée “porte d’entrée” ou “input gate layer” qui permet de décider quelles informations ajouter (c’est à dire quels élément du vecteur conserver pour ajouter à l’état, c’est un filtre en quelques sortes). Ensuite une couche tangente hyperbolique ```tanh``` créée un vecteur de nouvelles valeurs candidates à partie de ```[h_(t-1), x_t]``` noté ```~C_t``` qui pourraient être ajoutées à l’état du système.

Dans l’exemple de notre modèle de langage, on souhaiterait ajouter l’information décrivant le nouveau genre du sujet à l’état de la cellule. Dans l’étape suivante nous allons combiner le filtre et ce nouveau vecteur afin de remplacer les anciens que nous avons oubliés.








![](https://drive.google.com/uc?export=view&id=1Ttoq0Ajixov3GJT8Fa-QclYQm3s3LlEH)














Où ```Wᵢ``` et ```bᵢ``` sont les poids et le biais associé à la couche sigmoïde de la couche “input gate layer” et ```W_c``` et ```b_c``` sont les poids et le biai associés à la couche tangente hyperbolique de la couche “input gate layer”.

Il maintenant temps de mettre à jour l’ancien état de la cellule, ```C_(t-1)``` pour produire le nouvel état de la cellule ```C_t```. Les étapes présentées précédemment se sont déjà chargées de décider quoi faire, il n’y a plus qu’à.

On multiplie élément par élément ```C_t``` par ```f_t``` pour oublier les éléments dont on a plus besoin (c’est la porte “forget gate layer”) et ensuite on somme ce produit élément par élément avec ```i_t * ~C_t``` (la porte “input gate layer”). On obtient ainsi ```C_t```.

Dans le cas de notre modèle de langage c’est là qu’on oublie l’information concernant le genre de l’ancien sujet et qu’on ajoute l’information donnant le genre du nouveau sujet de la phrase.









![](https://drive.google.com/uc?export=view&id=1rlC-M1NgPTLssL55AqqG_rV6zhtob9fo)







Finalement, on doit décider ce que l’on doit produire en sortie du neurone considéré (pour le moment on s’est occupé uniquement de l’état de la cellule, qui correspond à l’information qui voyage à travers les différents réseaux successifs qui traitent les observations successives de notre texte). Cette sortie va être basée sur l'état de la cellule, mais une version filtrée. Pour commencer, on a une nouvelle couche sigmoïde qui va décider quels composants de l’état de la cellule nous allons utiliser comme sortie. Ensuite nous utilisons une fonction tangente hyperbolique afin d’obtenir des valeurs comprises entre -1 et 1 qu’on multiplie élément par élément avec la sortie de la couche sigmoïde afin de conserver uniquement les éléments pertinents en sortie du neurone considéré.

Dans l’exemple du modèle du langage, comme on vient d’observer l’apparition dans la phrase d’un nouveau sujet, on va sans doute vouloir avoir en sortie des informations utiles pour les verbes ou les adjectifs, au cas où ces types de mots arrivent ensuite. Par exemple, on voudra sans doute savoir si le sujet et singulier ou pluriel afin de pouvoir conjuguer le verbe suivant ou accorder l’adjectif qui vient ensuite.







![](https://drive.google.com/uc?export=view&id=1puGXdAvImcegSZIbiUFEjLc8TpmfLPVQ)








Où ```W₀``` et ```b₀``` sont les poids et le biai de la porte de sortie “output gate layer”.



3.  Conclusion

On a mentionné plus tôt les résultats impressionnants obtenus grâce aux réseaux de neurones récurrent, ces derniers sont en grande partie dus au développement des LSTM. Ils fonctionnent vraiment mieux pour bien des tâches.

Posés simplement comme des systèmes d’équations, les LSTM paraissent très intimidants, mais pris étape par étape on se rend compte que les idées sous-jacentes sont assez intuitives. Surtout vous comprenez maintenant pourquoi les LSTMS ont cette capacité de mémoire à long terme! Pour faire simple, on a vu que l’élément essentiel de chaque neurone d’un réseau LSTM est l’état du système au niveau de ce neurone, qui est un vecteur qui voyage à travers les différents réseaux successifs qui traitent les informations successives. Cet état n’est modifié uniquement lorsqu’on se rend compte qu’une nouvelle information plus pertinente vient remplacer une information conservée en mémoire, ainsi pour reprendre notre exemple de modèle du langage, si la phrase ne contient qu’un seul sujet qu’on décrit longuement, alors l’information concernant le sujet restera stockée dans la variable d’état jusqu’à la fin de la série d’information à traiter, jusqu’à la fin de la phrase ou du texte! C’est à dire que sans aucun événement venant perturber l’état, le comportement par défaut du réseau et de conserver l’état tel qu’il est, d’où vient cette mémoire de long terme !

Les LSTM représentent une grande étape franchie dans le développement les réseaux récurrents, est ce qu’une prochaine étape est à anticiper ? Les chercheurs pensent que oui, et appellent cette nouvelle capacité “l’attention”. L’idée serait de permettre aux réseaux récurrents de pouvoir traiter une partie choisie des informations observées dans le problème considéré. Par exemple, si on souhaite utiliser un réseau récurrent pour donner une légende à une image, le réseau pourrait concentrer son attention sur une zone différente de l’image pour chaque mot ou groupe de mot que le réseau produit.

Ce cours est en grande partie inspiré par le post du blog suivant : [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/), d’où les diagrammes explicatifs sont tirés.
