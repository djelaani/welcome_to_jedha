## Machine learning avancé


### Reinforcement learning


## Ce que vous apprendrez dans ce cours

Ce cours propose une introduction au vaste champ des possibles ouverts par le récent développement du reinforcement learning. Nous allons créer ensemble une véritable intelligence artificielle capable d’apprendre de zéro dans une situation très simplifiée.


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


En fonction des probabilité des actions HAUT et BAS, on fait un tirage aléatoire qui donnera la réponse HAUT avec une probabilité <img src="https://latex.codecogs.com/svg.latex?\Large&space;P_{HAUT}" /> et BAS avec une probabilité <img src="https://latex.codecogs.com/svg.latex?\Large&space;P_{BAS}" />. Cette action nous amène à un nouvel état du système, c’est à dire une nouvelle image qui sera envoyée comme entrée du réseau, cette action peut aussi entraîner une récompense, ou une punition dans le cas où le score change à l’issu de l’action et qu’une nouvelle manche commence. Nous exposons cette logique dans la figure suivante :


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

On initialise le policy network en choisissant au hasard les poids <img src="https://latex.codecogs.com/svg.latex?\Large&space;W_1" /> de la première couche et les poids <img src="https://latex.codecogs.com/svg.latex?\Large&space;W_Z" /> de la seconde couche du réseau. On laisse l’agent jouer 100 partie de Pong, en supposant que chaque partie dure 200 images, on obtient au total une collection de 20 000 décisions HAUT ou BAS. Pour chacune de ces décisions on peut calculer le gradient du réseau qui nous donne la manière dont nous devrions modifier les poids dans le réseau si nous voulions encourager ces actions à l’avenir. Tout ce qu’il nous manque est le résultat de la manche qui nous indique si les actions que nous avons entreprises étaient bonnes ou mauvaises. Supposons qu’on aie remporté 12 manches et perdu 88 manches du jeu, on considérera les ```12 x 200 = 2400``` actions qui ont mené à des victoire et leur appliquer un feedback positif, c’est à dire qu’on remplace l’inconnu dans la formule du gradient pour ces actions par ***+1*** et on change les poids dans le réseau en fonction. Pour les autres ``` 88 x 200 = 17 600``` actions qui ont mené à des défaites, on remplace l’inconnue dans les gradients pré calculés par ***-1*** et on applique les changements souhaités aux poids dans le réseau. Et voilà, grâce à cette première série de mises à jour, le réseau sera plus susceptible de reproduire des actions qui ont mené à des victoires et moins susceptible d’effectuer les actions qui ont mené à des défaites.

Si on repense à la manière dont on optimise un réseau de neurone dans le cadre du machine learning supervisé, les principes sont très similaire. En faisant jouer notre agent 100 parties, on a créé des données d’entraînement contenant ``` 200 x 100 = 20 000 ``` observations qu’on a labellisées à posteriori comme bonne ou mauvaise, calculé le gradient pour chaque observation et appliqué les changements grâce à la rétropropagation de l’erreur.

On répète ensuite le même procédé avec 100 nouvelles parties, on adapte les réseau en fonction de ces nouvelles parties et on itère jusqu’à obtenir un modèle capable de gagner le jeu de Pong.

Une question légitime qu’on peut se poser est : si certaines actions d’une partie perdue étaient en réalité de bonnes actions qui ont finalement mené à une défaite car les actions suivantes étaient mauvaises, ne risque t’on pas de diminuer aussi la probabilité de ces bonnes actions? La réponse est oui, cependant, on espère qu’en moyenne sur les très nombreuses partie qu’on aura fait jouer au système, les bonnes actions seront plutôt favorisées et les mauvaises plutôt rejetées.



    2. A partir de la fonction de coût (si on utilise des packages qui gèrent entièrement la rétro-propagation)

Si on utilise des package python comme Theano ou TensorFlow, qui se chargent entièrement de la rétropropagation et pour lesquels il est difficile de modifier les gradients en fonction des résultats d’une manche (car ils ont été construits à l’origine d’un point de vue apprentissage supervisé où l’on connaît les vraies valeurs de la variable cible). Alors on va utiliser la fonction de coût afin d’optimiser notre réseau et non pas modifier le gradient.

En machine learning supervisé, le but est d’optimiser la fonction de coût suivante (de manière schématique) :


<img src="https://latex.codecogs.com/svg.latex?\Large&space;P(A/B)=\sum_{i}log(p(y_i|x_i))" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i,\;y_i" /> sont les données d’apprentissage, respectivement les variables explicatives et la variable cible. Pour le reinforcement learning, on procède de la manière suivante :



*   On fait comme si la valeur de la variable cible <img src="https://latex.codecogs.com/svg.latex?\Large&space;y_i" /> est l’action entreprise par l’agent lorsqu’on lui fournit l’entrée <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" />
.
*   On modifie ensuite la fonction de coût en fonction du résultat de l’expérience (ici une manche de Pong).


<img src="https://latex.codecogs.com/svg.latex?\Large&space;\sum_{i}A_{i}log(p(y_i|x_i))" />


Où <img src="https://latex.codecogs.com/svg.latex?\Large&space;y_i" /> est l’action entreprise par l’agent exposé à l’état du système <img src="https://latex.codecogs.com/svg.latex?\Large&space;x_i" /> est <img src="https://latex.codecogs.com/svg.latex?\Large&space;A_i" /> est appelé l’avantage. Par exemple <img src="https://latex.codecogs.com/svg.latex?\Large&space;A_i=1" /> lorsque l’action *i* a mené finalement à une victoire et <img src="https://latex.codecogs.com/svg.latex?\Large&space;A_i=-1" /> si l’action *i* a mené à une défaite.



5. AI vs Intelligence humaine

En première conclusion de cette partie sur le reinforcement learning, qui permet à une machine d’effectuer des tâches complètes à la hauteur voire surpassant parfois l’intelligence ou le talent humains, nous reviendront sur les aspects qui différencient fondamentalement les intelligences artificielles des intelligences humaines.



*   En pratique, lorsque l’on donne une tâche à effectuer à quelqu’un, on l’exprime à travers le langage. Dans le cas du reinforcement learning, nous communiquons la tâche à effectuer via une fonction de récompense.
*   Les êtres humains commencent une partie de Pong armés de beaucoup de connaissances déjà acquise, comme des notions de physique et des idées de stratégie comme “si la balle rebondit de manière à bouger rapidement selon l’axe verticale, alors il est plus difficile d’anticiper ses mouvements”. Au contraire, notre algorithme démarre de zéro, ce qui est à la fois impressionnant car il parvient à apprendre beaucoup par lui-même, mais aussi alarmant car nous n’avons aucune idée de comment lui fournir ces connaissances à priori.
*   Le policy gradient repose sur la force brut, on doit donner au système un très très grand nombre d’exemple afin que le modèle parvienne à une solution satisfaisante. Les humains au contraire, construise une sorte de stratégie après très peu d’exemple et définisse une sorte de cadre logique des possibilités à explorer.
*   Le policy gradient ne peut améliorer le modèle que si il reçoit une récompense positive, sinon les actions continueront à être plus ou moins aléatoires. Alors que les humains peuvent se projeter dans l’avenir et imaginer à partir de leur expérience des manières d’obtenir de manière non aléatoire des récompenses.

Certaines tâches sont très difficile à appréhender avec le reinforcement learning à cause des raisons exprimées au dessus. Dans certains jeux par exemple, il est très improbables de parvenir au hasard à un enchaînement d’actions qui donneront au système une récompense, il est donc quasiment impossible de lui faire apprendre des comportements approprié dans un temps limité.
