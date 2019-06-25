## Semaine 5 : Machine learning non supervisé


1. Introduction

On a exploré précédemment de nombreuses techniques de machine learning supervisé, on disposait d’une variable cible dont on cherchait à comprendre et prédire le comportement. Nous allons maintenant nous intéresser au machine non supervisé, qui correspond aux situations dans lesquelles on ne dispose pas d’une variable cible que l’on cherche à prédire, cependant on émet l’hypothèse que les données dont on dispose peuvent être rapprochées au sein de groupes.


![S5_intro1](https://drive.google.com/uc?export=view&id=1nVYfEoJn1693JWQvjF4NgRdUdlZeTd-L)


La figure ci-dessus permet d’illustrer ce qu’est la différence entre l’apprentissage supervisé à gauche, où l’on sait que les croix sont différents des ronds et on cherche à les séparer, et l’apprentissage non supervisé à droite où les données ne sont pas labellisées comme différentes à priori, mais peuvent être séparée par d’autres méthodes, on voit bien dans la figure trois groupes cohérents apparaître.

Par exemple, si on se met à la place d’un directeur marketing d’un site de e-commerce, on dispose d’une base de données qui référence des clients, on connait le contenu de leurs paniers d’achats, leurs fréquences de visites et bien d’autres informations les concernant eux et leur comportement sur le site. Le directeur marketing essaiera souvent de rassembler ces clients au sein de classes afin de mieux comprendre les enjeux qui poussent certains individus à adopter certains type de comportements plutôt que d’autres. Par exemple on pourrait souhaiter identifier qui sont les parents, les étudiants, les jeunes cadres à fort revenus, les ménages plus modeste etc… Cependant le directeur marketing n’a pas à sa disposition une base de données dans laquelle cette information est renseignée dans une variable, il va donc devoir classer les clients sans pouvoir s’appuyer sur une variable cible, c’est là que le machine learning non supervisé intervient.

Nous allons maintenant rentrer dans le détail de trois techniques très populaires pour effectuer de l’apprentissage non supervisé.





2. K Means

Les K-Means ou K-moyennes en français, est une technique de partitionnement qui va séparer les observations en *K* groupes où chaque observations est considérées comme appartenant au groupe dont la moyenne est la plus proches selon une distance qu’on aura préalablement choisie.

L’algorithme des K-moyennes est très populaire car son fonctionnement est très facile à comprendre et à mettre en place, de plus, il peut s’appliquer à tous types de données à partir de moment où l’on est capable de définir une fonction qui donne la distance entre deux observations.

Introduisons dès maintenant l’algorithme des K-means et nous discuterons ensuite ses principales caractéristiques, ses avantages et inconvénients.



    1. Algorithme des K-means

Nous représenteront la logique de l’algorithme en illustrant à chaque fois par des images car le principe de cette technique est très simple à comprendre visuellement.

On dispose d’un jeu de données contenant 12 observations et deux variables quantitatives qui indiquent la position selon l’axe des *x* et des *y* des observations. On va appliquer l’algorithme des K-means à ce jeu de données afin de classer les observations :


![S5_intro2](https://drive.google.com/uc?export=view&id=1wRnUU_ol_BVUvdTEUjLly2huv3Fc-vTk)

![S5_intro3](https://drive.google.com/uc?export=view&id=1dqc7fSwE1FqKGfpeKt9zpRBQ9n3abjz)

![S5_intro4](https://drive.google.com/uc?export=view&id=12LbH-jL5h4QepmUP-0jP7UZeX38_6eNd)

![S5_intro5](https://drive.google.com/uc?export=view&id=1nVYfEoJn1693JWQvjF4NgRdUdlZeTd-L)




    2. Caractéristiques des K-Means

D’après l’algorithme que nous venons d’exposer, nous pouvons remarquer plusieurs caractéristiques remarquables de K-means.



*   On doit choisir à l’avance le nombre *K* de classes que l’on souhaite identifier parmi les observations. Cette contrainte implique un certain nombre de choses, on peut faire confiance à notre connaissance du sujet pour choisir *K*, par exemple, pour le dataset exemple qui référence les caractéristiques de différentes fleurs d’iris, on sait à l’avance que trois espèces distinctes sont acceptées par la communauté scientifique, on doit donc choisir *K=3*, on base donc notre choix de *K* en fonction des objectifs que l’on s’est fixé. Soit on cherche à optimiser un certain critère de distance entre les différentes classes, à ce moment là on va devoir explorer différentes valeurs de *K* et conclure une fois qu’on aura produit les différentes partitions et calculé leur score.
*   Les centres des classes sont déterminé au départ. Puisque les centres ne correspondent pas à des observations de notre jeu de donnée, on doit commencer par choisir leur position initiale. On peut évidemment choisir la position initiale des centres au hasard, mais ce choix n’est pas très judicieux car la position initiale des centres aura un impact à la fois sur la partition finale qu’on obtiendra et sur la vitesse de convergence des classes. Une méthode plus couramment utilisée est de choisir comme centres de départ les coordonnées des *K* observations les plus éloignées.
*   Choix de la distance. Les classes que l’on obtiendra au terme de l’algorithme dépendront de la distance choisie afin de mesurer l’éloignement des observations. Introduisons ici quelques exemple de distances qui sont utiles en machine learning et leurs différentes caractéristiques :




![S5_intro6](https://drive.google.com/uc?export=view&id=1W6pFxNWKRiinqVGXETSY5MdI_MMBLST6)

![S5_intro7](https://drive.google.com/uc?export=view&id=1b7tNnwUO49v5ZPvLsvknkIAJdJrzOxxJ)



    De nombreuses autres distances peuvent être utilisées si la situation est propice, mais ces exemples sont de loin les plus communément utilisés et permettent de résoudre la plupart des problèmes auxquels sont confrontés les data scientists.



*   Les K-means fournissent une partition unique des données, nous verrons par la suite que toutes les méthodes de classifications non supervisées ne suivent pas ce modèle.
    3. Remarques générales concernant les K-Means

En premier lieu, et comme à chaque fois qu’on fait appelle à des méthodes qui reposent sur des distances sensibles aux valeurs extrêmes et aux échelles de valeurs, il est important de se demander s’il est important de normaliser les variables que nous allons utiliser pour classer nos observations. La réponse est dans la grande majorité des cas OUI! Normaliser est essentiel dans la plupart des cas, sinon les variables dont l’amplitude de valeurs sont les plus grandes, ou celles dont toutes les valeurs sont très élevées pèseront beaucoup plus fortement que les autres. Il est donc conseillé de centrer et réduire les variables quantitatives, voir d’appliquer un logarithme sur certaines variables qui possèdent des valeurs aberrantes.

Il est essentiel également de traiter les variables qualitatives que vous souhaitez utiliser. Les variables ordinales (par exemple “très bon”, “bon”, “moyen”, “mauvais”, “très mauvais”) peuvent être remplacées par des valeurs numériques dans le même ordre. Les variables nominales devront par contre être transformées, on contruira une variable indicatrice pour chaque modalité (valant 1 si la modalité est vérifiée pour cette observation, 0 sinon).



    4. Avantages et inconvénients des K-Means

<table>
  <tr>
   <td>
<strong>Avantages</strong>
   </td>
   <td><strong>Inconvénients</strong>
   </td>
  </tr>
  <tr>
   <td>
<ul>

<li>Algorithme très simple à comprendre et à mettre en place

<li>Rapide

<li>Applicable à de très gros volumes de données et pour des datasets comprenant de très nombreuses variables
</li>
</ul>
   </td>
   <td>
<ul>

<li>Le nombre de classes doit être fixé au départ

<li>Le résultats dépend du choix initial des centres, ce qui nuit à la stabilité des résultats (deux choix de centres différents n’entraînent pas nécessairement la même partition)

<li>Les classes sont construites à partir de points qui n’existent pas dans les observations
</li>
</ul>
   </td>
  </tr>
</table>






3. Classification Ascendante Hiérarchique

La classification ascendante hiérarchique est une autre technique d’apprentissage non supervisé qui permet de classer une population de *n* observations dans un certain nombre de classes. L’algorithme repose sur une mesure de _dissimilarité_ entre les observations, autrement dit une distance. Elle est dite ascendante car le point de départ de cette méthode est une configuration dans laquelle chaque observation appartient à une classe qui lui est propre, on a donc autant de classes que d’observations dans la population. Elle est dite hiérarchique car elle se comporte à la manière d’un arbre avec des branches, cela signifie qu’au sommet de la hiérarchie, toutes les observations appartiennent à la même classe, en bas de la classification, on a autant de classes que d’observations, et pour toutes les classes intermédiaires deux classes intermédiaires n’ont soit aucune observation commune, soit l’une est incluse dans l’autre. Si l’on note la population <img src="https://latex.codecogs.com/svg.latex?\Large&space;\Omega=\{\omega_1,...,\omega_n\}" /> et l’ensemble des classes de la hiérarchie *H* on peut écrire mathématiquement ces propriétés de la manière suivante :



*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;\Omega\;\in\;H" />, l’ensemble contenant toute la population appartient à la hiérarchie
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;\forall\omega\;\in\;\Omega,\{\omega\}\;\in\;\H" />, tous les ensembles contenant une seule observation appartiennent à la hiérarchie
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;\forall{h,h'}\;\in\;H,h\cap{h'}=\emptyset\;ou\;h\subset{h'}\;h\supset{h'}" />, les classes de la hiérarchie sont soit distinctes soit incluses l’une dans l’autre.

Ces propriétés peuvent se comprendre facilement à l’aide d’une visualisation de l’arbre des classes, aussi appelé _dendrogramme._


![S5_intro8](https://drive.google.com/uc?export=view&id=1V-Uc6y1sPE_FDzfPCp4SvSCj6UXdqr5t)


Dans la figure ci-dessus, les observations sont représentées sur l’axe des abscisses, on parlera plus tard de l’axe des ordonnées, chaque branche représente une classe. On voit bien qu’en bas du dendrogramme on observe une branche pour chaque observation, et en remontant les branches fusionnent pour ne former plus qu’une branche/classe contenant toutes les observations se trouvant au bout de ces dernières.



1. Algorithme de formation de la classification ascendante hiérarchique.
    1. Principe général

Lors de l’étape initiale, chaque observation appartient à une classe qui lui est propre. A chaque étape à partir de là on fusionne ensemble les deux classes qui sont les plus “proches” au sens de la distance qu’on a choisi d’utiliser pour l’algorithme. La valeur de la dissimilarité ou distance minimale entre deux classes est appelé _indice d’agrégation._ Souvent les premiers indices d’agrégation sont faibles car les premières classes sont très proches, mais cet indice va croître au fur et à mesure des étapes de l’algorithme.



    2. Mesure de dissimilarité

La dissimilarité entre deux classes qu’on notera *d(h,h')* est l’élément essentiel de l’algorithme, c’est elle qui va déterminer de quelle manière les classes vont être formées. Lorsque les classes ne contiennent qu’un seul individu, la dissimilarité entre ces classes est égale à la dissimilarité entre les éléments qu’elles contiennent.



<img src="https://latex.codecogs.com/svg.latex?\Large&space;H=\{x\},{h'}=\{{x'}\},d(h,{h'})=d(x,{x'})" />


Lorsque les classes contiennent plusieurs éléments, il existe différentes manière de calculer leur dissimilarité que nous allons exposer maintenant.



*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,{h'})=\min_{x\in{h},{x'}\in{h'}}d(x,{x'})" />, la dissimilarité entre deux classes peut être égale à la dissimilarité minimum entre deux individus pris dans chaque classe.
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,{h'})=\max_{x\in{h},{x'}\in{h'}}d(x,{x'})" />, la dissimilarité entre deux classes peut être égale à la dissimilarité maximale entre deux observations prises dans chacune des classes.
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,h')=\frac{1}{Card(h)\cdot{Card(h')}}\sum_{x\in{h}}\sum_{x\in{h'}}d(x,x')" />, la dissimilarité entre deux classes peut être calculée comme la moyenne des dissimilarités entre chaque couples d’observations pris dans chaque classe.
*   <img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,h')=\frac{Card(h)\cdot{Card(h')}}{Card(h)+Card(h')}d(G,G')" />
, où *G, G'* sont les centres de gravité de *h, h'* respectivement. Cette mesure de dissimilarité est appelée la distance de Ward.

Dans tous les exemples de mesure de dissimilarité ci-dessus intervient l’objet mathématique *d* qui est une distance définie pour mesurer la distance entre deux observations et qui doit donc être choisie par le data scientist. On choisit souvent par défaut la distance euclidienne que nous avons vu précédemment, à condition d’avoir traité les données en amont afin qu’elles soient quantitatives et normalisées, pour éviter qu’une variables dont les valeurs sont plus grandes ne capture tout le pouvoir discriminant pour elle.



    3. Algorithme

L’algorithme de la classification ascendante hiérarchique peut se décrire de manière simple en utilisant du pseudo-code :



*   **Initialisation :** <img src="https://latex.codecogs.com/svg.latex?\Large&space;H_0=\{\{x_1\},...\{x_n\}\}" />, la hiérarchie contient toutes les classes à une seule observation.

*   **Tant que :**

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Omega\;\notin\;H_1:\\i=0\;\\i=i+1" />


Pour tout
<img src="https://latex.codecogs.com/svg.latex?\Large&space;h,h'\in\;H_{i-1},h\neq{h'}" />,
calculer
<img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h,h')" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;H_i=H_{i-1}-\{h_{min}\}-\{h_{min}^{'}\}+\{h_{min},h_{min}^{'}\}" />, on retire de la hiérarchie précédente les deux classes les plus proches et on ajoute la fusion des deux classes les plus proches qui vérifient

<img src="https://latex.codecogs.com/svg.latex?\Large&space;d(h_{min},h_{min}^{'})=\min_{h,h'\in{H_{i-1}},h\neq{h'}}d(h,h')" />


*   **Résultat :** <img src="https://latex.codecogs.com/svg.latex?\Large&space;\{H_0,H_1,...,H_1,\Omega\}" />. On obtient la hiérarchie complète.

Et ainsi on obtient le dendrogramme que nous avons pu observé précédemment.


![S5_intro9](https://drive.google.com/uc?export=view&id=1V-Uc6y1sPE_FDzfPCp4SvSCj6UXdqr5t)


On peut maintenant parler de l’axe des ordonnées que nous n’avions jusqu’alors pas commenté, il correspond à l’indices d’agrégation que nous calculons à chaque étape de l’algorithme, lorsque deux classes *h, h'* sont rassemblées en une, on forme un noeud dans le dendrogramme, la hauteur de ce noeud correspond à la valeur de *d(h,h').*



2. Comment déterminer la partition la plus pertinente.

Dans l’algorithme de classification ascendante hiérarchique que nous avons vu, les classes sont formées par agrégation de classes plus petites jusqu’à se retrouver avec une seule classe contenant toute la population. La hiérarchie obtenue permet de définir un grand nombre de partition des données possible, imaginez-vous que nous coupons l’arbre selon un axe vertical à une certaine hauteur, les classes que nous retiendrons seront les classes les plus basses parmi les classes se trouvant au-dessus de l’axe de coupe.



![S5_intro9](https://drive.google.com/uc?export=view&id=1rqcFjF6PispIlZLi_kG3PbdKKgSCuyx0)


Si on adopte cette coupe, on obtient en définitive les 5 classes suivantes :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;h_1=\{2,10\},h_2=\{5,8,9\},h_3=\{1,4\},h_4=\{3\},h_5=\{6,7\}" />

Il n’existe pas de technique qui fasse l’unanimité en termes de partition à retenir, cependant il existe des règles qui permettent de guider de votre choix afin de retenir la partition des données qui réponde le mieux à vos besoin ou à vos attentes.



*   Privilégier les troncatures de l’arbre au niveau de branches longues/hautes, plus la hauteur en ordonnée mesurée entre deux branches consécutives du dendrogramme, plus les classes ainsi formées seront éloignées les unes des autres. Si on coupe entre deux noeuds qui sont très proches au niveau du axes des ordonnées, cela signifie qu’on forme deux classes très proches quand on pourrait les rassembler pour n’en former qu’une qui resterait malgré tout assez cohérente. Une règle facile à mettre en application est de regarder la hauteur entre chaque noeuds consécutifs et de couper là où la différence entre deux hauteurs calculées est la plus grande. C’est ce qu’on a fait dans l’exemple au-dessus.
*   Si votre objectif n’est pas nécessairement d’obtenir les classes les plus grosses et les plus disparates possibles, mais qu’au contraire vous souhaitez également obtenir des classes dont les effectifs sont comparables, vous pourrez couper, si l’arbre s’y prête, au niveau qui vous donnera les classes les plus équilibrées. Attention, car il arrive souvent que les observations ne puissent pas naturellement être partitionnée de manière équilibrée.
*   Un critère populaire existe qui porte le nom de _critère de Ward_, qui repose sur une nouvelle mesure appelée _l’inertie._

    L’inertie d’une classe est définie de la manière suivante :


    ***Inertie totale:*** <img src="https://latex.codecogs.com/svg.latex?\Large&space;I_t=\frac{1}{n}\sum_{i=1}^{n}d(x_i,g)^2" />


    ***Inertie interclasse:*** <img src="https://latex.codecogs.com/svg.latex?\Large&space;I_e=\frac{1}{n}\sum_{i=1}^{k}n_i\cdot{d(g_i,g)^2}" />


    ***Inertie intraclasse:*** <img src="https://latex.codecogs.com/svg.latex?\Large&space;I_a=\frac{1}{n}\sum_{i=1}^{k}\sum_{j=1}^{n_i}{d(x_i,g_i)^2}" />


Où *n*  est le nombre d’observations, <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_1,...,x_n" /> est l’ensemble des observations, *d* est la distance choisie pour l’algorithme, *g* est le centre de gravité de la population, et <img src="https://latex.codecogs.com/svg.latex?\Large&space;g_1,...,g_k" /> sont les centres gravité respectifs des *k* classes formées par la classification ascendante hiérarchique avec une certaine coupure.

La méthode de Ward correspond à calculer l’inertie interclasse pour chaque niveau d’agrégation des données (c’est à dire à chaque étape de l’algorithme quand deux classes fusionnent) et retiendra comme dernière étape d’agrégation l’étape qui correspond à l’augmentation maximale de l’inertie interclasse.


##


4. T-SNE

Cette méthode, dont le nom est un acronyme pour “t-distributed stochastic neighbor embedding” est une méthode d’apprentissage non supervisée qui permet le tour de force de visualiser dans un espace de dimension petit (1 ou 2, une droite ou un plan) des données de très grandes dimension (c’est à dire avec de très nombreuses variables explicatives). L’idée sous-jacente est que si des clusters/groupes d’observations existent dans un espace de grande dimension, on doit pouvoir trouver un moyen de représenter ces groupes dans un espace de dimensions plus petite.



1. Principe général
    1. Objectif

Nous allons illustrer le principe général de cette méthode par des graphiques puisque le but final de T-SNE est de visualiser des cluster dans un espace de petite dimension. Comme nous ne pouvons pas visualiser des exemples en grandes dimensions, nous allons exposer les principes de la méthode pour un passage de deux à une dimension (un plan qui se projette sur une droite).


![S5_intro10](https://drive.google.com/uc?export=view&id=1TbiML4clQ07Do-1weAM5SJ33ZOVucBGG)



Maintenant qu’on comprends quel est le but de cette méthode, étudions son fonctionnement d’un peu plus prêt.



    2. Algorithme simplifié

Nous allons maintenant décrire le fonctionnement de l’algorithme de manière très imagée sans rentrer dans les détails afin que l’on comprenne bien comment il fonctionne, puis nous entrerons dans un second temps plus en profondeur dans les détails mathématiques.


![S5_intro10](https://drive.google.com/uc?export=view&id=192BHSmeheIRLQE7ap5LgceXM4jxwiC4i)


Cette explication très simplifiée a pour but de donner une intuition de l’algorithme, nous allons voir maintenant comment ce dernier fonctionne réellement et quelles sont les règles mathématiques qui nous permettent d’obtenir les résultats que nous avons exposés.



    3. Algorithme T-SNE

Si on repense au fonctionnement simplifié de l’algorithme de visualisation T-SNE, deux éléments sont extrêmement importants, la répartition dans l’espace original des points, et la répartition des points dans l’espace de plus petite dimension. Nous allons donc être amenés à calculer des distances dans les deux espaces et le but de l’algorithme sera d’amener les deux collections de distances à se ressembler le plus possible.


![S5_intro11](https://drive.google.com/uc?export=view&id=1Fr3TreiWcf9yJOxfaVg2S9m_S-0a45wk)


Une fois les deux familles de scores de similarité <img src="https://latex.codecogs.com/svg.latex?\Large&space;p_{j|i}" /> et <img src="https://latex.codecogs.com/svg.latex?\Large&space;q_{j|i}" /> définies, nous allons rentrer dans le coeur de l’algorithme. La famille <img src="https://latex.codecogs.com/svg.latex?\Large&space;p_{j|i}" /> est fixe, elle représente la vraie distribution des données dans l’espace de grande dimension. Notre but sera d’optimiser les <img src="https://latex.codecogs.com/svg.latex?\Large&space;q_{j|i}" /> afin qu’ils soient la meilleures représentation possible des <img src="https://latex.codecogs.com/svg.latex?\Large&space;p_{j|i}" />.

Pour mesurer l’adéquation entre les deux familles de scores de similarité, nous utiliserons la mesure de divergence de Kullback-Lieber, qui permet de comparer deux distributions par la formule mathématique suivante :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;KL(P||Q)=\sum_{i\neq{j}}p_{j|i}log(\frac{p_{j|i}}{q_{j|i}})" />

Cette divergence de Kullback-Lieber est grande lorsque les distributions sont très dissimilaire et petite lorsqu’elle le sont. Le but de l'algorithme sera d’optimiser de manière itérative les <img src="https://latex.codecogs.com/svg.latex?\Large&space;q_{j|i}" /> de manière à minimiser *KL(P||Q)*. Cette minimisation se fait de manière itérative pour chaque couple <img src="https://latex.codecogs.com/svg.latex?\Large&space;i,j\;;i\neq{j}" /> de points par la technique de la descente de gradient. A chaque étape de l'algorithme, on sélectionne un point *i*, et on calcule le gradient de *KL(P||Q)* par rapport à tous les points <img src="https://latex.codecogs.com/svg.latex?\Large&space;j\neq{i}" /> qui détermine la direction dans laquelle on va déplace le point *i* afin de minimiser *KL(P||Q)*. Le déplacement est donné par la formule de mise à jour suivante :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;y_i^{(n+1)}=y_i^{(n)}-y\sum_{i\neq{j}}p_{i|j}\frac{d}{dy_j}(log(\frac{p_{j|i}}{q_j|i}))" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;y_i^{(n+1)}=y_i^{(n)}-y\sum_{i\neq{j}}\frac{-p_{i|j}}{q_{j|i}}\cdot\frac{d}{dy_j}(q_{j|i})" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;y_i^{(n+1)}=y_i^{(n)}+y\sum_{i\neq{j}}\frac{p_{i|j}}{q_{j|i}}\cdot\frac{d}{dy_j}(q_{j|i})" />

De part la nature de la distribution originale,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;q_{j|i}" />

 chaque point sera plus attiré par les points proches de lui dans la distribution originale que par les autres points.

Une visualisation très simple de l’algorithme T-SNE en action peut être trouvée en suivant ce lien [T-SNE viz](https://www.oreilly.com/learning/an-illustrated-introduction-to-the-t-sne-algorithm).


5. DBSCAN

Le nom de cette méthode est un acronyme pour Density-Based Spatial Clustering of Applications with Noise, qui est un algorithme de classification non supervisé, qui comme son nom l’indique, s’appuie sur la densité des observations dans l’espace afin de former des clusters.



    5. Clusters de formes complexes

Nous avons vu jusqu’à maintenant un certain nombres de techniques qui permettent de classer des observations de manière non supervisé, et de visualiser des clusters dans des espaces de dimension réduite. Cependant les techniques de classification non supervisées que nous avons vues sont mal adaptées à des situations où les clusters que l’on cherche ne sont pas en forme de boule. Expliquons cette idée grâce à un exemple :


![S5_intro12](https://drive.google.com/uc?export=view&id=1S8QDZYLhB3HWf9rx4OgPC-UAUms630lz)


    6. Notions de densité

L’algorithme DBSCAN ne rencontre pas cette difficulté car il ne fait pas d’hypothèse sur la forme des classes ou cluster qu’il cherche à identifier, au lieu de cela il se base sur la densité des points dans l’espace des observations.

Une définition très simple de la _densité_ est de dire que la densité dans une zone donnée est égale au nombre d’observations situées dans cette zone.


![S5_intro13](https://drive.google.com/uc?export=view&id=1eyVLuEvY1zddFIb8VUTVlYZ_Ice9VKN4)


A partir de cette notion de densité, nous pouvons définir trois types de points.


![S5_intro14](https://drive.google.com/uc?export=view&id=1Njj0btVhU2g4skfFQvq5LArme8dFQVUO)

![S5_intro15](https://drive.google.com/uc?export=view&id=1bPgEaCINS-uXy00aS5y1tembjnXrRc9d)



    7. Algorithme DBSCAN

Le fonctionnement de l’algorithme DBSCAN n’est pas compliqué du tout, on peut le décrire de la manière suivante :



*   **Initialisation :**

    On  liste l’ensembles des observations, aucune d’entre elle n’a de classe assignée pour le moment.

*   **Itérations :**

    Tant que toutes les observations <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> ne sont pas classées:

*   Si <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> n’est pas classé alors :
    *   Si <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> est un _core point_ alors :
        *   Si il existe un point classé dans la classe *C* dans le voisinage de <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> alors : on ajoute <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> et toutes observations dans son voisinage à la classe *C*

        *   Sinon : on crée un nouveau cluster *C* dans lequel on ajoute <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> et toutes les observations
    *   Si <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> est un _border point_ alors : on ajoute <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> à la classe *C* du _core point_ classé le plus proche.
    *   Sinon on ajoute <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> à la classe *Noise*


L’algorithme est donc très simple à mettre en place, pas très technique dans sa dimension mathématiques et très pratique pour résoudre des problèmes de classification pour lesquels on suspecte des clusters de forme complexe.

Les seuls éléments qu’il est nécessaire de fixer pour utiliser l’algorithme sont :



*   La distance que l’on utilise pour mesurer l’espace des observations
*   *MinPts*, le nombre minimum de points nécessaires pour définir un _core point_
*   *d* la distance entre un point et les limites du voisinage qui l’entoure.
    8. Avantages et inconvénients de DBSCAN


![S5_intro16](https://drive.google.com/uc?export=view&id=1VYjgR0-p6r4rLUjmN3SeuSDbmFyMglXA)


Les inconvénient de cette méthode viennent principalement de la manière dont elle est construite : la définition des clusters est fondée sur la densité de point autour de chaque point, hors si la densité des observations dans l’espace varie, ou que certains clusters cohérents sont moins concentrés que d’autres, alors l’algorithme ne les reconnaîtra pas forcément comme appartenant à un seul et même cluster. En très grande dimension, les distances entre les observations tendent à s’agrandir énormément, ce qui rend très difficile pour l’algorithme d’identifier des régions de concentration suffisante pours définir des clusters. Enfin, la principale difficulté de la méthode DBSCAN est de bien choisir les paramètres *MinPts* et *d* qui permettent d’identifier les _core points._ Le choix de ces valeurs peut être guidé par une analyse de la densité des observations dans l’espace.

[methods for choosing optimal number of clusters](https://towardsdatascience.com/10-tips-for-choosing-the-optimal-number-of-clusters-277e93d72d92)
