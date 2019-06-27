# Les principes du cloud computing

## Le cloud computing


### Qu’est ce que le cloud computing ?

Le cloud computing consiste en l’exploitation de la puissance de calcul et de la capacité de stockage de serveurs distant par le biais d’internet. Autrement dit, cela vous donne la capacité d’utiliser un ordinateur que vous avez en votre possession pour en contrôler d’autres.

Plus concrètement les plateformes de cloud de computing vous permettent de louer des machines avec une très grande diversité de configurations disponibles pour s’adapter à différents besoins. Cette location peut s'effectuer selon différents modèles de coût : la quantité de donnée transférées sur le réseau, la puissance de calcul utilisée ou tout simplement le temps de location de la machine.


### Comment expliquer l’émergence du cloud computing ?

De façon générale les entreprises et les organisations ont tendance à se focaliser sur ce qui constitue leur cœur de métier. Dans la plupart des cas les services de gestion de matériel informatique sont des fonctions supports en entreprise, et si ces dernières sont essentielles pour son fonctionnement elles restent néanmoins souvent éloignées du reste de son activité.

L’externalisation de cette fonction est un moyen pour l’entreprise de ne pas se disperser en gérant les problématiques complexes liées au matériel informatique. De plus elle peut confier cette tâche à une organisation spécialisée (une plateforme de cloud computing) capable de gérer cela de façon plus efficiente.

A côté de cela, il existe d’autres raisons qui poussent les entreprises à adopter le cloud computing. D’abord, il peut s’agir d’une source d’économie car les coûts sont en lien avec l’utilisation. Si vous n’avez pas besoin de machines en permanence alors vous pouvez vous restreindre à en louer que lorsque cela est nécessaire. Ensuite, l’obsolescence n’est plus un problème à gérer, le matériel mis à disposition par les plateformes de cloud computing évolue en permanence. Enfin, pour les start-up et les petites entreprises cela permet de limiter l’investissement nécessaire au démarrage d’un projet nécessitant du matériel informatique.


## Les différents niveaux de service dans le cloud

Avant de s’intéresser davantage aux plateformes de cloud computing, il convient d’abord de distinguer les différents types de services qu’elles mettent à disposition des entreprises. On peut principalement les classer dans 3 catégories : Infrastructure / Plateforme / Software.

Le schéma ci-dessous permet d’effectuer la comparaison entre un modèle interne, c’est à dire une situation dans laquelle l’entreprise n’utilise pas le cloud computing et décide d’acheter et de gérer elle-même son matériel informatique, et les 3 autres typologies de service que nous venons d’évoquer.



![](https://drive.google.com/uc?export=view&id=16duJa00q4fbuFjUDUVQmniqqp9xk8klt)




### Le modèle interne

Sans le cloud computing l’entreprise doit totalement gérer ses machines, autrement dit choisir les composants matériels, effectuer les branchements pour les faire fonctionner ensemble, installer un système d’exploitation et des logiciels, puis éventuellement développer du code et gérer les flux de donnée.


### Le modèle infrastructure as a service (IaaS)

Dans le modèle IaaS on ne gère plus le matériel, c’est comme si vous veniez d’acheter un ordinateur vierge. Il vous suffira d’installer un système d’exploitation, de l’administrer puis d’installer les autres choses dont vous avez besoin… C’est le niveau de service le plus basique dans le cloud, l’entreprise continue de garder le contrôle sur tout ce qui ne concerne pas le matériel en lui-même.


### Le modèle plateforme as a service (PaaS)

C’est le niveau de service dont nous aurons le plus besoin. Ici le plateforme de cloud computing nous fournit du matériel prêt à l’emploi pour le développeur / data scientist. Pour reprendre la comparaison précédente c’est comme si vous achetiez un ordinateur avec un système d'exploitation déjà installé ainsi que tous les logiciels dont vous avez besoin pour développer. Tout ce qu’il vous reste à faire c’est commencer à coder et gérer les flux de données que vous manipulez (c’est à dire le download, l’upload et le stockage). Ce type de service permet entre autre de créer des bases de données ou des machines virtuelles en quelques cliques.


### Le modèle software as a service (SaaS)

C’est le niveau de service le plus complet dans le sens où son objectif est de mettre à disposition une application web pour l’utilisateur final. Dans cette situation celui que l’on appelle utilisateur final n’est pas un développeur, c’est une personne qui utilisera le logiciel pour ses besoin finaux. Vous êtes déjà tous habitués à ce type de service, il s’agit par exemple de l’application web vous permettant de consulter vos mail (gmail.com) ou bien de celle de votre banque qui vous permet de gérer vos compte. Dans les plateformes de cloud computing ce type service est en général plutôt à destination des experts métier comme par exemples les spécialiste du marketing.


## Les plateformes de cloud computing

Il existe aujourd’hui de nombreuses plateformes de cloud computing mais le marché se partage essentiellement entre quelques acteurs, principalement Amazon, Microsoft, Google et IBM. Vous pouvez constater sur le graphique ci-dessous qu’Amazon est de loin leader et est suivi par Microsoft qui jouit d’une plus forte croissance.


##

![](https://drive.google.com/uc?export=view&id=18ejo07Wi__wbAucrQMQmIAy5eNE6wCZa)


Comme toujours chaque plateforme a ses inconvénients et ses avantages. Pour choisir la bonne plateforme il faut tenir de différent facteurs comme le prix, les performances et la disponibilité de nombreux service qui répondent à vos propres contraintes et vos besoins spécifiques.

Dans votre cas vous avez besoin d’une plateforme qui vous permettra d'apprendre de façon efficace tout en vous permettant de réinvestir cet apprentissage dans un cadre professionnel. C’est cette dernière raison qui a dès le départ orienté notre choix sur Amazon (AWS) et Microsoft (Azure). Nous avons opté pour Azure car son utilisation est très répandu en France et qu’elle offre davantage de simplicité pour l’utilisation des technologie que nous cherchons à vous faire maîtriser dans ce cours.


## Microsoft Azure

Avant de passer à la pratique nous allons faire un rapide tour des différents éléments d’Azure que nous allons manipuler.


### Les groupes de ressource

Dans Azure, quelle que soit la ressource que vous voulez créer (un espace de stockage, une machine virtuelle, une base de données …) vous devrez préciser lors de sa création le groupe de ressource auquel elle appartient. Un groupe de ressource sert simplement à regrouper l'ensemble des ressources d’un projet dans une même groupe. Vous pourrez ensuite par exemple supprimer toutes les ressources d’un projet en supprimant son groupe de ressource. Le groupe de ressource est avant tout un outil qui vous permettra de mieux organiser votre utilisation de ressources dans le cloud.


### Le stockage dans Azure

Le stockage dans Azure est principalement organisé de la façon suivante :



*   Vous devez d'abord créer un compte de stockage. Ce n’est rien d’autres qu’un espace de stockage dans le cloud. Si vous avez plusieurs projets indépendants les uns des autres alors il semble logique de créer un espace de stockage par projet. Si vous devez partager des données avec l'extérieur assurez-vous de donner accès à un compte ne contenant que les données que vous souhaitez partager. Notez cependant que le transfert de données à l’intérieur d’un compte de stockage est bien plus rapide que le transfert d’un compte à un autre.
*   Ensuite à l’intérieur d’un compte de stockage vous devez créer des containers. Vous pouvez voir un container comme un dossier à la racine de votre disque dure. Chaque fichier que vous souhaitez mettre dans un compte de stockage devra nécessairement se situer dans un container. Vous pouvez également créer des sous-dossiers dans un container pour organiser vos données.


### Les machines virtuelles

Une machine virtuelle ou VM est simplement un ordinateur (on parle même plutôt de serveur) auquel vous allez pouvoir vous connecter à distance. Dans Azure vous pouvez créer une VM avec un très grand nombre de configuration relative au matériel (espace de stockage, mémoire RAM, processeur …) et au système (différentes version de Windows ou Linux). Il est pratique d’utiliser une VM dans tout un tas de situation en entreprise. Par exemple:



*   Pour accueillir des programmes automatisés qui se lanceront tout les jours sans que l’on ait besoin de gérer la machine
*   Pour disposer de machines plus puissantes que celle que l’on a à sa disposition


### Les bases de données

Les base de données que vous connaissez déjà ne sont rien d’autres que des VM sur lesquels ont été installés des logicielles de gestion de base de données comme SQL Server ou MySQL par exemple.


### La plateforme Databricks

Databricks est la société qui édite Spark. Afin de faciliter l’adoption de ce framework Databricks à créer une plateforme intégrant Spark dans une interface extrêmement pratique à utiliser pour les data scientist. Cette interface permet entre autre de déployer des clusters, créer des notebook et même générer des dashboard avec des graphiques pour faciliter l’analyse de données. La plateforme Databricks est disponible dans la *marketplace d’Azure.

*Les plateformes de cloud computing ne propose pas que leur propres produit, elles intègrent également des solution libre et propriétaire au travers d’une marketplace
