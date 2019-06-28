
##
    Séries temporelles


[TOC]



## Ce que vous apprendrez dans ce cours

Ce cours a pour ambition de vous apprendre tout ce qu’il y a à savoir sur l’analyse élémentaire des séries temporelles. Nous verrons comment lisser une série pour visualiser ses évolutions, comment extraire la tendance et les saisonnalités de séries temporelles. Pour finir nous verrons comment choisir les modèles les plus appropriés afin de modéliser une série temporelle et comment prédire les prochaines valeurs d’une séries temporelle.



    1. Définition


Une série temporelle est une succession ordonnée de valeurs d’une variable qui sont toutes séparées par un même intervalle de temps. Par exemple si on mesure tous les jours le cours du pétrole à midi pendant sept jours, on obtient une série temporelle de période 1 jour comprenant sept observations consécutives. Ce chapitre introduit l’étude des séries temporelles.


    2. Applications

Deux usages courants des séries temporelles sont :
*   Comprendre les lois sous-jacentes qui régissent et et structure les données observées
*   Construire des modèles de prédiction qui permettent d’anticiper les futures valeurs de la série de manière à prendre des décisions ou monitoré la série.
Les champs d’application des séries temporelles sont très variés : économie, prévision de ventes, analyse budgétaire, analyse boursière, prévision de rendement, logistique et inventaire et bien d’autres encore.


    3.  Analyse des séries temporelles


Nous allons ici voir différentes manières d’analyser les séries temporelles de différentes techniques et explorer différentes caractéristiques remarquables des séries temporelles.


    a. Moyennes mobiles et techniques de lissage


La plupart des séries temporelles ne se comportent pas comme des fonctions simples du temps, leurs variations peuvent souvent sembler assez imprévisible, c’est pourquoi il existe un certain nombres de techniques qui vont permettre de transformer une série temporelle difficilement compréhensible en une version très simplifiée. C’est techniques sont ce qu’on appelle du lissage et permettent comme leur nom l’indique, d’obtenir des versions résumées des séries temporelles dont les variations sont très atténuées afin d’en extraire la tendance générale.
De manière générale il existe deux grandes familles de techniques de lissage, les moyennes mobiles et les technique de lissage exponentiel.


    i.  Moyenne mobile simple


Une technique de lissage très courante et très simple à comprendre et interpréter des séries temporelles. Imaginons que nous étudions la séries temporelle qui donne les montants dépensés par une entreprise en matières premières par jour cette série temporelle est notée *X* est la réalisation de *X* à la date *t* est notée <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t" />. On définit l’ensemble des moyennes mobiles associées à cette série, l’ensemble des séries temporelles de la forme :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;M_t=\frac{X_t+X_{t-1}+...+X_{t-N+1}}{N}" />

Dit simplement, une moyenne mobile d’ordre par exemple 3 est la moyenne de l’observation courante et des deux observations précédentes à chaque date (c’est à dire chaque date pour lesquelles on dispose d’au moins deux observations précédentes).


![tab_moy_mobile_simple](https://drive.google.com/uc?export=view&id=1JyGFi5y9re0zsr7xuf6-8PHeOXJa5l9c)


Afin d’évaluer la qualité d’adhésion entre la moyenne mobile et les données réelles on calcule souvent la moyenne des erreurs au carré (Mean Squared Error MSE) qui ici vaut 7.71.


    ii.  Moyenne mobile centrée


Dans l’exemple précédent, on a calculé la moyenne mobile d’ordre 3, la première date à laquelle la moyenne mobile était définie était *t=3*. On aurait pu choisir par exemple de placer cette valeur au niveau de l’observation *t=2* afin de centrer la première valeur au centre de l’intervalle utilisé pour son calcule, et on procède de la même manière pour toutes les valeurs suivantes. Cette méthode fonctionne bien pour les ordres de moyenne mobile impaires car le centre de l’intervalle est un nombre entier, mais pas si bien que ça pour les ordres pairs car la valeur qui coupe l’intervalle en deux partie égale est un nombre décimal.



![tab_moy_mobile_centree](https://drive.google.com/uc?export=view&id=1jMLArRoLEZVjS22wBlczv2rFVAT-JEvR)



Dans l’exemple ci-dessus, on représente les moyennes mobiles centrées d’ordre 4 et 3. La caractéristique principale des moyennes mobiles est que toutes les observations précédentes utilisées pèsent le même poids dans le calcul des valeurs de la série lissée.
Nous allons voir comment une autre forme de pondération des observations permet également de construire des séries lissées.


    iii.	Lissage exponentiel simple


Le lissage exponentiel est une méthode très populaire pour le calcul de séries temporelles lissées qui assigne des poids qui décroissent de manière exponentielle plus les observations sont ancienne par rapport au point à estimer. Cela entraîne que les observations les plus proches du point à estimer se verront assigner un poids relativement beaucoup important que les observations plus anciennes.
On notera la série lissée exponentielle <img src="https://latex.codecogs.com/svg.latex?\Large&space;S_t" /> et la série originale est toujours <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t" />. <img src="https://latex.codecogs.com/svg.latex?\Large&space;S_2" /> prend la valeur <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1" />, <img src="https://latex.codecogs.com/svg.latex?\Large&space;S_3=\alpha{X_2}+(1-\alpha)S_2" />, puis de manière récurssive :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;S_t=\alpha{X_{t-1}}+(1-\alpha)S_{t-1},\;0<\alpha\leq{1,t}\ge3" />


Ceci est l’équation de base du lissage exponentiel, qui suffit à définir toute la série lissée de manière itérative. Plus α est proche de 1, plus la série sera proche en valeur de <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1" /> est attribuera un poids très faible aux précédentes observations. Plus α sera proche de 0, plus on donne de l’importance anciennes valeur de *X* pour calculer la série lissée. La valeur de α doit donc être choisie avec cette donnée en tête.
Exemple de séries temporelles lissées par lissage exponentiel


    iv.	Prédiction par lissage exponentiel simple


La formule qui permet de prédire les dates futures à partir de la série lissée construite grâce à la série originale est :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;F_{t+1}=\alpha{X_t}+(1-\alpha)S_t,\;0<\alpha<(1,t)>0" />


Ce qui permet d’obtenir les valeurs hypothétiques que la série prendra à l’avenir en partant du principe qu’elle préservera le même comportement pendant un certain nombre de prériodes.


    v. Lissage exponentiel double


Comme le montre l’exemple montré précédemment, le lissage exponentiel simple n’est pas une méthode qui permette de bien suivre la série temporelle originale si celle-ci suit on tendance générale. Cela peut être résolu par l’addition d’un terme supplémentaire dans l’équation de calcul des <img src="https://latex.codecogs.com/svg.latex?\Large&space;S_t" />.


<img src="https://latex.codecogs.com/svg.latex?\Large&space;S_t=\alpha{X_t}+(1-\alpha)(S_{t-1}+b_{t-1}),\;0\leq\alpha\leq{1}" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;b_t=\gamma(S_t-S_{t-1)+(1-\gamma)b_{t-1}},\;0\leq\gamma\leq{1}" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;b_t" /> est l’élément censé représenter la tendance générale de la série temporelle, et d’éviter ainsi les décrochages observés dans l’exemple précédent. Il s’agit en tout cas dans un premier temps de choisir la valeur initiale de ce terme <img src="https://latex.codecogs.com/svg.latex?\Large&space;b_t" />. Les suggestions les plus courantes sont :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;b_1=X_2-X_1" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;b_1=\frac{1}{3}[(X_2-X_1)+(X_3-X_2)+(X_4-X_3)]" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;b_1=\frac{X_n-1}{n-1}" />



Peu importe quelle formule l’on choisit pour l’initialisation, tant que cette dernière représente d’une certaine façon la tendance de la série. Schématiquement, plus <img src="https://latex.codecogs.com/svg.latex?\Large&space;\gamma" /> est proche de 0, plus les variations antérieures de la série auront de l’importance dans l’estimation du terme de tendance, inversement plus <img src="https://latex.codecogs.com/svg.latex?\Large&space;\gamma" /> sera grand, plus le terme de tendance sera la réflexion des variations immédiates de la série.


    vi.  Prédiction par lissage exponentiel double


Si on cherche à prédire la valeur prise par la série temporelle *X* à la date *t+1*, qui est la première date suivant la dernière observation disponible, la prédiction par lissage exponentiel double est donnée par la formule suivante :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;F_{t+1}=S_t+b_t" />

C’est donc la somme du dernier terme de la série lissée et du dernier terme de tendance calculé.
Si par contre on cherche à prédire la valeur de la série originale à la date *t+m*, la formule est légèrement modifiée :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;F_{t+m}=S_t+mb_t" />

Qui est la somme de la dernière valeur disponible de la série lissée à laquelle on ajoute *m* fois le terme de tendance. Ceci est logique car le terme <img src="https://latex.codecogs.com/svg.latex?\Large&space;b_t" /> est construit de manière à représenter le coefficient directeur d’une éventuelle tendance linéaire de la série originale *X*.


    vii.  Lissage exponentiel triple


Le lissage exponentiel triple est un nouveau niveau de raffinement pour le lissage des séries temporelles qui cette fois prendra en compte une éventuelle saisonnalité de la série temporelle considérée. La saisonnalité est un terme utilisé pour décrire tout phénomène qui affecte les valeurs d’une série temporelle à intervalle régulier. Par exemple, une série temporelle qui mesure les ventes d’un magasin comme les galeries Lafayette aura des périodes de comportement normal et des périodes de forte augmentation pendant les soldes et les périodes de fêtes, qui sont des événements qui reviennent chaque année autour des mêmes périodes.
Le lissage exponentiel triple est décrit par un jeu de plusieurs équations qui sont appelé la méthode de Holt-Winters pour l’analyse des séries temporelles, nommée ainsi d’après le nom de ses deux inventeurs.


![tab_formules](https://drive.google.com/uc?export=view&id=1oAiZuvpStOJWcisdv_cVJpU2B-h20E2X)


Dans les formules ci-dessus les paramètres on les significations suivantes:
* <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t" /> est la valeur que la série temporelle X prend à la date *t*
* <img src="https://latex.codecogs.com/svg.latex?\Large&space;S_t" /> est la valeur de la série triplement lissée à la date *t*
*	<img src="https://latex.codecogs.com/svg.latex?\Large&space;b_t" /> est la valeur de la série décrivant la tendance à la date *t*
*	<img src="https://latex.codecogs.com/svg.latex?\Large&space;I_t" /> est la valeur prise par l’indice de saisonnalité à la date *t*
*	<img src="https://latex.codecogs.com/svg.latex?\Large&space;F_{t+m}" /> est la valeur de la prédiction pour la date *t+m*
*	0<α<1,0<β<1,0< <img src="https://latex.codecogs.com/svg.latex?\Large&space;\gamma" /> <1 sont trois constantes qu’il convient de choisir de manière à réduire l’erreur moyenne commise lors du calcul de la série lissée.
*	*L* est un entier qui décrit le nombre de périodes qui constituent un cycle complet de la série temporelle (dans l’exemple des galeries lafayette *L* doit être égal à un nombre de périodes équivalent à une année, si une période représente un mois alors *L=12*, si une période est une semaine *L=52* et ainsi de suite)

Le modèle de Holt-Winter ne peut être estimé si l’on ne dispose pas au minimum d’un cycle complet de données, de plus, il est grandement conseillé en général de disposer de deux cycles complets ou plus afin d’obtenir de bons résultats.

***Exemple de lissage triple***


    b.  Propriétés des séries temporelles


On prendra comme exemples dans cette partie deux jeux de données communément utilisés pour illustrer les notions de modélisation que nous verrons dans ce qui suit. Il s’agit d’une série de concentration ce CO2 dans l’air, mesurée par un observatoire, l’autre série mesure la différentiel de pression atmosphérique au niveau de la mer entre deux points de la planète : [Hawaii](https://www.itl.nist.gov/div898/handbook/datasets/MLCO2MON.DAT) et [Tahiti les îles Darwin](https://www.itl.nist.gov/div898/handbook/datasets/ELNINO.DAT)
Nous allons maintenant découvrir des propriétés des séries temporelles qui correspondent à des hypothèses de bases nous permettant d’appliquer certains modèles d’analyse des séries temporelles.


    i.  Stationarité


La stationnarité est certainement la propriété des séries temporelles dont a le plus souvent besoin afin de pouvoir faire de la modélisation. Une série temporelle stationnaire a pour propriétés que sa moyenne, sa variance et la structure de ses corrélations ne changent pas au cours du temps, ce qui en termes mathématiques peut s’expliquer de la manière suivante :

*	<img src="https://latex.codecogs.com/svg.latex?\Large&space;E(X_t)=\mu,\forall{t}" />, chaque valeur de la série temporelle est considérée comme une réalisation particulière d’une variable aléatoire suivant une certaine loi, si cette loi reste inchangée au cours du temps, alors la moyenne des X_t devrait être constante.
*	<img src="https://latex.codecogs.com/svg.latex?\Large&space;V(X_t)=\sigma^2,\forall{t}" />, chaque réalisation de la série temporelle repose sur une variable aléatoire dont la variance est constante dans le temps.
*	<img src="https://latex.codecogs.com/svg.latex?\Large&space;Cov(X_t,X_{t-d})=\rho_d" />, les autocorrélations de la série avec elle même possède une structure qui ne dépend pas du temps, mais uniquement du décalage entre les périodes observées.
Les séries temporelles sont malheureusement très rarement stationnaires, il est donc souvent nécessaire de les différencier afin d’obtenir une série temporelle stationnaire à partir des données dont on dispose. Différencier une série temporelle correspond au fait de remplacer la série originale *X* par la série suivante :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y_t=X_t-X_{t-1}" />


Si la série originale suit une certaine tendance, linéaire par exemple, on peut estimer la nature de cette tendance et la soustraire aux données originales avec l’espoir que les résidus ainsi obtenus auront un comportement stationnaire.
Lorsque la variance de la série originale est non constante dans le temps, étudier le logarithme ou la racine carrée de la série permet parfois de stabiliser les propriétés de la variance dans le temps.
Ces techniques permettent d’obtenir des séries temporelles dont l’échelle et le niveau dans le temps sont constants dans le temps, cependant une propriété comme la saisonnalité contredit l’hypothèse de stationnarité. Cela n’est pas grave cependant, car la plupart des modèles sur les séries temporelles incluent une description des propriétés saisonnières.


     ii.  Saisonalité


De nombreuses séries temporelles présentent certains degrés de saisonnalité, c’est l’exemple des ventes aux galeries lafayette. Des techniques existent afin de repérer et décrire la saisonnalité des séries temporelles.
*	Une visualisation graphique des valeurs de la série au cours du temps permet en général de montrer assez facilement la présence ou non de saisonnalité.
*	Si on connaît la période de saisonnalité (12 mois dans le cas des galeries lafayette par exemple) alors il est possible de tracer un graphique où les valeurs pour chaque période du cycle sont représentée côte à côte et l’axe des abscisse ne comprend que les, ici 12, périodes constituants un cycle.
*	On peut également tracer une boîte à moustache pour chaque période du cycle qui aurait pour but de représenter la distribution des valeurs de la série pour chaque nouveau cycle.
*	La table des autocorrélations de la série peut permettre également de mettre en évidence la saisonnalité de la série temporelle, si la série <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t" /> et la série <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_{t-d}" /> sont fortement corrélées, alors on soupçonne la présence d’une saisonnalité de période *d*.


    c.  Modélisation des séries temporelles univariées


      i.  Bruit blanc


Un concept très utile lorsqu’on s’intéresse aux séries temporelles est celui de bruit blanc (white noise en anglais). Un bruit blanc ϵ est une série temporelle qui possède les propriétés suivantes:
*	<img src="https://latex.codecogs.com/svg.latex?\Large&space;E[\epsilon_t]=0" /> E[ϵ_t]=0 l’espérance d’un bruit blanc à toutes dates observée est nulle
*	<img src="https://latex.codecogs.com/svg.latex?\Large&space;E[\epsilon_{t}^2]=\sigma^2" /> la variance d’un bruit blanc est constante dans le temps
*	<img src="https://latex.codecogs.com/svg.latex?\Large&space;E[\epsilon_t,\epsilon_k]=0,t\neq{k}" /> les auto-corrélations du bruit blanc sont nulles
Le concept du bruit blanc est l’équivalent pour les séries temporelles des résidus pour les modèles d’apprentissage supervisé.


    ii.  Modèle auto-régressif


Le modèle auto-regressif est un modèle dans lequel la variable cible est la série temporelle elle-même, et les variables explicatives sont les dates antérieures de la même série temporelle. Mathématiquement cela s’écrit:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t=\delta+\Phi_1X_{t-1}+...+\Phi_pX_{t-p}+A_t" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t" />   est la série temporelle que l’on souhaite modéliser et <img src="https://latex.codecogs.com/svg.latex?\Large&space;A_t" /> est un bruit blanc et <img src="https://latex.codecogs.com/svg.latex?\Large&space;\delta=(1-\Sigma_{i=1}^{P}\Phi_i)\mu" />, où μ est la moyenne de la série temporelle <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t" /> .

Le modèle auto-régressif n’est donc ni plus ni moins qu’une régression linéaire de la série temporelle sur ses réalisations précédentes. La valeur p est appelée l’ordre du modèle autorégressif. Le modèle auto-régressif d’ordre *p* est noté *AR(p)*.
Il est important de noter qu’il est absolument nécessaire de s’assurer que la série temporelle à laquelle on s’intéresse est bien STATIONNAIRE avant de se lancer dans la modélisation.


    iii.  Modèle moyenne mobile


Une autre approche très courante pour modéliser les séries temporelles est le modèle des moyennes mobiles. L’idée est de faire une régression linéaire de la série temporelle sur les réalisation à différentes dates d’un bruit blanc de distribution souvent choisie comme gaussienne.


<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t=\mu+A_t-\Theta_1A_{t-1}-,...,-\Theta_qA_{t-q}" />

Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t" /> est la série temporelle que nous modélisons, μ est la moyenne de la série, <img src="https://latex.codecogs.com/svg.latex?\Large&space;A_t" /> est un bruit blanc, *q* est l’ordre du modèle de moyennes mobiles, noté *MA(q)*.
Il est encore une fois important de noter qu’un modèle *MA* ne peut fonctionner que s’il est appliqué à une série STATIONNAIRE.


    iv.  Modèle ARMA (Box-Jenkins)


Il arrive assez souvent que le modèle le plus pertinent afin de décrire une série temporelle stationnaire soit une combinaison d’un modèle auto-régressif et des moyennes mobiles, ce modèle appelé modèle de Box-Jenkins est noté ARMA(p,q) où p est l’ordre du modèle autorégressif et q l’ordre du modèle de moyennes mobiles. Mathématiquement, le modèle s’écrit ainsi :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_t=\delta+\Phi_1{X_{t-1}}+...+\Phi_p{X_{t-1}}+A_t-\Theta_1{A_{t-1}}-...-\Theta_q{A_{t-q}}" />

Ce modèle est très utile car en théorie toute série stationnaire peut être modélisée de cette façon, la difficulté est de trouver les ordres *p* et *q* adéquat. Nous allons voir tout de suite des techniques afin d’identifier les ordres susceptibles de fonctionner.


    v. Autocorrélations


Les coefficients d’autocorrélation sont définis par le calcul des corrélations entre la série originale et la série décalée dans le temps.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\gamma_d=Cov(X_t,X_{t-d})" />

En pratique on est obligé de calculer une estimation de ces coefficients d’autocorrélation de la manière suivante :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\widehat{r_d}=\frac{1}{T-d}\sum_{t-d+1}^{T}(X_T-\mu)(X_{t-d}-\mu)" />

Les valeurs des coefficients vont pouvoir être visualisés sous forme graphique et permettre de déduire la nature du modèle qui décrit les données.


    vi.	Autocorrélations partielles


Les coefficients d’autocorrelation partielle sont définis pour chaque ordre de décalage comme la corrélation de la série avec elle même, sans prendre en compte la contribution des dates antérieures. Mathématiquement cela s’écrit :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\rho_d=Corr(X_{T+d}-P(X_t|X_{t-1},...,X_1),X_t-P(X_t|X_{t-1},...,X_1))" />


De la même manière, on peut les visualiser pour obtenir des indices quand à la nature du modèle adequat.


    vii.  Spécification du modèle


L’allure du graphique des autocorrélations permet de déterminer la nature du modèle de la manière suivante :



![tab_ts_specif](https://drive.google.com/uc?export=view&id=1LF9379zg_QgIX_Gs3WNBKi85rw6VDqJ6)



Une fois l’analyse du graphe des autocorrélations effectuée, on utilise le graphe des autocorrélations partielles afin de déterminer l’éventuel ordre de la composante *AR* du modèle, la position du dernier coefficient d’autocorrélation partielle non nulle indique l’ordre du modèle *AR*.
